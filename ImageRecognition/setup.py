from setuptools import setup, find_packages

setup(
    name='ImageRecognition',
    version='0.1.0',
    install_requires=[
        'Pillow',
        'tkinterdnd2',
        'opencv-python'
    ],
    packages=find_packages(where='ImageRecognition'),
    package_dir={'': 'ImageRecognition'},
)