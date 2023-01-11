import mimetypes, os
import subprocess

class VideoCompressor:
    
    def compress(self, path_to_file, path_to_output, filename):
        filename_ext = os.path.splitext(filename)
        filename_new = filename_ext[0] + '.mp4'
        file_path = os.path.join(path_to_output, filename_new)
        
        result = subprocess.run('ffmpeg -i '+path_to_file+' -vcodec libx265 -crf 28 '+file_path)
        print(result)
        