from cffi import FFI
import os

ffi = FFI()

ffi.cdef("""int encodeJPEG(unsigned char *inputbuffer, int width, int height, unsigned char **outputbuffer, unsigned long *outputsize, int quality);
        int optimizeJPEG(unsigned char *inputbuffer, unsigned long inputsize, unsigned char **outputbuffer, unsigned long *outputsize, int quality);""")

lib = ffi.verify(sources=['src/memjpegoptim.c'], libraries=['jpeg'])

def optimizeJPEG(buf, quality):
    output = ffi.new("unsigned char**")
    size = ffi.new("unsigned long*")
    lib.optimizeJPEG(buf, len(buf), output, size, quality)

    if size[0] > 0:
        return ffi.buffer(output[0], size[0])
