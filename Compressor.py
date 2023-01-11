import os, shutil, mimetypes, json, PIL
from PIL import Image

from modules.GifCompressor   import GifCompressor
from modules.VideoCompressor import VideoCompressor
from modules.ImageCompressor import ImageCompressor

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

    def compress(self, path_to_file, path_to_output, filename, object):
        object.compress(path_to_file, path_to_output, filename)
        pass

    def getPathToSrcFile(self, filename):
        return os.path.abspath(filename)

    def getPathToOutputDirectory(self, directory):
        return os.path.join(self.workdir, self.outputdir, directory)

    def getCompressor(self, filename):
        item = mimetypes.guess_type(filename)[0]

        if item.startswith('video'):
            return VideoCompressor()
        elif item.endswith('gif'):
            return GifCompressor()
        elif item.startswith('image'):
            return ImageCompressor()
        return None