import os
from PIL import Image, ExifTags
from components.FileHelper import FileHelper

class ImageCompressor:
    FORMAT_JPEG = '.jpg'

    def compress(self, path_to_file):
        img = self.get_image(path_to_file)
        path_new = FileHelper.rename_filename_with_format(path_to_file, self.FORMAT_JPEG)
        
        img = self.remove_exif_data(img)

        img.save(path_new, 'JPEG', quality=85, optimize=True, progressive=True)
        
        if path_new != path_to_file:
            FileHelper.delete_file(path_to_file)

    def get_image(self, filename):
        img = Image.open(filename)
        myWidth, myHeight = img.size
        img = img.convert('RGB')
        img = img.resize((myWidth, myHeight), Image.Resampling.LANCZOS)
        return img

    def remove_exif_data(self, img):
        try:
            exif = img.info['exif']
            img = img.copy()
            del img.info['exif']
        except KeyError:
            pass
        return img