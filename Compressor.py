import os, shutil, mimetypes, json

from hurry.filesize import size

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

    def getPathToSrcFie(self, filename = ''):
        return os.path.abspath(filename)

    def getPathToOutputDirectory(self, directory):
        return os.path.join(self.workdir, self.outputdir, directory)

    def getCompressor(self, filename):
        filetype = mimetypes.guess_type(filename)[0]

        compressor = None

        if filetype == None:
            compressor = None
        elif filetype.startswith('video'):
            compressor = VideoCompressor()
        elif filetype.endswith('gif'):
            compressor = GifCompressor()
        elif filetype.startswith('image'):
            compressor = ImageCompressor()
            
        return compressor

    def getDirSize(self, path):
        total = 0
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
        return size(total)  