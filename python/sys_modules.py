"""check how hodules available."""

import sys
import textwrap


names = sorted(sys.modules.keys())
name_text = ', '.join(names)

print(textwrap.fill(name_text, width=64))

'''
RESULTS:
__main__, _abc, _codecs, _collections, _collections_abc,
_distutils_hack, _frozen_importlib, _frozen_importlib_external,
_functools, _imp, _io, _locale, _operator, _signal,
_sitebuiltins, _sre, _stat, _thread, _warnings, _weakref, abc,
apport_python_hook, builtins, codecs, collections, contextlib,
copyreg, encodings, encodings.aliases, encodings.utf_8, enum,
functools, genericpath, google, importlib, importlib._abc,
importlib._bootstrap, importlib._bootstrap_external,
importlib.machinery, importlib.util, io, itertools, keyword,
marshal, operator, os, os.path, posix, posixpath, re, reprlib,
site, sitecustomize, sre_compile, sre_constants, sre_parse,
stat, sys, textwrap, time, types, warnings, zipimport
'''
