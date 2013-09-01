#!/usr/bin/env python
"""putils: utilities to projects.
"""

DOCLINES = __doc__.split("\n")

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import commands,re,sys

CLASSIFIERS = """\
Development Status :: Alpha
Intended Audience :: Developers
License :: GNU General Public License version 2.0 (GPLv2)
Programming Language :: Python
Topic :: Libraries
Operating System :: All POSIX (Linux/BSD/UNIX-like OSes)
"""

NAME                = 'putils'
MAINTAINER          = "Willians Costa da Silva"
MAINTAINER_EMAIL    = "willianscsilva@gmail.com"
DESCRIPTION         = DOCLINES[0]
LONG_DESCRIPTION    = "\n".join(DOCLINES[2:])
URL                 = "https://github.com/willianscsilva/putils"
DOWNLOAD_URL        = "https://github.com/willianscsilva/putils"
LICENSE             = 'GNU General Public License version 2.0 (GPLv2)'
CLASSIFIERS         = filter(None, CLASSIFIERS.split('\n'))
AUTHOR              = "Willians Costa da Silva"
AUTHOR_EMAIL        = "willianscsilva@gmail.com"
PLATFORMS           = ["Linux","Unix"]
MAJOR               = 0
MINOR               = 0
MICRO               = 1
VERSION             = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

if len(sys.argv) == 2:
    arg = sys.argv[1]
    if arg == "build" or arg == "install":
        ext_modules = [Extension("mysqlconn", ["mysqlconn.pyx"]), Extension("daemon", ["daemon.pyx"]),]
        for e in ext_modules:
            e.pyrex_directives = {"boundscheck": False}
            setup(
                name = NAME,
                maintainer=MAINTAINER,
                maintainer_email=MAINTAINER_EMAIL,
                description=DESCRIPTION,
                long_description=LONG_DESCRIPTION,
                url=URL,
                download_url=DOWNLOAD_URL,
                license=LICENSE,
                classifiers=CLASSIFIERS,
                author=AUTHOR,
                author_email=AUTHOR_EMAIL,
                platforms=PLATFORMS,
                version=VERSION,
                cmdclass = {"build_ext": build_ext},
                ext_modules = ext_modules
            )
