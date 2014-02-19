from distutils.core import setup

import memjpegoptim

setup(
    name='memjpegoptim',
    version='0.1',
    license='BSD',
    description='An in memory jpegoptim chain toolkit for Python.',
    long_description="""An in memory jpegoptim chain toolkit for Python.

    See Documentation <https://github.com/akhenakh/memjpegoptim/blob/master/README.md>`_.""",
    author='Fabrice Aneche',
    author_email='akh@nobugware.com',
    url='https://github.com/akhenakh/memjpegoptim',
    ext_modules=[memjpegoptim.ffi.verifier.get_extension()],
    install_requires=['cffi >= 0.8'],
)
