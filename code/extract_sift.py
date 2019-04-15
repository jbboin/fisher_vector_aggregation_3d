import subprocess, os, shutil
from sys import platform
from multiprocessing import Pool

def extract(VIDEOSEARCH_DIR, DIR_TO_EXTRACT, SIFT_MODE, NUM_THREADS):
	IMG_FILE_NAME = 'frame_list.txt'

	filePaths = []

	for root, subdirs, files in os.walk(DIR_TO_EXTRACT):
		for file in files:
			if file.endswith('.jpg'):
				filePaths.append(os.path.join(root, file))

	print '%d image files found' % len(filePaths)

	if SIFT_MODE == 0:
		imgFilePath = os.path.join(DIR_TO_EXTRACT, IMG_FILE_NAME)
		imgFile = open(imgFilePath, 'w')
		for filePath in filePaths:
			print>>imgFile, filePath
		imgFile.close()

		subprocess.call('%s/indexer/local_descriptors/extract -s -i %s -t %d' % (VIDEOSEARCH_DIR, imgFilePath, NUM_THREADS), shell=True)

		os.remove(imgFilePath)
	else:
		global COMPUTE_DESCRIPTORS_BIN
		if platform == 'darwin':
			COMPUTE_DESCRIPTORS_BIN = '%s/indexer/local_descriptors/compute_descriptors_mac' % VIDEOSEARCH_DIR
		else:
			COMPUTE_DESCRIPTORS_BIN = '%s/indexer/local_descriptors/compute_descriptors_linux64' % VIDEOSEARCH_DIR

		pool = Pool(NUM_THREADS)
		pool.map(extractHessianAffine, filePaths)

def extractHessianAffine(file):
	fileName, fileExt = os.path.splitext(file)
	siftFile = '%s.siftgeo' % fileName
	pgmFile = '%s.pgm' % fileName

	# Check if output file already exists, if so we skip it
	if os.path.isfile(siftFile):
		return

	cmd = 'convert %s -set colorspace RGB -contrast-stretch 0.01%%x0.01%% -resize $[1024*768]@\> %s' % (file, pgmFile)
	print(cmd)
	subprocess.call(cmd, shell=True)

	cmd='time %s -i %s -o4 %s -hesaff -sift' % (COMPUTE_DESCRIPTORS_BIN, pgmFile, siftFile)
	print(cmd)
	subprocess.call(cmd, shell=True)

	os.remove(pgmFile)
