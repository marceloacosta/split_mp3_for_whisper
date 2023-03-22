# MP3 Splitter

This Python script splits an MP3 file into smaller files with a maximum specified size. It uses the `pydub` library and requires FFmpeg to be installed on your system.

## Requirements

- Python 3.6 or higher
- pydub
- FFmpeg

## Installation

1. Install `pydub` using `pip`:

pip install pydub


2. Install FFmpeg on your system.

- For macOS users, you can use Homebrew to install FFmpeg:

  ```
  brew install ffmpeg
  ```

- For Windows users, visit https://www.ffmpeg.org/download.html and download the appropriate package for your system. Make sure to add the FFmpeg `bin` folder to your system's `PATH`.

- For Linux users, you can use the package manager for your distribution to install FFmpeg. For example, on Ubuntu, you can run:

  ```
  sudo apt-get update
  sudo apt-get install ffmpeg
  ```

## Usage

To run the script, execute the following command in your terminal or command prompt:


python split_mp3.py <input_file> <output_prefix> [max_size_mb]


Replace `<input_file>` with the name of the input MP3 file, `<output_prefix>` with the desired prefix for the output files, and `[max_size_mb]` with the maximum size in MB for each output file (optional).

Example:

```bash
python split_mp3.py input.mp3 output 25

This command will split the input.mp3 file into smaller files with a maximum size of 25 MB, and the output files will have the prefix output.
```

## License
This project is released under the MIT License. See the LICENSE file for more information.