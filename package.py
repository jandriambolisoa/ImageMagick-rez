name = "ImageMagick"

version = "7.1.2"

authors = [
    "ImageMagick Studio LLC",
    "Jeremy Andriambolisoa",
]

description = \
    """
    ImageMagick® is a free, open-source software suite, used for editing and manipulating digital images. It can be used to create, edit, compose, or convert bitmap images, and supports a wide range of file formats, including JPEG, PNG, GIF, TIFF, and Ultra HDR.
    """

requires = [
    "python-3",
]

uuid = "ImageMagick.ImageMagick"

build_command = "python {root}/build.py {install}"

def commands():
    env.PATH.append("{root}/src/ImageMagick-7.1.2-Q16-HDRI/")
