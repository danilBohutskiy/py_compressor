from pygifsicle import *

class GifCompressor:

    def compress(self, path_to_file):
        gifsicle(
            sources=path_to_file,
            destination=path_to_file,
            optimize=True,
            colors=256,
            options=["--verbose"]
        )