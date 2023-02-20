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

git clone git@github.com:danilBohutskiy/py_compressor.git
cd py_compressor/

pip install -r requirements.txt
```

## Usage
After installing, you need to:
1. Configure settings.json.
2. Run main.py file. It will generate INPUTDIR and OUTPUTDIR directories.
```sh
python3 main.py
```
3. Add your media folders to INPUTDIR
4. Run main.py file.

## License

MIT
