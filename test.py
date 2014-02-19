import memjpegoptim

jpeg = memjpegoptim.optimizeJPEG(open("test.jpg").read(), 100)
if  not jpeg[6:10] in (b'JFIF', b'Exif'):
    print "invalid jpeg"
else:
    print "jpeg ok"

