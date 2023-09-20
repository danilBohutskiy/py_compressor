# py_compressor
## Simple Python 3 media compressor

## Features
- Compress image files by [Pillow](https://pypi.org/project/Pillow/)
- Compress & optimize .gif files by [pygifsicle](https://pypi.org/project/pygifsicle/)
- Compress & optimize video files by [ffmpeg](https://ffmpeg.org/)

## Installation (Linux)

```sh
sudo apt update && sudo apt upgrade
sudo apt install -y gifsicle
sudo apt install -y ffmpeg
sudo apt install -y python3-tk

git clone git@github.com:danilBohutskiy/py_compressor.git py_compressor
cd py_compressor/

pip install -r requirements.txt
pip install hurry.filesize
```

## Usage
After installing, you need to:
1. Configure settings.json.
2. Run main.py file. It will generate INPUTDIR and OUTPUTDIR directories.
```sh
python3 main.py
```
3. Choose your folder
4. Start.

## License

MIT
