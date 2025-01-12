# Other modules
import os
import subprocess
import imageio_ffmpeg

# Local modules
from audio_extract import utils

FFMPEG_BINARY = imageio_ffmpeg.get_ffmpeg_exe()


def create_output_folder(filepath: str):
    folder_path = "\\".join(filepath.split('\\')[:-1])

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def extract_full_audio(path: str, output: str, start_time: str):
    # Create output directory if it doesn't exist
    create_output_folder(output)

    result = subprocess.run(
        [FFMPEG_BINARY,
         '-i', path,
         '-ss', start_time,
         '-f', 'mp3',
         '-ab', '192k',
         '-ar', '44100',
         '-ac', '2',
         '-vn',
         '-y', output], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        utils.print_success(f"Success : audio file has been saved to \"{output}\".")
    else:
        error = result.stderr.decode().strip().split("\n")[-1]
        utils.print_error(f"Failed : {error}.")


def extract_sub_audio(path: str, output: str, start_time: str, duration: str):
    # Create output directory if it doesn't exist
    create_output_folder(output)

    result = subprocess.run(
        [FFMPEG_BINARY,
         '-i', path,
         '-ss', start_time,
         '-t', duration,
         '-f', 'mp3',
         '-ab', '192k',
         '-ar', '44100',
         '-ac', '2',
         '-vn',
         '-y', output], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        utils.print_success(f"Success : audio file has been saved to \"{output}\".")
    else:
        error = result.stderr.decode().strip().split("\n")[-1]
        utils.print_error(f"Failed : {error}.")
