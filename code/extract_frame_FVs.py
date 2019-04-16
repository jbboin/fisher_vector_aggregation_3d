import extract_global, config
import os, argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Extract frame FVs')
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
    joint_index_name = 'joint_index_frames.sift_scfv_idx'

    output_dir = os.path.join(config.OUTPUT_DIR, 'output_frame_descriptors')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    extract_global.generateGlobalFeatureFrame(config.VIDEOSEARCH_DIR, output_dir, config.DATASET_DIR, joint_index_name, args.gaussians, args.sift_mode, args.num_threads)

if __name__ == '__main__':
    main(parse_arguments())
