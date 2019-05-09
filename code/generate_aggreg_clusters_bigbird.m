clear all;

[~,datasetDir] = system("python -c 'import config;print(config.DATASET_DIR)'");
datasetDir = deblank(datasetDir);
[~,outputDir] = system("python -c 'import config;print(config.OUTPUT_DIR)'");
outputDir = deblank(outputDir);

dbDir = [datasetDir '/model_frames'];
aggregClustersRootDir = [datasetDir '/aggreg_clusters'];
mkdir(aggregClustersRootDir);

% File containing the FVs for all frames (used for SIM)
frameFvsFile = [outputDir '/output_frame_descriptors/global_descriptors.txt'];

% Directory containing camera calibration information (used for POSE)
calibrationDir = [datasetDir '/model_extract/3m_high_tack_spray_adhesive'];

cluster_range = [1, 2, 3, 4, 6, 10, 16, 25, 40, 63, 100, 158, 251, 398, 600];

%% Get database info (model IDs and number of frames)

dbInfoFile = [datasetDir '/db_info.txt'];
if exist(dbInfoFile, 'file') == 2
    fid = fopen(dbInfoFile);
    C = textscan(fid, '%s %f');
    fclose(fid);
    modelIds = C{1};
    numFrames = C{2};
else
    models = dir(dbDir);
    modelIds = cell(numel(models)-2,1);
    numFrames = zeros(numel(models)-2,1);
    for i = 3:numel(models)
        modelIds{i-2} = models(i).name;
        numFrames(i-2) = numel(dir(fullfile(dbDir, models(i).name, '*.jpg')));
    end
    C = modelIds';
    for i =1:numel(numFrames)
        C{2,i} = numFrames(i);
    end
    fid = fopen(dbInfoFile,'w');
    fprintf(fid,'%s %d\n', C{:});
    fclose(fid);
end

%%

disp('Generating INDEP')

startIndex = [1;cumsum(numFrames(1:end-1))+1];
endIndex = cumsum(numFrames);

aggregClustersDir = fullfile(aggregClustersRootDir, 'aggreg_clusters_indep');
mkdir(aggregClustersDir);

for k = cluster_range

    disp(k)
    
    numClustersPerElev = floor(k/5) * ones(5,1) + [ones(mod(k,5),1); zeros(5-mod(k,5),1)];

    for model = 1:numel(numFrames)
        output = [k];
        numFramesInModel = endIndex(model) - startIndex(model) + 1;
        assert(mod(numFramesInModel,5) == 0, 'Incorrect number of images for current model')
        numFramesInModelElev = numFramesInModel/5;
        if k <= numFramesInModel
            for elev = 1:5
                numClusters = numClustersPerElev(elev);
                if numClusters == 1
                    output = [output; 1; 1 + (elev-1) * numFramesInModelElev];
                else
                    assert(numClusters <= numFramesInModelElev)
                    clusters = {};
                    for j = 1:numClusters
                        idx = round((j-1) * numFramesInModelElev / numClusters) + 1;
                        idx = idx + (elev-1) * numFramesInModelElev;
                        output = [output; 1; idx];
                    end
                end
            end
        else
            for j = 1:k
                output = [output; 1; min(j, numFramesInModel)];
            end
        end
        file = [aggregClustersDir '/' modelIds{model} '_' num2str(k) '.txt'];
        fid = fopen(file,'wt');
        for j = 1:numel(output)
            fprintf(fid,'%d\n',output(j));
        end
        fclose(fid);
    end

end

%%

disp('Generating RAND')

rng(42)

aggregClustersDir = fullfile(aggregClustersRootDir, 'aggreg_clusters_rand');
mkdir(aggregClustersDir);

for k = cluster_range

    disp(k)

    for model = 1:numel(numFrames)
        output = [k];
        numFramesInModel = endIndex(model) - startIndex(model) + 1;
        if k < numFramesInModel
            idx = randi([1 k], numFramesInModel, 1);
            clusters = {};
            for j = 1:k
                clusters{j} = find(idx == j);
                output = [output; numel(clusters{j}); clusters{j}];
            end
        else
            for j = 1:k
                output = [output; 1; min(j, numFramesInModel)];
            end
        end
        file = [aggregClustersDir '/' modelIds{model} '_' num2str(k) '.txt'];
        fid=fopen(file,'wt');
        for j = 1:numel(output)
            fprintf(fid,'%d\n',output(j));
        end
        fclose(fid);
    end

end

%%

disp('Generating SIM')

rng(42)

aggregClustersDir = fullfile(aggregClustersRootDir, 'aggreg_clusters_sim');
mkdir(aggregClustersDir);

if exist(frameFvsFile, 'file') ~= 2
    disp('Aborted: required data not generated yet')
else
    data = csvread(frameFvsFile);

    dimLDA = 32;
    numDesc = data(1);
    numGaussians = data(2);

    FV = double(dec2bin(data(3:end)) == '1');
    FV = reshape(FV', numGaussians * dimLDA, numDesc)';

    for k = cluster_range

        disp(k)

        for model = 1:numel(numFrames)
            output = [k];
            numFramesInModel = endIndex(model) - startIndex(model) + 1;
            if k < numFramesInModel
                [idx,C] = kmeans(FV(startIndex(model):endIndex(model),:),k,'Replicates',10);
                clusters = {};
                for j = 1:k
                    clusters{j} = find(idx == j);
                    output = [output; numel(clusters{j}); clusters{j}];
                end
            else
                for j = 1:k
                    output = [output; 1; min(j, numFramesInModel)];
                end
            end
            file = [aggregClustersDir '/' modelIds{model} '_' num2str(k) '.txt'];
            fid=fopen(file,'wt');
            for j = 1:numel(output)
                fprintf(fid,'%d\n',output(j));
            end
            fclose(fid);
        end

    end
end

%%

disp('Generating POSE')

rng(42)

aggregClustersDir = fullfile(aggregClustersRootDir, 'aggreg_clusters_pose');
mkdir(aggregClustersDir);

for k = cluster_range

    disp(k)
    
    % Get all camera positions
    cam_pos_all = [];
    for cam_idx = 1:5
        H = h5read([calibrationDir '/poses/NP5_0_pose.h5'], '/H_table_from_reference_camera')';
        M_table_to_cam = h5read([calibrationDir '/calibration.h5'], ['/H_N' num2str(cam_idx) '_from_NP5'])' * H^-1;
        M_cam_to_table = M_table_to_cam^-1;
        cam_pos = M_cam_to_table(1:3,4);
        % Get camera positions for all rotations around the z-axis
        for th = 0:3:357
            R = [cosd(th) -sind(th) 0
            sind(th) cosd(th) 0
            0 0 1];
            cam_pos_all = [cam_pos_all; (R*cam_pos)'];
        end
    end
    
    % Assign positions to one of k clusters
    output = [k];
    numFramesInModel = endIndex(1) - startIndex(1) + 1;
    if k < numFramesInModel
        [idx,C] = kmeans(cam_pos_all,k,'Replicates',10);
        clusters = {};
        for j = 1:k
            clusters{j} = find(idx == j);
            output = [output; numel(clusters{j}); clusters{j}];
        end
    else
        for j = 1:k
            output = [output; 1; min(j, numFramesInModel)];
        end
    end
    
    % Save same file for all objects
    for model = 1:numel(numFrames)
        file = [aggregClustersDir '/' modelIds{model} '_' num2str(k) '.txt'];
        fid=fopen(file,'wt');
        for j = 1:numel(output)
            fprintf(fid,'%d\n',output(j));
        end
        fclose(fid);
    end

end
