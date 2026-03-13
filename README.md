# VisionKit

A set of CLI tools for video frame extraction, deblurring, image deduplication, and similar-image search. Each module runs independently with isolated parameters.

## Install

```bash
pip install -r requirements.txt
```

Notes:
- This project uses `pyiqa` and `torch`, which currently require `numpy<2`. The `requirements.txt` pins `numpy<2` to avoid the NumPy 2.x compatibility error.

## Usage

View global help:

```bash
python main.py -h
```

View subcommand help:

```bash
python main.py video2image -h
python main.py deblur -h
python main.py deduplicate -h
python main.py search-duplicate -h
```

## Commands

### 1) Video to Image

```bash
python main.py video2image \
  -i /path/to/video_folder \
  -o /path/to/output_folder \
  -p img \
  -n 30
```

Parameters:
- `-i, --input`: video folder path (required)
- `-o, --output`: output image folder path (required)
- `-p, --prefix`: output filename prefix (default `img`)
- `-n, --interval`: frame extraction interval (default `30`)

### 2) Deblur

```bash
python main.py deblur \
  -i /path/to/images \
  -lt 100 \
  -nt 5
```

Parameters:
- `-i, --input`: image folder path (required)
- `-lt, --laplacian-threshold`: Laplacian threshold (default `100.0`)
- `-nt, --niqe-threshold`: NIQE threshold (default `5.0`)

### 3) Deduplicate

```bash
python main.py deduplicate \
  -m CNN \
  -i /path/to/images \
  -st 0.9
```

Parameters:
- `-m, --method`: `CNN` or `PHash` (required)
- `-i, --input`: image folder path (required)
- `-st, --similarity-threshold`: similarity threshold (default `0.90`)

### 4) Search Duplicate

```bash
python main.py search-duplicate \
  -m cosine \
  -op /path/to/original \
  -tp /path/to/target \
  -o /path/to/output \
  -st 0.9
```

Parameters:
- `-m, --method`: `cosine` or `hamming` (required)
- `-op, --original-path`: original image folder path (required)
- `-tp, --target-path`: target image folder path (required)
- `-o, --output`: output folder path for matched images (required)
- `-st, --similarity-threshold`: similarity threshold (default `0.90`)
