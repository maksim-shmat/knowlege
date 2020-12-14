""" About Sphinx."""

pip install -U sphinx (???) # from sphinx docs for linux
python3 -m pip install Sphinx  # from django docs

sphinx-build --version  # all ok?

sphinx-quickstart
# all pkgs in venv2/lib

sphinx-build -b html (sourcedir, I`m go in and write . ) builddir

make  # all variants of add to make: html, txt, etc

-For Docer load from Docker Hub:
    sphinxdoc/sphinx  - vanila
    sphinxdoc/sphinx-latexpdg  - pdf(2Gb you serious?!)
$ docker run -it --rm -v /path/to/document:/docx sphinxdoc/sphinx sphinx-quickstart  (for start)

$ docker run --rm -v /path/to/document:/docs sphinxdoc/sphinx make html
(make html)

This is Head
============

This is Second Head
-------------------

This is list.
* One element
* Two element

This is autonumeric list
#. Element 1
#. Element 2

*cursive text*
**Fat text**
``code``


