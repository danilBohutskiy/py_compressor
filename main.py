from compressor.FileCompressor import FileCompressor
from components.FileHelper import FileHelper
from components.ColoramaHelper import ColoramaHelper

def main():
    src_directory = FileHelper.ask_directory()
    directories = FileHelper.get_list_directories(src_directory)
    file_compressor = FileCompressor()
    colorama_helper = ColoramaHelper()

    for directory in directories:
        colorama_helper.print_current_dir(directory)
        process_directory(directory, file_compressor, colorama_helper)

def process_directory(directory, file_compressor, colorama_helper):
    file_list = FileHelper.get_file_list(directory)
    dir_original_size = FileHelper.get_dir_size(directory)

    for path_to_file in file_list:
        filename = FileHelper.get_filename_from_path(path_to_file)
        colorama_helper.print_current_file(filename)

        compressor_instance = file_compressor.create(path_to_file)
        if compressor_instance is None:
            continue

        compressor_instance.compress(path_to_file)
    dir_compressed_size = FileHelper.get_dir_size(directory)
    colorama_helper.print_comparison_directories_size(directory, dir_original_size, dir_compressed_size)

if __name__ == "__main__":
    main()
