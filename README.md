# python_point_cloud

[![Build Status](https://travis-ci.org/tesseract-ocr/tesseract.svg?branch=master)](https://travis-ci.org/tesseract-ocr/tesseract)
[![Build status](https://ci.appveyor.com/api/projects/status/miah0ikfsf0j3819/branch/master?svg=true)](https://ci.appveyor.com/project/zdenop/tesseract/)
![Build status](https://github.com/tesseract-ocr/tesseract/workflows/sw/badge.svg)<br>
[![Coverity Scan Build Status](https://scan.coverity.com/projects/tesseract-ocr/badge.svg)](https://scan.coverity.com/projects/tesseract-ocr)
[![Code Quality: Cpp](https://img.shields.io/lgtm/grade/cpp/g/tesseract-ocr/tesseract.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tesseract-ocr/tesseract/context:cpp)
[![Total Alerts](https://img.shields.io/lgtm/alerts/g/tesseract-ocr/tesseract.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tesseract-ocr/tesseract/alerts)
[![OSS-Fuzz](https://img.shields.io/badge/oss--fuzz-fuzzing-brightgreen)](https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=-opened&can=2&q=proj:tesseract-ocr)
<br/>
[![GitHub license](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://raw.githubusercontent.com/tesseract-ocr/tesseract/master/LICENSE)
[![Downloads](https://img.shields.io/badge/download-all%20releases-brightgreen.svg)](https://github.com/tesseract-ocr/tesseract/releases/)

## Environment

Python 3


## Usage

Install the reference libs:

    pip install -r requirements.txt


## Run
You can have a look at the help for usage:

    python main.py -h


## About

This project is to generate the change result to a tsv file from source data.
There is the demo input and output data in this repo.

## Brief history

&nbsp;&nbsp;At first we want to develop an algorithm automatically tracking the whole construction process, based on the point cloud data collected by our DJI unmanned aerial vehicles. With no previous engineering knowledge.    
&nbsp;&nbsp;1. I started this project by consulting professionals at 3D modeling for advice. After a few days of effort, I proposed a workable but not optimal computation complexity algorithm, which was to search each pair corresponding points in two-day cloud points by sorting Euclidean distance between the points. The distance difference of the corresponding pairs we got was just the construction progress made. This algorithm did work, but was taking as long as 8 hours.   
&nbsp;&nbsp;2. In the second optimized version, I tried multi CPU threads to make it a parallel computation, and the process time was shortened to about two hours. However, my manager was expecting an even higher speed as half an hour. I struggled for the first few days, reading hundreds of papers and studying similar cases for possible solutions. Finally, I found the k-dimensional tree (KD-tree), which could be applied to both space searching and the nearest points searching. This approach worked very efficiently for this challenge, taking only a few minutes to finish the calculation. My manager was very satisfied with the performance optimization.


## Dependencies

    alembic==1.0.10
    appnope==0.1.0
    atomicwrites==1.3.0
    attrs==19.1.0
    backcall==0.1.0
    bleach==3.1.0
    certifi==2019.6.16
    chardet==3.0.4
    Click==7.0
    cognitojwt==1.1.0
    decorator==4.4.0
    defusedxml==0.6.0
    ecdsa==0.13.2
    entrypoints==0.3
    Flask==1.0.2
    Flask-Cognito==1.13
    Flask-Cors==3.0.7
    Flask-Migrate==2.4.0
    Flask-Script==2.0.6
    Flask-SQLAlchemy==2.4.0
    future==0.17.1
    idna==2.8
    ipykernel==5.1.2
    ipython==7.8.0
    ipython-genutils==0.2.0
    itsdangerous==1.1.0
    jedi==0.15.1
    Jinja2==2.10.1
    jsonschema==3.0.2
    jupyter-client==5.3.1
    jupyter-core==4.5.0
    Mako==1.0.10
    MarkupSafe==1.1.1
    mistune==0.8.4
    mkl-fft==1.0.14
    mkl-random==1.0.2
    mkl-service==2.0.2
    more-itertools==7.0.0
    nbconvert==5.5.0
    nbformat==4.4.0
    notebook==6.0.0
    numpy==1.16.4
    pandas==0.25.1
    pandocfilters==1.4.2
    parso==0.5.1
    pexpect==4.7.0
    pickleshare==0.7.5
    pluggy==0.11.0
    prettytable==0.7.2
    prometheus-client==0.7.1
    prompt-toolkit==2.0.9
    psycopg2-binary==2.8.2
    ptyprocess==0.6.0
    py==1.8.0
    pyasn1==0.4.5
    pyecharts==1.3.1
    Pygments==2.4.2
    pyrsistent==0.14.11
    pytest==4.5.0
    python-dateutil==2.8.0
    python-editor==1.0.4
    python-jose==3.0.1
    pytz==2019.2
    pyzmq==18.1.0
    requests==2.22.0
    rsa==4.0
    Send2Trash==1.5.0
    simplejson==3.16.0
    six==1.12.0
    SQLAlchemy==1.3.3
    terminado==0.8.2
    testpath==0.4.2
    tornado==6.0.3
    traitlets==4.3.2
    urllib3==1.25.2
    wcwidth==0.1.7
    webencodings==0.5.1

## Latest Version of README

For the latest online version of the README.md, I updated it in 11/10/2020
