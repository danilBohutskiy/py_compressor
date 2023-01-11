import os, PIL
from PIL import Image

class ImageCompressor:

    def compress(self, path_to_file, path_to_output, filename):
        name, extension = os.path.splitext(filename)
        
        filepath = os.path.join(path_to_output, (name + '.jpg'))

        img = self.getImage(path_to_file)   
        img.save(filepath)

    def getImage(self, filename):
        img = PIL.Image.open(filename)
        
        myHeight, myWidth = img.size
        img = img.convert('RGB')
        img.resize((myHeight, myWidth), Image.Resampling.LANCZOS)
        
        return img

