import os, pathlib, shutil, PIL
from PIL import Image

WORKDIR = os.getcwd()
INPUTDIR = 'src'
OUTPUTDIR = 'output'

def getImagePil(filename):
    img = PIL.Image.open(filename)
    
    myHeight, myWidth = img.size
    img.resize((myHeight, myWidth), Image.Resampling.LANCZOS)
    
    return img

def refreshDirectory(path):
    dirpath = os.path.join((WORKDIR + '\\' + OUTPUTDIR), path)
    if os.path.isdir(dirpath):
        os.chmod(dirpath, 0o0777)
        shutil.rmtree(dirpath)
    else:
        os.mkdir(dirpath)

def saveToDirectory(img, index, filename, path):
    dirpath = os.path.join((WORKDIR + '\\' + OUTPUTDIR), path)

    file_extension = pathlib.Path(filename).suffix
    new_filename = str(index) + file_extension
    img.save(os.path.join(dirpath, new_filename))

    print('File \"' + filename + '\" saved as \"' + new_filename + '\"')

def initDirectories():
    outputpath = os.path.join(WORKDIR, INPUTDIR)
    if os.path.isdir(outputpath):
        os.chmod(outputpath, 0o0777)
    else:
        os.mkdir(outputpath)
    inputpath = os.path.join(WORKDIR, OUTPUTDIR)
    if os.path.isdir(inputpath):
        os.chmod(inputpath, 0o0777)
    else:
        os.mkdir(inputpath)

def run():
    print('Start...')
    initDirectories()
    os.chdir('./' + INPUTDIR)

    for directory in os.listdir():
        os.chdir('./' + directory)
        print('Current directory: ' + os.getcwd())
        refreshDirectory(directory)
        for index, filename in enumerate(os.listdir()):
            img = getImagePil(filename)
            saveToDirectory(img, (index + 1), filename, directory)
        os.chdir('..')
    
    print('Done!')

run()
