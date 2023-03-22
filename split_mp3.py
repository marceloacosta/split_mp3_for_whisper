import sys
import os
from pydub import AudioSegment

def split_mp3(input_file, output_prefix, max_size_mb=25):
    # Load the input MP3 file
    audio = AudioSegment.from_mp3(input_file)

    # Calculate the target duration in milliseconds
    max_size_bytes = max_size_mb * 1024 * 1024
    target_duration_ms = (max_size_bytes / len(audio)) * audio.duration_seconds * 1000
    total_parts = int(audio.duration_seconds * 1000 / target_duration_ms) + 1

    # Split the audio file into parts
    for i in range(total_parts):
        start = i * target_duration_ms
        end = (i + 1) * target_duration_ms if (i + 1) * target_duration_ms < len(audio) else len(audio)

        part = audio[start:end]
        output_file = f"{output_prefix}_part{i + 1}.mp3"

        # Export the part to a new MP3 file
        part.export(output_file, format="mp3")
        print(f"Successfully saved part {i + 1} as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python split_mp3.py <input_file> <output_prefix> [max_size_mb]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_prefix = sys.argv[2]
    max_size_mb = float(sys.argv[3]) if len(sys.argv) > 3 else 25

    split_mp3(input_file, output_prefix, max_size_mb)
