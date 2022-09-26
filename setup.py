import setuptools
# from nandini import __version__

core_requirements = [ 
    'numpy~=1.23.2',
    'regex',
    'tqdm~=4.64.1',
    'joblib~=1.1.0',
    'nltk~=3.7',
    'progressbar~=2.5',
    'scipy~=1.9.1',
    'gensim~=4.2.0'
]

setuptools.setup(
    name='nandini',
    description="A Scratch Module for Machine learning",
    url="",
    author='Sanjaypranav',
    author_email='sanjaypriya195@gmail.com',
    version= '0.0.5',
    install_requires=core_requirements,
    python_requires='>=3.7,<=3.10.6',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['nandini'],
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    )
