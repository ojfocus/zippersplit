import os
import zipfile

SOURCE_DIR = r'path\to\your\folder'  # Change this to your folder
OUTPUT_DIR = r'path\to\output\zips'  # Change this to your output folder
MAX_ZIP_SIZE = 10 * 1024 * 1024 * 1024  # 10GB

def collect_files(source_dir):
    files = []
    for root, _, filenames in os.walk(source_dir):
        for fname in filenames:
            fpath = os.path.join(root, fname)
            try:
                size = os.path.getsize(fpath)
                relpath = os.path.relpath(fpath, source_dir)
                files.append((fpath, relpath, size))
            except Exception as e:
                print(f"Skipping {fpath}: {e}")
    return files

def group_files(files, max_size):
    batches = []
    current_batch = []
    current_size = 0
    for fpath, relpath, size in files:
        if size > max_size:
            print(f"Warning: {relpath} is larger than {max_size} bytes and will be skipped.")
            continue
        if current_size + size > max_size and current_batch:
            batches.append(current_batch)
            current_batch = []
            current_size = 0
        current_batch.append((fpath, relpath))
        current_size += size
    if current_batch:
        batches.append(current_batch)
    return batches

def zip_batches(batches, source_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for idx, batch in enumerate(batches, 1):
        zip_name = os.path.join(output_dir, f'archive_part{idx}.zip')
        print(f"Creating {zip_name} with {len(batch)} files...")
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
            for fpath, relpath in batch:
                zf.write(fpath, arcname=relpath)

def main():
    files = collect_files(SOURCE_DIR)
    batches = group_files(files, MAX_ZIP_SIZE)
    zip_batches(batches, SOURCE_DIR, OUTPUT_DIR)
    print("Done.")

if __name__ == "__main__":
    main()