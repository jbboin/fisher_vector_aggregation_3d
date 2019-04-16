import extract_global, retrieval, config
import os, argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Evaluate dataset')
    parser.add_argument(
        '--output_dir',
        type=str,
        required=True
    )
    parser.add_argument(
        '--custom_shot_dir',
        type=str,
        required=True
    )
    parser.add_argument(
        '--extract_global',
        dest='extract_global',
        action='store_true'
    )
    parser.add_argument(
        '--run_retriever',
        dest='run_retriever',
        action='store_true'
    )
    parser.add_argument(
        '--merge_results',
        dest='merge_results',
        action='store_true'
    )
    parser.add_argument(
        '--cluster_range',
        type=int,
        required=False,
        nargs='*',
        default=[]
    )
    parser.add_argument(
        '--sift_mode', # mode = 0 -> SIFT detector; 1 -> Hessian affine detector
        type=int,
        required=False,
        default=1
    )
    parser.add_argument(
        '--gaussians',
        type=int,
        required=False,
        default=128
    )
    parser.add_argument(
        '--num_threads',
        type=int,
        required=False,
        default=8
    )
    args = parser.parse_args()
    return args


def main(args):
    videosearch_dir = '../videosearch'
    shot_frames_dir = 'shot_list_frames'
    results_dir = 'results'
    joint_index_name = 'joint_index_%d.sift_scfv_idx'
    output_file = 'out_%d'
    output_res = 'out_results.txt'
    db_dir = os.path.join(config.DATASET_DIR, 'model_frames')
    query_dir = os.path.join(config.DATASET_DIR, 'queries')

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    if args.extract_global:
        for numFilesInSeq in args.cluster_range:
            extract_global.generateCustomShotLists(args.output_dir, db_dir, shot_frames_dir, numFilesInSeq)
            extract_global.generateGlobalFeatureAggregation(videosearch_dir, args.output_dir, config.DATASET_DIR, args.custom_shot_dir, numFilesInSeq, joint_index_name % numFilesInSeq, args.gaussians, args.sift_mode, args.num_threads)

    if args.run_retriever:
        retrieval.retrieveParallelFeatureAggregation(videosearch_dir, args.output_dir, joint_index_name, db_dir, query_dir, shot_frames_dir, results_dir, output_file, args.cluster_range, args.gaussians, args.sift_mode, args.num_threads)

    if args.merge_results:
        retrieval.postProcess(args.output_dir, results_dir, output_res, output_file, args.cluster_range)


if __name__ == '__main__':
    main(parse_arguments())

