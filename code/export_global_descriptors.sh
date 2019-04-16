OUTPUT_DIR="$(python -c 'import config;print(config.OUTPUT_DIR)')"

./export_global_descriptors/export_global_descriptors \
    -i $OUTPUT_DIR/output_frame_descriptors/joint_index_frames.sift_scfv_idx \
    -o $OUTPUT_DIR/output_frame_descriptors/global_descriptors.txt
