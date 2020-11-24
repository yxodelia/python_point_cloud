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

Tesseract was originally developed at Hewlett-Packard Laboratories Bristol and
at Hewlett-Packard Co, Greeley Colorado between 1985 and 1994, with some
more changes made in 1996 to port to Windows, and some C++izing in 1998.
In 2005 Tesseract was open sourced by HP. Since 2006 it is developed by Google.

The latest (LSTM based) stable version is **[4.1.1](https://github.com/tesseract-ocr/tesseract/releases/tag/4.1.1)**, released on December 26, 2019.
Latest source code is available from [master branch on GitHub](https://github.com/tesseract-ocr/tesseract/tree/master).
Open issues can be found in [issue tracker](https://github.com/tesseract-ocr/tesseract/issues),
and [planning documentation](https://tesseract-ocr.github.io/tessdoc/Planning.html).

The latest 3.0x version is **[3.05.02](https://github.com/tesseract-ocr/tesseract/releases/tag/3.05.02)**, released on June 19, 2018. Latest source code for 3.05 is available from [3.05 branch on GitHub](https://github.com/tesseract-ocr/tesseract/tree/3.05).
There is no development for this version, but it can be used for special cases (e.g. see [Regression of features from 3.0x](https://tesseract-ocr.github.io/tessdoc/Planning.html#regression-of-features-from-30x)).

See **[Release Notes](https://tesseract-ocr.github.io/tessdoc/ReleaseNotes.html)**
and **[Change Log](https://github.com/tesseract-ocr/tesseract/blob/master/ChangeLog)** for more details of the releases.

## Installing Tesseract

You can either [Install Tesseract via pre-built binary package](https://tesseract-ocr.github.io/tessdoc/Home.html)
or [build it from source](https://tesseract-ocr.github.io/tessdoc/Compiling.html).

Supported Compilers are:

* GCC 4.8 and above
* Clang 3.4 and above
* MSVC 2015, 2017, 2019

Other compilers might work, but are not officially supported.

## Running Tesseract

Basic **[command line usage](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html)**:

    tesseract imagename outputbase [-l lang] [--oem ocrenginemode] [--psm pagesegmode] [configfiles...]

For more information about the various command line options use `tesseract --help` or `man tesseract`.

Examples can be found in the [documentation](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html#simplest-invocation-to-ocr-an-image).

## For developers

Developers can use `libtesseract` [C](https://github.com/tesseract-ocr/tesseract/blob/master/include/tesseract/capi.h) or
[C++](https://github.com/tesseract-ocr/tesseract/blob/master/include/tesseract/baseapi.h) API to build their own application.
If you need bindings to `libtesseract` for other programming languages, please see the
[wrapper](https://tesseract-ocr.github.io/tessdoc/AddOns.html#tesseract-wrappers) section in the AddOns documentation.

Documentation of Tesseract generated from source code by doxygen can be found on [tesseract-ocr.github.io](https://tesseract-ocr.github.io/).

## Support

Before you submit an issue, please review **[the guidelines for this repository](https://github.com/tesseract-ocr/tesseract/blob/master/CONTRIBUTING.md)**.

For support, first read the [documentation](https://tesseract-ocr.github.io/tessdoc/),
particularly the [FAQ](https://tesseract-ocr.github.io/tessdoc/FAQ.html) to see if your problem is addressed there.
If not, search the [Tesseract user forum](https://groups.google.com/d/forum/tesseract-ocr), the [Tesseract developer forum](https://groups.google.com/d/forum/tesseract-dev) and [past issues](https://github.com/tesseract-ocr/tesseract/issues), and if you still can't find what you need, ask for support in the mailing-lists.

Mailing-lists:
* [tesseract-ocr](https://groups.google.com/d/forum/tesseract-ocr) - For tesseract users.
* [tesseract-dev](https://groups.google.com/d/forum/tesseract-dev) - For tesseract developers.

Please report an issue only for a **bug**, not for asking questions.

## License

    The code in this repository is licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

**NOTE**: This software depends on other packages that may be licensed under different open source licenses.

Tesseract uses [Leptonica library](http://leptonica.com/) which essentially
uses a [BSD 2-clause license](http://leptonica.com/about-the-license.html).

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
