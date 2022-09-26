
<div>
<a><img href='https://github.com/Sanjaypranav/Scratch-modules' src="https://img.shields.io/badge/nandini-github-green?style=flat&logo=github" alt="nandini" /></a>
<a href = 'https://pypi.org/project/nandini/'><img src="https://img.shields.io/badge/nandini-PyPi-blue?style=flat&logo=python" alt="nandini" /></a>
<a href = 'https://hub.docker.com/repository/docker/sanjaypranav/nandini-0.0.3'><img src="https://img.shields.io/badge/nandini-container-red?style=flat&logo=docker" alt="nandini" /></a>
</div>

# Introduction to Nandini
<p style= 'font-size:12px'> Note : only supported for Python 3.7 to Python 3.9 </p>

Nandini is a NLP based Python Package devoloped by Puretalk AI employee and Nandini from the name of the employee who devoloped this package. Nandini comprises of various NLP based functions and modules which can be used to perform various NLP tasks.


# <div align="center">Installation <img width = 30px height = 30px src ='https://imgs.search.brave.com/boLkeEITNBddmKoVc4Q41tEheu7XTCx4mB79Rj0x3Pc/rs:fit:300:300:1/g:ce/aHR0cHM6Ly93d3cu/Y2VydHNhbi5jb20u/YnIvd3AtY29udGVu/dC91cGxvYWRzLzIw/MjAvMDQvaW5zdGFs/bGF0aW9uLWljb24t/cG5nLTctMzAweDMw/MC5wbmc' style="vertical-align:middle" ></div>
---

### Quick Installation

here is the [PyPi link](https://pypi.org/project/nandini/0.0.3/) for the package

or you can install it using pip

    $ pip install nandini

or by cloning the repository

```bash
$ git clone https://github.com/Sanjaypranav/Scratch-modules.git
$ cd Scratch-modules
$ export PYTHONPATH=./src
$ python3 setup.py sdist bdist_wheel
$ python3 setup.py install
```
### Docker Installation <img width = 35px height = 35px src ='https://imgs.search.brave.com/8zyG1tMW7_Nnark19_kPdUHXVXERQWozcd00Vr57tgY/rs:fit:900:900:1/g:ce/aHR0cHM6Ly95dDMu/Z2dwaHQuY29tLy00/RGlURzB2dEVXMC9B/QUFBQUFBQUFBSS9B/QUFBQUFBQUFBQS83/M2tnX0NOSzU0Zy9z/OTAwLWMtay1uby1t/by1yai1jMHhmZmZm/ZmYvcGhvdG8uanBn' style="vertical-align:middle" >

```bash
$ docker pull sanjaypranav/nandini-0.0.3:latest
```

# <div align="center">Documentation <img width = 35px height = 35px src ='https://imgs.search.brave.com/1wNAywm_gk_2MYx946TR_cgqHDlKf07jV6E3sYYJnO4/rs:fit:1024:1024:1/g:ce/aHR0cHM6Ly93d3cu/aWNvbmJ1bm55LmNv/bS9pY29ucy9tZWRp/YS9jYXRhbG9nL3By/b2R1Y3QvNC8wLzQw/MzkuMTItZG9jdW1l/bnRzLWFuZC1wZW4t/aWNvbi1pY29uYnVu/bnkuanBn' style="vertical-align:top" ></div>
---------

### Getting Started 
We are planned to provide Natural Language Processing  tasks like Preprocessing, Vectorizer, Text Summarizing, Translation ...etc, as a Python package.

```python
from nandini import *
```


<!-- for writing packages refer [link](https://towardsdatascience.com/how-to-publish-a-python-package-to-pypi-7be9dd5d6dcd)

for writing readme refer [link](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)
for writing docker 
1) dockerfile
2) build the dockerfile with image name 
3) check the container list, commit and push the container to the docker hub -->

##### <p>Connect us with <img width = 20px height = 20px src = 'https://imgs.search.brave.com/Q224hx_R_P1Wb4F_xf46NGKcChadDLGanxijTRzFRSk/rs:fit:512:512:1/g:ce/aHR0cHM6Ly9jZG4z/Lmljb25maW5kZXIu/Y29tL2RhdGEvaWNv/bnMvc29jaWFsLTcv/NTAwL0Nvbm5lY3Rf/Y29ubmVjdGlvbl9k/YXRhX2dsb2JhbF9s/aW5rX25ldHdvcmst/NTEyLnBuZw' style="vertical-align:top" > </p>


[<img align="left" alt="Puretalk | LinkedIn" width="30px" src="https://img.icons8.com/color/48/000000/linkedin.png" />][linkedin][<img align="left" alt="Puretalk | Twitter" width="30px" src="https://img.icons8.com/fluent/48/000000/twitter.png" />][twitter][<img align ="left" alt="Sanjaypranav" width="30px" src="https://img.icons8.com/color/48/000000/gmail.png" />][gmail]


[linkedin]: https://www.linkedin.com/in/Nandini-s-175655176
[twitter]: https://twitter.com/Nandhin96093533 
[gmail]: mailto:Nandinivadalur@gmail.com

<!-- for Author use -->
test-pypi

    python3 -m twine upload --repository testpypi dist/*

pypi

    python3 -m twine upload dist/*


