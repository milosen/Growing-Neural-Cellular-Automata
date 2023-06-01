from setuptools import setup, find_packages

setup(
    name='nca',
    version='1.0.0',
    url='https://github.com/Growing-Neural-Cellular-Automata.git',
    author='Nikola Milosevic',
    author_email='milose.nik@gmail.com',
    description='Description of my package',
    packages=find_packages(),
    install_requires=[
        'matplotlib >= 1.5.1',
        'torch >= 2.0.0',
        'jupyter',
        'tqdm',
        'rich',
        'pygame',
        'imageio'
    ],
)
