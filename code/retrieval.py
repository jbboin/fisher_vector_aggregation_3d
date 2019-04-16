import os, subprocess, shutil, random
from multiprocessing import Pool

def retrieveParallelFeatureAggregation(VIDEOSEARCH_DIR, OUTPUT_DIR, JOINT_INDEX_NAME, DB_DIR, QUERY_DIR, SHOT_FRAMES_DIR, RESULTS_DIR, OUTPUT_FILE, RANGE, GAUSSIANS, SIFT_MODE, NUM_THREADS):
	pool = Pool(NUM_THREADS)
	args = []
	for subsample in RANGE:
		args.append((VIDEOSEARCH_DIR, OUTPUT_DIR, JOINT_INDEX_NAME % subsample, DB_DIR, QUERY_DIR, SHOT_FRAMES_DIR, RESULTS_DIR, OUTPUT_FILE % subsample, subsample, GAUSSIANS, SIFT_MODE))
	pool.map(retrieveWrapperFeatureAggregation, args)
	
def retrieveWrapperFeatureAggregation(args):
	retrieveFeatureAggregation(*args)
		
def retrieveFeatureAggregation(VIDEOSEARCH_DIR, OUTPUT_DIR, JOINT_INDEX_NAME, DB_DIR, QUERY_DIR, SHOT_FRAMES_DIR, RESULTS_DIR, OUTPUT_FILE, numFilesInSequence, GAUSSIANS, SIFT_MODE):
	QUERY_LIST_FILE = 'query_list.txt'
	DB_LIST_FILE = 'db_list.txt'

	# Path where to find GDIndex's trained parameters
	GDINDEX_PATH='%s/indexer/global_descriptors/trained_parameters' % VIDEOSEARCH_DIR
	# Number of results to output
	NUMBER_OUTPUT_RESULTS=999999
	# Flag that if set avoids outputting redundant scene results
	AVOID_REDUNDANT_RESULTS=1
	# Verbose level
	VERBOSE=1
	# Number of min words to consider a match (default: 0)
	MIN_NUM_WORDS_SELECTED=0
	# Word selection mode: (0=L1 norm), (1=soft assgn)
	WORD_SELECTION_MODE=0
	# Word selection thresh
	WORD_SELECTION_THRESH=10
	# Shot parameters
	SHOT_MODE=1
	SHOT_FIRST_FRAMES = os.path.join(OUTPUT_DIR, SHOT_FRAMES_DIR, 'shot_%d.txt' % numFilesInSequence)
	# Power normalization for score denominator
	SCORE_DEN_POWER_NORM = 0.5

	options = ''
	options += ' -c %d' % GAUSSIANS
	options += ' -f %d' % SIFT_MODE
	options += ' --gdindex_parameters_path %s' % GDINDEX_PATH
	options += ' --number_output_results %d' % NUMBER_OUTPUT_RESULTS
	options += ' -v %d' % VERBOSE
	options += ' --min_number_words_visited %d' % MIN_NUM_WORDS_SELECTED
	options += ' --word_selection_mode %d' % WORD_SELECTION_MODE
	options += ' --word_selection_thresh %d' % WORD_SELECTION_THRESH
	options += ' --shot_mode %d' % SHOT_MODE
	options += ' --shot_list %s' % SHOT_FIRST_FRAMES
	options += ' --score_den_power_norm %f' % SCORE_DEN_POWER_NORM

	if AVOID_REDUNDANT_RESULTS == 1:
		options += ' --avoid_redundant_scene_results '

	# Composing output path
	outputPath = os.path.join(OUTPUT_DIR, RESULTS_DIR)
	outputBase = os.path.join(outputPath, OUTPUT_FILE)

	queries = []
	for root, subdirs, files in os.walk(QUERY_DIR):
		for file in files:
			if file.endswith('.jpg'):
				queries.append(os.path.join(root, file))
	queries = sorted(queries)
	queryListFilePath = os.path.join(OUTPUT_DIR, QUERY_LIST_FILE)
	if not os.path.exists(queryListFilePath):
	        with open(queryListFilePath, 'w') as f:
			for queryPath in queries:
	                        f.write('%s\n' % queryPath)

	dbListFilePath = os.path.join(OUTPUT_DIR, DB_LIST_FILE)
	if not os.path.exists(dbListFilePath):
		dbFiles = []
		for root, subdirs, files in os.walk(DB_DIR):
			for file in sorted(files):
				if file.endswith('.jpg'):
					dbFiles.append(os.path.join(root, file))
		dbFiles = sorted(dbFiles)
	        with open(dbListFilePath, 'w') as f:
			for dbFile in dbFiles:
	                        f.write('%s\n' % dbFile)

	indexFile = os.path.join(OUTPUT_DIR, JOINT_INDEX_NAME)

	# Create output folder if necessary
	if not os.path.exists(outputPath):
		try:
			os.makedirs(outputPath)
		except:
			pass

	# Compose command line
	cmd = '%s/retriever/retrieve_on_dataset -i %s -d %s -q %s -o %s %s' % \
		(VIDEOSEARCH_DIR, indexFile, dbListFilePath, queryListFilePath, outputBase, options)
	print cmd
	subprocess.call(cmd.split())
	
	# Post-process results
	resFilePath = os.path.join(outputPath, '%s_results.txt' % OUTPUT_FILE)
	resultsRaw = [line.rstrip('\n') for line in open(resFilePath)]
	results = []
	lineIdx = 0
	resIdx = -1
	for line in resultsRaw:
		if line.startswith('Query'):
			results.append([])
			lineIdx = 0
			resIdx += 1
		else:
			results[resIdx].append(line)
			lineIdx += 1
	# Convert to ranked list of models
	rankedLists = []
	for res in results:
		rankedList = []
		for line in res:
			model = line.split('/')[-2]
			if model not in rankedList:
				rankedList.append(model)
		rankedLists.append(rankedList)
	numQueries = 0
	correct = 0
	modelRanks = []
	for rankedList in rankedLists:
		# Check if model ID (found in path) is matching
		queryModel = queries[numQueries].split('/')[-2]
		if queryModel == rankedList[0]:
			correct += 1
		try:
			rank = rankedList.index(queryModel)
		except ValueError:
			rank = float('inf')
		modelRanks.append(rank)
		numQueries += 1
	print correct, numQueries
	mAP = sum([1.0/(rank+1) for rank in modelRanks]) * 1.0 / len(modelRanks)

	with open(os.path.join(outputPath, '%s_processed.txt' % OUTPUT_FILE), 'w') as outputFile:
		print>>outputFile, 'correct\n%d\ntotal\n%d' % (correct, numQueries)
		print>>outputFile, 'mAP\n%f' % mAP
		
def postProcess(OUTPUT_DIR, RESULTS_DIR, OUTPUT_RES, OUTPUT_FILE, RANGE):
	resultsData = {}
	for subsample in RANGE:
		resFilePath = os.path.join(OUTPUT_DIR, RESULTS_DIR, '%s_processed.txt' % (OUTPUT_FILE % subsample))
		with open(resFilePath, 'r') as resFile:
			resFile.readline()
			nRet = resFile.readline().rstrip('\n')
			resFile.readline()
			nTot = resFile.readline().rstrip('\n')
			resFile.readline()
			mAP = resFile.readline().rstrip('\n')
		if not nRet.isdigit() or not nTot.isdigit():
			print nRet, nTot
			raise Exception('Error in results file')
		resultsData[subsample] = (float(nRet)/float(nTot), float(mAP))
	with open(os.path.join(OUTPUT_DIR, RESULTS_DIR, OUTPUT_RES), 'w') as outputFile:
		for s in sorted(resultsData):
			outputFile.write('%d,%f,%f\n' % (s, resultsData[s][0], resultsData[s][1]));
