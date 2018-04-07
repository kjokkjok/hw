# Trimming.py

## This tool allows do sequences trimming

### The following options are required:

`-h, --help            show this help message and exit`

`-in<> , --input_file  path to file in fastq format`

`-out<> , --output_file path to file for output`

`-slide_window int, --integer1 size of window`

`-right_end int, --integer2 int length to crop at right end`

`-left_end int, --integer3 int length to crop at left end`

`-quality_threshold int, --integer4 int quality to crop`

### Usage:

`$python trimming.py [-h] [-in str] [-out str] [-slide_window int] [-right_end int] [-left_end int] [-quality_threshold int]`

