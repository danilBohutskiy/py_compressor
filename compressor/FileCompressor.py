import mimetypes

from compressor.modules.GifCompressor   import GifCompressor
from compressor.modules.VideoCompressor import VideoCompressor
from compressor.modules.ImageCompressor import ImageCompressor

class FileCompressor:
    MIMETYPE_VIDEO = 'video'
    MIMETYPE_GIF = 'gif'
    MIMETYPE_IMAGE = 'image'

    def compress(self, path_to_file, object):
        object.compress(path_to_file)

    def create(self, filename):
        filetype = mimetypes.guess_type(filename)[0]

        compressor = None

        if filetype == None:
            compressor = None
        elif filetype.startswith(self.MIMETYPE_VIDEO):
            compressor = VideoCompressor()
        elif filetype.endswith(self.MIMETYPE_GIF):
            compressor = GifCompressor()
        elif filetype.startswith(self.MIMETYPE_IMAGE):
            compressor = ImageCompressor()
            
        return compressor