import config
import os, shutil, zipfile


data_FPS = 30


def unzip_files(zip_dir, unzip_dir):
    for model_zip in sorted(os.listdir(zip_dir)):
        model = model_zip[:-4]
    
        print('Unzipping model: ' + model)

        # Unzip file
        zip_ref = zipfile.ZipFile(os.path.join(zip_dir, model+'.zip'), 'r')
        zip_ref.extractall(os.path.join(unzip_dir, model))
        zip_ref.close()
    
        # Delete "depth" images (unused for this project)
        shutil.rmtree(os.path.join(unzip_dir, model, 'depth'))
    
        # Move all image files from "rgb" to parent directory
        for filename in os.listdir(os.path.join(unzip_dir, model, 'rgb')):
            shutil.move(os.path.join(unzip_dir, model, 'rgb', filename), os.path.join(unzip_dir, model, filename))
        shutil.rmtree(os.path.join(unzip_dir, model, 'rgb'))


def sample_frames(input_dir, output_dir, sampled_FPS):
    assert data_FPS % sampled_FPS == 0, 'Sampled frame rate should be an integer multiple of the original frame rate'
    step = data_FPS/sampled_FPS
    for model in sorted(os.listdir(input_dir)):
        print('Sampling frames from model: ' + model)
        
        output_sub_dir = os.path.join(output_dir, model)
        if not os.path.exists(output_sub_dir):
            os.makedirs(output_sub_dir)
        
        frames = sorted(os.listdir(os.path.join(input_dir, model)))
        for frame in frames[::step]:
            shutil.copy(os.path.join(input_dir, model, frame), os.path.join(output_dir, model, frame))
        

zip_dir = os.path.join(config.DATASET_DIR, 'model_zip')

# Unzip files to get RGB frames
print('Unzipping files')
unzip_dir = os.path.join(config.DATASET_DIR, 'model_unzip')
if not os.path.exists(unzip_dir):
    os.makedirs(unzip_dir)
unzip_files(zip_dir, unzip_dir)

# Sample frames at 1 FPS
print('Sampling files at 1 FPS')
sampled_frames_dir = os.path.join(config.DATASET_DIR, 'model_frames')
if not os.path.exists(sampled_frames_dir):
    os.makedirs(sampled_frames_dir)
sampled_FPS = 1
sample_frames(unzip_dir, sampled_frames_dir, sampled_FPS)

# Also sample frames at 3 FPS (will be used for SfM reconstruction)
print('Sampling files at 3 FPS')
sampled_frames_dir = os.path.join(config.DATASET_DIR, 'model_frames_3fps')
if not os.path.exists(sampled_frames_dir):
    os.makedirs(sampled_frames_dir)
sampled_FPS = 3
sample_frames(unzip_dir, sampled_frames_dir, sampled_FPS)

# Delete files with high sampling rate
shutil.rmtree(unzip_dir)

# Move queries to dataset
shutil.copytree('../data/sculptures_queries', os.path.join(config.DATASET_DIR, 'queries'))
