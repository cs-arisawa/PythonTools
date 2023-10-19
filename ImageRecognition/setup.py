from setuptools import setup, find_packages

setup(
    name='ImageRecognition',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'tkinterdnd2',
        'opencv-python'
    ],
)