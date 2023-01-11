import os

from Compressor import Compressor

def run():
    
    print('Start...')

    model = Compressor(os.getcwd())
    os.chdir('./' + model.inputdir)

    for directory in os.listdir():
        os.chdir('./' + directory)
        print('Current directory: ' + directory)

        model.clearOutputDir(directory)

        for index, filename in enumerate(os.listdir()):
            pathToFile = model.getPathToSrcFile(filename)
            pathToOutput = model.getPathToOutputDirectory(directory)

            compressor = model.getCompressor(pathToFile)

            if compressor == None:
                continue

            compressor.compress(pathToFile, pathToOutput, filename)

        os.chdir('..')
    
    print('Done!')

run()
