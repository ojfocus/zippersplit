# README.md

# ZipperSplit

**ZipperSplit** is a Python script that compresses the contents of a folder (including all subdirectories) into multiple zip files, each smaller than a specified size (default: 10GB). This is useful for backing up or transferring large directories in manageable chunks.

## Features

- Recursively includes all files and subdirectories
- Preserves directory structure inside each zip
- Splits files into batches so that no zip exceeds the size limit
- Skips files larger than the specified maximum size
- Simple and cross-platform (works on Windows, Linux, macOS)

## Requirements

- Python 3.6 or newer (tested on Python 3.9+)

## Usage

1. **Clone or download this repository.**

2. **Edit `zippersplit.py`:**
   - Set `SOURCE_DIR` to the folder you want to compress.
   - Set `OUTPUT_DIR` to the folder where you want the zip files to be saved.
   - (Optional) Adjust `MAX_ZIP_SIZE` if you want a different size limit (in bytes).

   Example:
   ```python
   SOURCE_DIR = '/home/user/myfolder'
   OUTPUT_DIR = '/home/user/zipped'
   MAX_ZIP_SIZE = 10 * 1024 * 1024 * 1024  # 10GB
   ```

3. **Run the script:**
   ```bash
   python zippersplit.py
   ```

4. **Find your split zip files in the output directory.**

## Example Output

```
Creating /home/user/zipped/archive_part1.zip with 1200 files...
Creating /home/user/zipped/archive_part2.zip with 950 files...
Done.
```

## Notes

- Files larger than the specified maximum size are skipped (with a warning).
- Directory structure is preserved inside each zip file.
- No file is split between zips.

## License

This project is licensed under the MIT License.

---

**Contributions and