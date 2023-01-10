import os, pathlib, shutil, json, PIL
from PIL import Image

class Compressor:

    workdir = None
    outputdir = None
    inputdir = None

    def __init__(self, WORKDIR):
        self.initVariables(WORKDIR)
        self.initDirectories()

    def initVariables(self, WORKDIR):
        file = open('settings.json')
        settings = json.load(file)
        
        self.outputdir = settings['OUTPUTDIR']
        self.inputdir = settings['INPUTDIR']
        self.workdir = WORKDIR
    
    def initDirectory(self, path):
            dirpath = os.path.join(self.workdir, path)
            if os.path.isdir(dirpath):
                os.chmod(dirpath, 0o0777)
            else:
                os.mkdir(dirpath)

    def initDirectories(self):
        self.initDirectory(self.inputdir)
        self.initDirectory(self.outputdir)
    
    def clearOutputDir(self, path):
        dirpath = os.path.join(self.workdir, self.outputdir, path)
        if os.path.isdir(dirpath):
            os.chmod(dirpath, 0o0777)
            shutil.rmtree(dirpath)
            os.mkdir(dirpath)
        else:
            os.mkdir(dirpath)
    
    def compressImage(self, filename):
        img = PIL.Image.open(filename)
        
        myHeight, myWidth = img.size
        img.resize((myHeight, myWidth), Image.Resampling.LANCZOS)
        
        return img

    def saveImgToDir(self, img, path, file_name, new_file_name = None):
        dirpath = os.path.join(self.workdir, self.outputdir, path)
        
        file_ext = pathlib.Path(file_name).suffix

        filename = None
        if new_file_name:
            filename = new_file_name + file_ext
        else:
            filename = file_name

        filepath = os.path.join(dirpath, filename)    
        img.save(filepath)
