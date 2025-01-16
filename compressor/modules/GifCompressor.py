import subprocess
from components.FileHelper import FileHelper

class GifCompressor:
    def compress(self, path_to_file):
        path_new = FileHelper.rename_filename_with_format(path_to_file, '.gif', True)
        cmd = (
            f'ffmpeg -nostats -loglevel 0 '
            f'-i "{path_to_file}" '
            f'-vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" '
            f'-loop 0 '
            f'-c:v gif '
            f'-preset slow '
            f'-crf 18 '
            f'-f gif '
            f'"{path_new}"'
        )
        subprocess.run(cmd, shell=True)
        FileHelper.delete_file(path_to_file)
        FileHelper.rename_path(path_new, path_to_file)