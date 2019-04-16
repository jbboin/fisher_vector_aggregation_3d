clear all;

[~,datasetDir] = system("python -c 'import config;print(config.DATASET_DIR)'");
datasetDir = deblank(datasetDir);
[~,outputDir] = system("python -c 'import config;print(config.OUTPUT_DIR)'");
outputDir = deblank(outputDir);

dbDir = [datasetDir '/model_frames'];
aggregClustersRootDir = [datasetDir '/aggreg_clusters'];
mkdir(aggregClustersRootDir);

% File containing the FVs for all frames (used for SIM)
frameFvsFile = [outputDir '/output_128_gauss_frame/global_descriptors.txt'];

% Frame-rate used for SfM reconstruction (used for POSE)
sfmFPS = 3;
% Directory containing output of SfM reconstruction for all models (used for POSE)
sfmDir = [datasetDir '/bundler_output_3dscan_3fps'];

cluster_range = [1, 2, 3, 4, 6, 10, 16, 25, 40, 63, 100, 158, 251, 398, 631];

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

    for model = 1:numel(numFrames)
        output = [k];
        numFramesInModel = endIndex(model) - startIndex(model) + 1;
        if k == 1
            output = [output; 1; 1];
        elseif k <= numFramesInModel
            clusters = {};
            for j = 1:k
                idx = round((j-1) * (numFramesInModel-1) / (k-1)) + 1;
                clusters{j} = idx;
                output = [output; numel(clusters{j}); clusters{j}];
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

disp('Generating TEMP')

aggregClustersDir = fullfile(aggregClustersRootDir, 'aggreg_clusters_temp');
mkdir(aggregClustersDir);

for k = cluster_range

    disp(k)

    for model = 1:numel(numFrames)
        output = [k];
        numFramesInModel = endIndex(model) - startIndex(model) + 1;
        if k <= numFramesInModel
            clusters = {};
            clusterStartIndex = round(((0:k-1)) * (numFramesInModel-1) / k) + 1;
            clusterEndIndex = [clusterStartIndex(2:end)-1 numFramesInModel];
            for j = 1:k
                idx = (clusterStartIndex(j):clusterEndIndex(j))';
                clusters{j} = idx;
                output = [output; numel(clusters{j}); clusters{j}];
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

        for model = 1:numel(numFrames)
            output = [k];
            numFramesInModel = endIndex(model) - startIndex(model) + 1;
            if k < numFramesInModel
                opts = statset('Display','final');
                [idx,C] = kmeans(FV(startIndex(model):endIndex(model),:),k,'Replicates',10,'Options',opts);
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

if exist(sfmDir) ~= 7
    disp('Aborted: required data not generated yet')
else
    data = dir(sfmDir);

    for bundleIdx = 3:numel(data)
        model = data(bundleIdx).name;
        fileToRead = [sfmDir '/' model '/bundle/bundle.out'];
        disp(fileToRead)
    
        fid = fopen(fileToRead,'r');
        if fid ~= -1
            fgetl(fid);
            fgetl(fid);
            camera_raw = [];
            while 1
                line = fgetl(fid);
                nums = str2double(strsplit(line));
                if numel(nums) ~= 3
                    break;
                else
                    camera_raw = [camera_raw; nums];
                end
            end
            N = floor(size(camera_raw,1)/5);
            camera_raw = camera_raw(1:N*5, :);

            validViews = [];
            for i = 1:N
                R(:,:,i) = camera_raw(5*i-3:5*i-1,:);
                tvec(i,:) = camera_raw(5*i,:);
                K(:,:,i) = diag([camera_raw(5*i-4,1)*[1;1]; 0]);
                k1(i) = camera_raw(5*i-4,2);
                k2(i) = camera_raw(5*i-4,3);
                if norm(R(:,:,i)) > 0.5
                    validViews = [validViews; i];
                end
            end
        
            % go back to 1FPS sampling (for frame aggregation)
            N1FPS = ceil(N/sfmFPS);
            tvec1FPS = [];
            validViews1FPS = [];
            validViewsCorresp = floor((validViews-1)/sfmFPS)+1;
            for i = 1:N1FPS
                frames = find(validViewsCorresp == i);
                if numel(frames) ~= 0
                    validViews1FPS = [validViews1FPS; i];
                    tvec1FPS = [tvec1FPS; tvec(validViews(frames(1)), :)];
                else
                    tvec1FPS = [tvec1FPS; zeros(1,3)];
                end
            end

            for k = cluster_range
                output = [k];
                if k < numel(validViews1FPS)
                    opts = statset('Display','final');
                    [idx,C] = kmeans(tvec1FPS(validViews1FPS,:),k,'Replicates',10,'Options',opts);
                    clusters = {};
                    for j = 1:k
                        clusters{j} = validViews1FPS(idx==j);
                        output = [output; numel(clusters{j}); clusters{j}];
                    end
                else
                    for j = 1:k
                        output = [output; 1; min(j, numel(validViews1FPS))];
                    end
                end
                file = [aggregClustersDir '/' model '_' num2str(k) '.txt'];
                fid=fopen(file,'wt');
                for j = 1:numel(output)
                    fprintf(fid,'%d\n',output(j));
                end
                fclose(fid);
            end
        
        else
            for k = cluster_range
                output = [k];
                for j = 1:k
                    output = [output; 1; 1];
                end
                file = [aggregClustersDir '/' model '_' num2str(k) '.txt'];
                fid=fopen(file,'wt');
                for j = 1:numel(output)
                    fprintf(fid,'%d\n',output(j));
                end
                fclose(fid);
            end
        end
        
    end
end
