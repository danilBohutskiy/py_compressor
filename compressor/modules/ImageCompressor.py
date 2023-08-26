import PIL
from components.FileHelper import FileHelper
from PIL import Image

class ImageCompressor:

    FORMAT_JPG = '.jpg'

    def compress(self, path_to_file):
        img = self.get_image(path_to_file)
        path_new = FileHelper.rename_filename_with_format(path_to_file, self.FORMAT_JPG)
        img.save(path_new)
        if (path_new != path_to_file):
            FileHelper.delete_file(path_to_file)

    def get_image(self, filename):
        img = PIL.Image.open(filename)
        myHeight, myWidth = img.size
        img = img.convert('RGB')
        img.resize((myHeight, myWidth), Image.Resampling.LANCZOS)
        return img

