import setuptools

core_requirements = [ 
    'numpy==1.23.2',
    'regex==2022.9.13',
    'tqdm==4.64.1',
    'joblib==1.1.0',
    'nltk==3.7',
]

setuptools.setup(
    name='nandini',
    description="A Scratch Module for Machine learning",
    url="",
    author='Sanjaypranav',
    author_email='sanjaypriya195@gmail.com',
    version='0.0.1',
    install_requires=core_requirements,
    python_requires='>=3.7,<3.10',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    )
