import subprocess, os, shutil, random

MODEL_FRAMES = 'model_frames'
MODEL_FRAMES_LISTS = 'model_frames_lists'
MODEL_INDEXES_DIR = 'model_indexes_%d'
VERBOSE = 1
SHOT_KEYF=-1

# Generate frame lists for all models
def generateFrameLists(INPUT_DIR):
	modelFramesPath = os.path.join(INPUT_DIR, MODEL_FRAMES)
	modelFramesListsPath = os.path.join(INPUT_DIR, MODEL_FRAMES_LISTS)
	if not os.path.exists(modelFramesListsPath):
		os.makedirs(modelFramesListsPath)
		for model in sorted(os.listdir(modelFramesPath)):
			imgFiles = []
			modelDir = os.path.join(modelFramesPath, model)
			for file in sorted(os.listdir(modelDir)):
				if file.endswith('.jpg'):
					imgFiles.append(os.path.join(modelDir, file))
			with open('%s/%s.txt' % (modelFramesListsPath, model), 'w') as listPath:
				for img in imgFiles:
					listPath.write('%s\n' % img)

def generateCustomShotLists(OUTPUT_DIR, INPUT_DIR, SHOT_FRAMES_DIR, numFilesInSequence):
	if not os.path.exists(os.path.join(OUTPUT_DIR, SHOT_FRAMES_DIR)):
		os.makedirs(os.path.join(OUTPUT_DIR, SHOT_FRAMES_DIR))
	allIndices = []
	curTotalNumFiles = 0
	for model in sorted(os.listdir(INPUT_DIR)):
		modelDir = os.path.join(INPUT_DIR, model)
		totalFilesInSequence = len([file for file in os.listdir(modelDir) if file.endswith('jpg')])
		allIndices.extend([curTotalNumFiles] * numFilesInSequence)
		curTotalNumFiles += totalFilesInSequence
	with open(os.path.join(OUTPUT_DIR, SHOT_FRAMES_DIR, 'shot_%d.txt' % numFilesInSequence), 'w') as f:
		for idx in allIndices:
			f.write('%d\n' % idx)

def generateGlobalFeatureAggregation(VIDEOSEARCH_DIR, OUTPUT_DIR, INPUT_DIR, CUSTOM_SHOT_DIR, numFilesInSequence, JOINT_INDEX_NAME, GAUSSIANS, SIFT_MODE, NUM_THREADS):
	modelFramesListsPath = os.path.join(INPUT_DIR, MODEL_FRAMES_LISTS)
        modelDirPath = os.path.join(INPUT_DIR, MODEL_FRAMES)
	modelIndexesDirPath = os.path.join(OUTPUT_DIR, MODEL_INDEXES_DIR % numFilesInSequence)
	if not os.path.exists(modelIndexesDirPath):
		os.makedirs(modelIndexesDirPath)
	LIST_INDEXES = 'list_indexes_%d.txt' % numFilesInSequence
	gdindexPath = '%s/indexer/global_descriptors/trained_parameters' % VIDEOSEARCH_DIR
	
	for model in sorted(os.listdir(modelDirPath)):
		listPath = os.path.join(modelFramesListsPath, model) + '.txt'
		outIndex = os.path.join(modelIndexesDirPath, model) + '.sift_scfv_idx'
		shotFile = os.path.join(CUSTOM_SHOT_DIR, '%s_%d.txt' % (model, numFilesInSequence))
		SHOT_MODE = 4
		cmd = '%s/indexer/global_descriptors/index_dataset -i %s -o %s -r %s -c %d -l %d -v %d -m %d -k %d -s %s' % (VIDEOSEARCH_DIR, listPath, outIndex, gdindexPath, GAUSSIANS, SIFT_MODE, VERBOSE, SHOT_MODE, SHOT_KEYF, shotFile)
		subprocess.call(cmd, shell=True)
	
	# Get list of indexes
	indexesPath = os.path.join(OUTPUT_DIR, LIST_INDEXES)
	with open(indexesPath, 'w') as f:
		for model_idx in sorted(os.listdir(modelIndexesDirPath)):
			f.write('%s/%s\n' % (modelIndexesDirPath, model_idx))
	
	# Compose output index name
	outIndex = os.path.join(OUTPUT_DIR, JOINT_INDEX_NAME)
	
	# Execute command
	cmd = '%s/indexer/global_descriptors/join_indexes -i %s -o %s -r %s -c %d -l %d -t %d -v %d' % \
		(VIDEOSEARCH_DIR, indexesPath, outIndex, gdindexPath, GAUSSIANS, SIFT_MODE, NUM_THREADS, VERBOSE)
	subprocess.call(cmd, shell=True)
	
	try:
		shutil.rmtree(modelIndexesDirPath)
	except:
		pass
	os.remove(indexesPath)

def generateGlobalFeatureFrame(VIDEOSEARCH_DIR, OUTPUT_DIR, INPUT_DIR, JOINT_INDEX_NAME, GAUSSIANS, SIFT_MODE, NUM_THREADS):
	modelFramesListsPath = os.path.join(INPUT_DIR, MODEL_FRAMES_LISTS)
        modelDirPath = os.path.join(INPUT_DIR, MODEL_FRAMES)
	modelIndexesDirPath = os.path.join(OUTPUT_DIR, MODEL_INDEXES_DIR % 0)
	if not os.path.exists(modelIndexesDirPath):
		os.makedirs(modelIndexesDirPath)
	LIST_INDEXES = 'list_indexes.txt'
	gdindexPath = '%s/indexer/global_descriptors/trained_parameters' % VIDEOSEARCH_DIR
	
	for model in sorted(os.listdir(modelDirPath)):
		listPath = os.path.join(modelFramesListsPath, model) + '.txt'
		outIndex = os.path.join(modelIndexesDirPath, model) + '.sift_scfv_idx'
		cmd = '%s/indexer/global_descriptors/index_dataset -i %s -o %s -r %s -c %d -l %d -v %d' % (VIDEOSEARCH_DIR, listPath, outIndex, gdindexPath, GAUSSIANS, SIFT_MODE, VERBOSE)
		subprocess.call(cmd, shell=True)
	
	# Get list of indexes
	indexesPath = os.path.join(OUTPUT_DIR, LIST_INDEXES)
	with open(indexesPath, 'w') as f:
		for model_idx in sorted(os.listdir(modelIndexesDirPath)):
			f.write('%s/%s\n' % (modelIndexesDirPath, model_idx))
	
	# Compose output index name
	outIndex = os.path.join(OUTPUT_DIR, JOINT_INDEX_NAME)
	
	# Execute command
	cmd = '%s/indexer/global_descriptors/join_indexes -i %s -o %s -r %s -c %d -l %d -t %d -v %d' % \
		(VIDEOSEARCH_DIR, indexesPath, outIndex, gdindexPath, GAUSSIANS, SIFT_MODE, NUM_THREADS, VERBOSE)
	subprocess.call(cmd, shell=True)
	
	try:
		shutil.rmtree(modelIndexesDirPath)
	except:
		pass
	os.remove(indexesPath)
