#!/usr/bin/python
# #### BEGIN LICENSE BLOCK ####
#
# bundler.py - Python convenience module for running Bundler.
# Copyright (C) 2013 Isaac Lenton (aka ilent2)
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# #### END LICENSE BLOCK ####

import gzip
import os
import sys
import glob
import subprocess
import tempfile
import multiprocessing
from PIL import Image
import shutil

import config

# This module replaces the existing RunBundler.sh script with a more
# cross platform implementation.  Additional elements replaced:
#   - RunBundler.sh             2008-2013 Noah Snavely
#   - ToSift.sh
#   - extract_focal.pl          2005-2009 Noah Snavely
#   - jhead

BIN_PATH = os.path.join(config.BUNDLER_DIR, "bin")
LIB_PATH = os.path.join(config.BUNDLER_DIR, "lib")
BIN_SIFT = None
BIN_BUNDLER = None
BIN_MATCHKEYS = None

FIXED_FOCAL_LENGTH = 534

input_dir = os.path.join(config.DATASET_DIR, 'model_frames_3fps')
output_dir = os.path.join(config.DATASET_DIR, 'bundler_output_3fps')

def get_images():
    """Searches the present directory for JPEG images."""
    images = glob.glob("./*.[jJ][pP][gG]")
    if len(images) == 0:
        error_str = ("Error: No images supplied!  "
                     "No JPEG files found in directory!")
        raise Exception(error_str)
    images_dict = {}
    for i in images:
        images_dict[i] = 0
    return images_dict

def sift_image(image, verbose=False):
    """Extracts SIFT features from a single image.  See sift_images."""
    global BIN_SIFT, BIN_PATH

    if BIN_SIFT is None:
        if sys.platform == 'win32' or sys.platform == 'cygwin':
            BIN_SIFT = os.path.join(BIN_PATH, "siftWin32.exe")
        else:
            BIN_SIFT = os.path.join(BIN_PATH, "sift")

    pgm_filename = image.rsplit('.', 1)[0] + ".pgm"
    key_filename = image.rsplit('.', 1)[0] + ".key"

    # Convert image to PGM format (grayscale)
    with open(image, 'rb') as fp_img:
        image = Image.open(fp_img)
        image.convert('L').save(pgm_filename)

    # Extract SIFT data
    if verbose:
        with open(pgm_filename, 'rb') as fp_in:
            with open(key_filename, 'wb') as fp_out:
                subprocess.call(BIN_SIFT, stdin=fp_in, stdout=fp_out)
    else:
        with open(pgm_filename, 'rb') as fp_in:
            with open(key_filename, 'wb') as fp_out:
                with open(os.devnull, 'w') as fp_err:
                    subprocess.call(BIN_SIFT, stdin=fp_in, stdout=fp_out,
                                    stderr=fp_err)

    # Remove pgm file
    os.remove(pgm_filename)

    # GZIP compress key file (and remove)
    with open(key_filename, 'rb') as fp_in:
        with gzip.open(key_filename + ".gz", 'wb') as fp_out:
            fp_out.writelines(fp_in)
    os.remove(key_filename)

    return key_filename

def sift_images(images, verbose=False, parallel=True):
    """Extracts SIFT features from images in 'images'.

    'images' should be a list of file names.  The function creates a
    SIFT compressed key file for each image in 'images' with a '.key.gz'
    extension.  A list of the uncompressed key file names is returned.

    If 'parallel' is True, the function executes SIFT in parallel.
    """
    global BIN_SIFT, BIN_PATH

    key_filenames = []

    if BIN_SIFT is None:
        if sys.platform == 'win32' or sys.platform == 'cygwin':
            BIN_SIFT = os.path.join(BIN_PATH, "siftWin32.exe")
        else:
            BIN_SIFT = os.path.join(BIN_PATH, "sift")
        
    if parallel:
        pool = multiprocessing.Pool()
        key_filenames = pool.map(sift_image, sorted(images))
    else:
        for image in sorted(images):
            key_filenames.append(sift_image(image))

    return key_filenames

def match_images(key_files, matches_file, verbose=False):
    "Executes KeyMatchFull to match key points in images."""
    global BIN_MATCHKEYS, BIN_PATH

    if BIN_MATCHKEYS is None:
        if sys.platform == 'win32' or sys.platform == 'cygwin':
            BIN_MATCHKEYS = os.path.join(BIN_PATH, "KeyMatchFull.exe")
        else:
            BIN_MATCHKEYS = os.path.join(BIN_PATH, "KeyMatchFull")

    keys_file = ""
    with tempfile.NamedTemporaryFile(delete=False) as fp:
        for key in key_files:
            fp.write(key + '\n')
        keys_file = fp.name

    # Add lib folder to LD_LIBRARY_PATH
    env = dict(os.environ)
    if env.has_key('LD_LIBRARY_PATH'):
        env['LD_LIBRARY_PATH'] = env['LD_LIBRARY_PATH'] + ':' + LIB_PATH
    else:
        env['LD_LIBRARY_PATH'] = LIB_PATH

    if verbose:
        subprocess.call([BIN_MATCHKEYS, keys_file, matches_file], env=env)
    else:
        with open(os.devnull, 'w') as fp_out:
            subprocess.call([BIN_MATCHKEYS, keys_file, matches_file],
                            stdout=fp_out, env=env)
            
    os.remove(keys_file)

def bundler(image_list=None, options_file=None, shell=False, *args, **kwargs):
    """Run bundler, parsing arguments from args and kwargs through.
    For Bundler usage run bundler("--help").

    image_list : File containing list of images.
    options_file : Specify an options file for bundler (optional).
    shell : Enable full shell support for parsing args (default: False).
    """
    global BIN_BUNDLER, BIN_PATH

    if BIN_BUNDLER is None:
        if sys.platform == 'win32' or sys.platform == 'cygwin':
            BIN_BUNDLER = os.path.join(BIN_PATH, "Bundler.exe")
        else:
            BIN_BUNDLER = os.path.join(BIN_PATH, "bundler")

    def kwargs_bool(b, r):
        if b: return r
        else: return []

    kwargs_dict = {
        'match_table'            : lambda k,v: ['--'+k,v],
        'output'                 : lambda k,v: ['--'+k,v],
        'output_all'             : lambda k,v: ['--'+k,v],
        'output_dir'             : lambda k,v: ['--'+k,v],
        'fixed_focal_length'     : lambda k,v: kwargs_bool(v, ['--'+k]),
        'init_focal_length'      : lambda k,v: ['--'+k,str(v)],
        'run_bundle'             : lambda k,v: kwargs_bool(v, ['--'+k]),
    }

    str_args = [a for a in args if type(a) == str]
    for k,v in kwargs.items():
        print k, v
        if not kwargs_dict.has_key(k): continue
        str_args.extend(kwargs_dict[k](k,v))

    if len(str_args) != 0 and options_file is not None:
        with open(options_file, 'wb') as fp:
            for o in str_args:
                if o.startswith('--'): fp.write('\n')
                else: fp.write(' ')
                fp.write(o)

    image_list_file = ""
    if type(image_list) == dict:
        with tempfile.NamedTemporaryFile(delete=False) as fp:
            for image,value in sorted(image_list.items()):
                if value == None: fp.write(image + '\n')
                else: fp.write(' '.join([image, '0', str(value), '\n']))
            image_list_file = fp.name
    elif type(image_list) == str:
        image_list_file = image_list
    else:
        raise Exception("Error: Not a valid list or filename for image_list!")

    # Add lib folder to LD_LIBRARY_PATH
    env = dict(os.environ)
    if env.has_key('LD_LIBRARY_PATH'):
        env['LD_LIBRARY_PATH'] = env['LD_LIBRARY_PATH'] + ':' + LIB_PATH
    else:
        env['LD_LIBRARY_PATH'] = LIB_PATH

    try:    os.mkdir("bundle")
    except: pass

    with open(os.path.join("bundle", "out"), 'wb') as fp_out:
        if options_file is not None:
            subprocess.call([BIN_BUNDLER, image_list_file, "--options_file",
                options_file], shell=shell, env=env, stdout=fp_out)
        else:
            subprocess.call([BIN_BUNDLER, image_list_file] + str_args,
                shell=shell, env=env, stdout=fp_out)

    if type(image_list) == dict:
        os.remove(image_list_file)

def run_bundler(images=[], verbose=False, parallel=True):
    """Prepare images and run bundler with default options."""
    # Create list of images
    if len(images) == 0:
        if verbose: print "[- Creating list of images -]"
        images = get_images()

    # Extract SIFT features from images
    if verbose: print "[- Extracting keypoints -]"
    key_files = sift_images(images, parallel=parallel, verbose=verbose)

    # Match images
    if verbose: print "[- Matching keypoints (this can take a while) -]"
    matches_file = "matches.init.txt"
    match_images(key_files, matches_file, verbose=verbose)

    # Run Bundler
    if verbose: print "[- Running Bundler -]"
    bundler(image_list=images,
            options_file="options.txt",
            verbose=verbose,
            match_table=matches_file,
            output="bundle.out",
            output_all="bundle_",
            output_dir="bundle",
            fixed_focal_length=True,
            init_focal_length=FIXED_FOCAL_LENGTH,
            run_bundle=True)

    if verbose: print "[- Done -]"

def change_dir_and_run_bundler(path):
    prevPath = os.getcwd()
    os.chdir(path)
    run_bundler(verbose=True, parallel=False)
    os.chdir(prevPath)
    print 'FINISHED MODEL ' + path

if __name__ == '__main__':

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # copy files in new directory
    model_dirs = []
    for model in sorted(os.listdir(input_dir)):
        db_path = os.path.join(input_dir, model)
        print db_path
        model_dir = os.path.join(output_dir, model)
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        for fil in sorted(os.listdir(db_path)):
            if fil.endswith('jpg'):
                shutil.copy(os.path.join(db_path, fil), os.path.join(model_dir, fil))
        model_dirs.append(model_dir)

    # run all Bundler instances in parallel
    p = multiprocessing.Pool()
    p.map(change_dir_and_run_bundler, model_dirs)
