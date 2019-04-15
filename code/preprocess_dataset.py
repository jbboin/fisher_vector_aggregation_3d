import extract_sift, extract_global, retrieval, config
import os, shutil, argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Evaluate dataset')
    parser.add_argument(
        '--sift_mode', # mode = 0 -> SIFT detector; 1 -> Hessian affine detector
        type=int,
        required=False,
        default=1
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
    db_dir = os.path.join(config.DATASET_DIR, 'model_frames')
    query_dir = os.path.join(config.DATASET_DIR, 'queries')
    extract_sift.extract(config.VIDEOSEARCH_DIR, db_dir, args.sift_mode, args.num_threads)
    extract_sift.extract(config.VIDEOSEARCH_DIR, query_dir, args.sift_mode, args.num_threads)
    extract_global.generateFrameLists(config.DATASET_DIR)

if __name__ == '__main__':
    main(parse_arguments())


