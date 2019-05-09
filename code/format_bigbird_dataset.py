import config
import os, shutil, tarfile, sys
import numpy as np
from PIL import Image
from PIL import ImageOps


def extract_files(tar_dir, untar_dir):
    for model_tar in sorted(os.listdir(tar_dir)):
        model = model_tar[:-4]
    
        print('Extracting model: ' + model)

        # Extract file
        tar = tarfile.open(os.path.join(tar_dir, model_tar), 'r:gz')
        tar.extractall(untar_dir)
        tar.close()


# Function adapted from: https://gist.github.com/sigilioso/2957026
def roi_resize_and_crop(img_path, modified_path, roi, size):
    """
    Resize and crop a ROI from an image to fit the specified size.
    args:
        img_path: path for the image to resize.
        modified_path: path to store the modified image.
        roi: `(left, upper, right, lower)` tuple.
        size: `(width, height)` tuple.
    raises:
        Exception: if can not open the file in img_path of there is problems
            to save the image.
    """
    # If height is higher we resize vertically, if not we resize horizontally
    img = Image.open(img_path)
    # Get current and desired ratio for the images
    img_ratio = img.size[0] / float(img.size[1])
    roi_ratio = (roi[2]-roi[0]) / float(roi[3]-roi[1])
    ratio = size[0] / float(size[1])
    # The new ROI is cropped vertically or horizontally depending on the ratio
    if ratio > roi_ratio:
        d = ((roi[3]-roi[1])*ratio - (roi[2]-roi[0]))/2
        roi_resized = (roi[0]-d, roi[1], roi[2]+d, roi[3])
        roi_img = img.crop(roi_resized)
    elif ratio < roi_ratio:
        d = ((roi[2]-roi[0])/ratio - (roi[3]-roi[1]))/2
        roi_resized = (roi[0], roi[1]-d, roi[2], roi[3]+d)
        roi_img = img.crop(roi_resized)
    else :
        roi_img = img.crop(roi)
    roi_img = roi_img.resize(size, Image.ANTIALIAS)
    roi_img.save(modified_path)


np.random.seed(0)

compr_dir = os.path.join(config.DATASET_DIR, 'model_zip')
q_compr_dir = os.path.join(config.DATASET_DIR, 'queries_zip')

# Extract files to get RGB frames
print('Extracting files')
extract_dir = os.path.join(config.DATASET_DIR, 'model_extract')
if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)
extract_files(compr_dir, extract_dir)

print('Extracting files (queries)')
q_extract_dir = os.path.join(config.DATASET_DIR, 'queries_extract')
if not os.path.exists(q_extract_dir):
    os.makedirs(q_extract_dir)
extract_files(q_compr_dir, q_extract_dir)

print('Processing files')
frame_dir = os.path.join(config.DATASET_DIR, 'model_frames')
if not os.path.exists(frame_dir):
    os.makedirs(frame_dir)

for model in sorted(os.listdir(extract_dir)):
    print('Processing model: ' + model)
    
    if not os.path.exists(os.path.join(frame_dir, model)):
        os.makedirs(os.path.join(frame_dir, model))
    
    top_left_corner = (sys.maxsize, sys.maxsize)
    bot_right_corner = (0, 0)
    
    # Use mask to extract ROI for that object
    print('    Compute ROI from masks')
    for el in range(1,6):
        for az in range(0,360,3):
            mask_file = os.path.join(extract_dir, model, 'masks/N%d_%d_mask.pbm' % (el,az))
            mask = Image.open(mask_file)
            mask_inv = ImageOps.invert(mask.convert('L')).convert('1')
            bbox = mask_inv.getbbox()
            top_left_corner = (min(top_left_corner[0], bbox[0]), min(top_left_corner[1], bbox[1]))
            bot_right_corner = (max(bot_right_corner[0], bbox[2]), max(bot_right_corner[1], bbox[3]))
    roi = top_left_corner + bot_right_corner
    
    # Crop and resize ROI
    print('    Resize/crop images')
    for el in range(1,6):
        for az in range(0,360,3):
            in_file = os.path.join(extract_dir, model, 'N%d_%d.jpg' % (el,az))
            out_file = os.path.join(frame_dir, model, 'N%d_%03d.jpg' % (el,az))
            roi_resize_and_crop(in_file, out_file, roi, (640,480))

print('Processing files (queries)')
queries_dir = os.path.join(config.DATASET_DIR, 'queries')
if not os.path.exists(queries_dir):
    os.makedirs(queries_dir)

for model in sorted(os.listdir(q_extract_dir)):
    print('Processing model: ' + model)
    
    if not os.path.exists(os.path.join(queries_dir, model)):
        os.makedirs(os.path.join(queries_dir, model))
    
    top_left_corner = (sys.maxsize, sys.maxsize)
    bot_right_corner = (0, 0)
    
    # Use mask to extract ROI for that object
    print('    Compute ROI from masks')
    for el in range(1,6):
        for az in range(0,360,3):
            mask_file = os.path.join(q_extract_dir, model, 'masks/NP%d_%d_mask.pbm' % (el,az))
            mask = Image.open(mask_file)
            mask_inv = ImageOps.invert(mask.convert('L')).convert('1')
            bbox = mask_inv.getbbox()
            top_left_corner = (min(top_left_corner[0], bbox[0]), min(top_left_corner[1], bbox[1]))
            bot_right_corner = (max(bot_right_corner[0], bbox[2]), max(bot_right_corner[1], bbox[3]))
    roi = top_left_corner + bot_right_corner
    
    # Crop and resize ROI
    print('    Resize/crop images')
    idx = np.random.choice(600, 5, replace=False)
    for i in idx:
        el = range(1,6)[i%5]
        az = range(0,360,3)[i/5]
        in_file = os.path.join(q_extract_dir, model, 'NP%d_%d.jpg' % (el,az))
        out_file = os.path.join(queries_dir, model, 'NP%d_%03d.jpg' % (el,az))
        roi_resize_and_crop(in_file, out_file, roi, (640,480))
