<p align="center"><img src="https://github.com/Nefcore/CRLFsuite/blob/main/static/crlfsuite_logo.png" height="200"/></p>
<h2 align="center">CRLFsuite - CRLF injection scanner</h2>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![GitHub release](https://img.shields.io/github/release/Nefcore/CRLFsuite)](https://GitHub.com/Nefcore/CRLFsuite/releases/)
[![GitHub forks](https://badgen.net/github/forks/Nefcore/CRLFsuite/)](https://GitHub.com/Nefcore/CRLFsuite/network/)
[![GitHub contributors](https://img.shields.io/github/contributors/Nefcore/CRLFsuite)](https://GitHub.com/Nefcore/badges/graphs/contributors/)

CRLFsuite is a fast tool specially designed to scan `CRLF injection`.

<img src="https://github.com/Nefcore/CRLFsuite/blob/main/static/crlfsuitev2.0.svg">

<hr>

## ⬇️ Installation

```ruby
$ git clone https://github.com/Nefcore/CRLFsuite.git
$ cd CRLFsuite
$ sudo python3 setup.py install
$ crlfsuite -h
```

## ⚙️ Features

:heavy_check_mark: Single URL scanning

:heavy_check_mark: Multiple URL scanning

:heavy_check_mark: WAF detection

:heavy_check_mark: XSS through CRLF injection

:heavy_check_mark: Stdin supported

:heavy_check_mark: GET & POST method supported

:heavy_check_mark: Concurrency

:heavy_check_mark: Powerful payloads (WAF evasion payloads are also included)

:heavy_check_mark: Fast and efficient scanning with negligible false-positive

## 📈 Usage

Single URL scanning:

```python
$ crlfsuite -u "http://testphp.vulnweb.com"
```

Multiple URLs scanning:

```
$ crlfsuite -i targets.txt
```

from stdin:

```bash
$ subfinder -d google.com -silent | httpx -silent | crlfsuite -s
```

Specifying cookies 🍪:

```python
$ crlfsuite -u "http://testphp.vulnweb.com" --cookies "key=val; newkey=newval"
```

Using POST method:

```python
$ crlfsuite -i targets.txt -m POST -d "key=val&newkey=newval"
```

## 🔑 License

:point_right: <a href="https://github.com/Nefcore/CRLFsuite/blob/main/LICENSE">MIT LICENSE</a>

## 🐞 Bug report

If You're facing some errors or issues with this tool, you can open a issue here:

👉 <a href="https://github.com/Nefcore/CRLFsuite/issues">Open a issue</a>
