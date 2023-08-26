import PIL
from PIL import Image

class ImageCompressor:

    def compress(self, path_to_file):
        img = self.getImage(path_to_file)   
        img.save(path_to_file)

    def getImage(self, filename):
        img = PIL.Image.open(filename)
        
        myHeight, myWidth = img.size
        img = img.convert('RGB')
        img.resize((myHeight, myWidth), Image.Resampling.LANCZOS)
        
        return img

