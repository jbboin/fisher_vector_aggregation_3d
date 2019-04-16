DATASET_DIR="$(python -c 'import config;print(config.DATASET_DIR)')"
OUTPUT_DIR="$(python -c 'import config;print(config.OUTPUT_DIR)')"

python retrieval_main.py \
    --output_dir $OUTPUT_DIR/output_512_gauss_rand \
    --custom_shot_dir $DATASET_DIR/aggreg_clusters/aggreg_clusters_rand \
    --gaussians 512 \
    --cluster_range 1 2 3 4 6 10 16 25 40 63 100 158 251 398 631 \
    --extract_global \
    --run_retriever \
    --merge_results
