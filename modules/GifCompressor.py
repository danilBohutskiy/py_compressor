import os

from pygifsicle import *

class GifCompressor:

    def compress(self, path_to_file, path_to_output, filename):
        filename_ext = os.path.splitext(filename)
        filename_new = filename_ext[0] + '.gif'
        file_path = os.path.join(path_to_output, filename_new)
        
        gifsicle(
            sources=path_to_file,
            destination=file_path,
            optimize=True,
            colors=256,
            options=["--verbose"]
        )