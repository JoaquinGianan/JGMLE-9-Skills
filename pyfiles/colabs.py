# Mount the drive to ensure access to where you store the images on Google Drive. 

from google.colab import drive
drive.mount('/content/drive')


# Clone the tensorflow models repository if it doesn't already exist

import pathlib


if "models" in pathlib.Path.cwd().parts:
    while "models" in pathlib.Path.cwd().parts:
        os.chdir('..')
elif not pathlib.Path('models').exists():
    !git clone --depth 1 https://github.com/tensorflow/models


# Install dependencies of the pre-trained models and the TF Object Detection API. This may take a few minutes.

%%bash
sudo apt install -y protobuf-compiler
cd models/research/
protoc object_detection/protos/*.proto --python_out=.
cp object_detection/packages/tf2/setup.py .
python -m pip install -q -U .    