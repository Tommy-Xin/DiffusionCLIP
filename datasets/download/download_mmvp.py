from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="MMVP/MMVP_VLM",
    repo_type="dataset",
    local_dir="./MMVP_VLM",
    endpoint="https://hf-mirror.com"
)
