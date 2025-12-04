from huggingface_hub import hf_hub_download
import os

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

repo_id = "pixparse/cc3m-wds"
local_dir = "/data2/xinc/DIVA/datasets/cc3m"

# 指定多个文件（可按需修改范围）
file_list = [f"cc3m-validation-{i:04d}.tar" for i in range(1, 16)]

for fname in file_list:
    print(f"⬇️ 正在下载: {fname}")
    try:
        hf_hub_download(
            repo_id=repo_id,
            filename=fname,
            repo_type="dataset",
            local_dir=local_dir,
            resume_download=True,
            local_dir_use_symlinks=False
        )
        print(f"✅ 完成: {fname}\n")
    except Exception as e:
        print(f"❌ 失败: {fname} ({e})\n")
