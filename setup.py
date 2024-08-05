from setuptools import setup, find_packages
setup(
    name='nexusnlp',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fasttext',
        'spacy'
    ],
)
