# coding:utf-8

"""
filetype_.py
version = '0.0.1'
by tacey@AtomPai on 18-7-3
"""
import os
import subprocess

FILE_EXIST = True
try:
    exe_info = subprocess.check_output(['file', "--version"])
except OSError:
    FILE_EXIST = False
else:
    if not exe_info.startswith('file-'):
        FILE_EXIST = False


class Type(object):
    def __init__(self, mime, extension):
        self.__mime = mime
        self.__extension = extension

    @property
    def mime(self):
        return self.__mime

    @property
    def extension(self):
        return self.__extension

    @property
    def is_extension(self, extension):
        return self.__extension is extension

    @property
    def is_mime(self, mime):
        return self.__mime is mime

    def match(self, buf):
        raise NotImplementedError


# IMAGE

class Jpeg(Type):
    """
    Implements the JPEG image type matcher.
    """
    MIME = 'image/jpeg'
    EXTENSION = 'jpg'

    def __init__(self):
        super(Jpeg, self).__init__(
            mime=Jpeg.MIME,
            extension=Jpeg.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 2 and
                buf[0] == 0xFF and
                buf[1] == 0xD8 and
                buf[2] == 0xFF)


class Png(Type):
    """
    Implements the PNG image type matcher.
    """
    MIME = 'image/png'
    EXTENSION = 'png'

    def __init__(self):
        super(Png, self).__init__(
            mime=Png.MIME,
            extension=Png.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x89 and
                buf[1] == 0x50 and
                buf[2] == 0x4E and
                buf[3] == 0x47)


class Gif(Type):
    """
    Implements the GIF image type matcher.
    """
    MIME = 'image/gif'
    EXTENSION = 'gif'

    def __init__(self):
        super(Gif, self).__init__(
            mime=Gif.MIME,
            extension=Gif.EXTENSION,
        )

    def match(self, buf):
        return (len(buf) > 2 and
                buf[0] == 0x47 and
                buf[1] == 0x49 and
                buf[2] == 0x46)


class Webp(Type):
    """
    Implements the WEBP image type matcher.
    """
    MIME = 'image/webp'
    EXTENSION = 'webp'

    def __init__(self):
        super(Webp, self).__init__(
            mime=Webp.MIME,
            extension=Webp.EXTENSION,
        )

    def match(self, buf):
        return (len(buf) > 11 and
                buf[8] == 0x57 and
                buf[9] == 0x45 and
                buf[10] == 0x42 and
                buf[11] == 0x50)


class Cr2(Type):
    """
    Implements the CR2 image type matcher.
    """
    MIME = 'image/x-canon-cr2'
    EXTENSION = 'cr2'

    def __init__(self):
        super(Cr2, self).__init__(
            mime=Cr2.MIME,
            extension=Cr2.EXTENSION,
        )

    def match(self, buf):
        return (len(buf) > 9 and
                ((buf[0] == 0x49 and buf[1] == 0x49 and
                  buf[2] == 0x2A and buf[3] == 0x0) or
                 (buf[0] == 0x4D and buf[1] == 0x4D and
                  buf[2] == 0x0 and buf[3] == 0x2A)) and
                buf[8] == 0x43 and buf[9] == 0x52)


class Tiff(Type):
    """
    Implements the TIFF image type matcher.
    """
    MIME = 'image/tiff'
    EXTENSION = 'tif'

    def __init__(self):
        super(Tiff, self).__init__(
            mime=Tiff.MIME,
            extension=Tiff.EXTENSION,
        )

    def match(self, buf):
        return (len(buf) > 3 and
                ((buf[0] == 0x49 and buf[1] == 0x49 and
                  buf[2] == 0x2A and buf[3] == 0x0) or
                 (buf[0] == 0x4D and buf[1] == 0x4D and
                  buf[2] == 0x0 and buf[3] == 0x2A)))


class Bmp(Type):
    """
    Implements the BMP image type matcher.
    """
    MIME = 'image/bmp'
    EXTENSION = 'bmp'

    def __init__(self):
        super(Bmp, self).__init__(
            mime=Bmp.MIME,
            extension=Bmp.EXTENSION,
        )

    def match(self, buf):
        return (len(buf) > 1 and
                buf[0] == 0x42 and
                buf[1] == 0x4D)


class Jxr(Type):
    """
    Implements the JXR image type matcher.
    """
    MIME = 'image/vnd.ms-photo'
    EXTENSION = 'jxr'

    def __init__(self):
        super(Jxr, self).__init__(
            mime=Jxr.MIME,
            extension=Jxr.EXTENSION,
        )

    def match(self, buf):
        return (len(buf) > 2 and
                buf[0] == 0x49 and
                buf[1] == 0x49 and
                buf[2] == 0xBC)


class Psd(Type):
    """
    Implements the PSD image type matcher.
    """
    MIME = 'image/vnd.adobe.photoshop'
    EXTENSION = 'psd'

    def __init__(self):
        super(Psd, self).__init__(
            mime=Psd.MIME,
            extension=Psd.EXTENSION,
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x38 and
                buf[1] == 0x42 and
                buf[2] == 0x50 and
                buf[3] == 0x53)


class Ico(Type):
    """
    Implements the ICO image type matcher.
    """
    MIME = 'image/x-icon'
    EXTENSION = 'ico'

    def __init__(self):
        super(Ico, self).__init__(
            mime=Ico.MIME,
            extension=Ico.EXTENSION,
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x00 and
                buf[1] == 0x00 and
                buf[2] == 0x01 and
                buf[3] == 0x00)


#  VIDEO

class Mp4(Type):
    """
    Implements the MP4 video type matcher.
    """
    MIME = 'video/mp4'
    EXTENSION = 'mp4'

    def __init__(self):
        super(Mp4, self).__init__(
            mime=Mp4.MIME,
            extension=Mp4.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 27 and
                (buf[0] == 0x0 and buf[1] == 0x0 and
                 buf[2] == 0x0 and
                 ((buf[3] == 0x18 or
                   buf[3] == 0x20) and
                  buf[4] == 0x66 and
                  buf[5] == 0x74 and buf[6] == 0x79 and
                  buf[7] == 0x70) or
                 (buf[0] == 0x33 and buf[1] == 0x67 and
                  buf[2] == 0x70 and buf[3] == 0x35) or
                 (buf[0] == 0x0 and buf[1] == 0x0 and
                  buf[2] == 0x0 and buf[3] == 0x1C and
                  buf[4] == 0x66 and buf[5] == 0x74 and
                  buf[6] == 0x79 and buf[7] == 0x70 and
                  buf[8] == 0x6D and buf[9] == 0x70 and
                  buf[10] == 0x34 and buf[11] == 0x32 and
                  buf[16] == 0x6D and buf[17] == 0x70 and
                  buf[18] == 0x34 and buf[19] == 0x31 and
                  buf[20] == 0x6D and buf[21] == 0x70 and
                  buf[22] == 0x34 and buf[23] == 0x32 and
                  buf[24] == 0x69 and buf[25] == 0x73 and
                  buf[26] == 0x6F and buf[27] == 0x6D)))


class M4v(Type):
    """
    Implements the M4V video type matcher.
    """
    MIME = 'video/x-m4v'
    EXTENSION = 'm4v'

    def __init__(self):
        super(M4v, self).__init__(
            mime=M4v.MIME,
            extension=M4v.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 10 and
                buf[0] == 0x0 and buf[1] == 0x0 and
                buf[2] == 0x0 and buf[3] == 0x1C and
                buf[4] == 0x66 and buf[5] == 0x74 and
                buf[6] == 0x79 and buf[7] == 0x70 and
                buf[8] == 0x4D and buf[9] == 0x34 and
                buf[10] == 0x56)


class Mkv(Type):
    """
    Implements the MKV video type matcher.
    """
    MIME = 'video/x-matroska'
    EXTENSION = 'mkv'

    def __init__(self):
        super(Mkv, self).__init__(
            mime=Mkv.MIME,
            extension=Mkv.EXTENSION
        )

    def match(self, buf):
        return ((len(buf) > 15 and
                 buf[0] == 0x1A and buf[1] == 0x45 and
                 buf[2] == 0xDF and buf[3] == 0xA3 and
                 buf[4] == 0x93 and buf[5] == 0x42 and
                 buf[6] == 0x82 and buf[7] == 0x88 and
                 buf[8] == 0x6D and buf[9] == 0x61 and
                 buf[10] == 0x74 and buf[11] == 0x72 and
                 buf[12] == 0x6F and buf[13] == 0x73 and
                 buf[14] == 0x6B and buf[15] == 0x61) or
                (len(buf) > 38 and
                 buf[31] == 0x6D and buf[32] == 0x61 and
                 buf[33] == 0x74 and buf[34] == 0x72 and
                 buf[35] == 0x6f and buf[36] == 0x73 and
                 buf[37] == 0x6B and buf[38] == 0x61))


class Webm(Type):
    """
    Implements the WebM video type matcher.
    """
    MIME = 'video/webm'
    EXTENSION = 'webm'

    def __init__(self):
        super(Webm, self).__init__(
            mime=Webm.MIME,
            extension=Webm.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x1A and
                buf[1] == 0x45 and
                buf[2] == 0xDF and
                buf[3] == 0xA3)


class Mov(Type):
    """
    Implements the MOV video type matcher.
    """
    MIME = 'video/quicktime'
    EXTENSION = 'mov'

    def __init__(self):
        super(Mov, self).__init__(
            mime=Mov.MIME,
            extension=Mov.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 7 and
                buf[0] == 0x0 and
                buf[1] == 0x0 and
                buf[2] == 0x0 and
                buf[3] == 0x14 and
                buf[4] == 0x66 and
                buf[5] == 0x74 and
                buf[6] == 0x79 and
                buf[7] == 0x70)


class Avi(Type):
    """
    Implements the AVI video type matcher.
    """
    MIME = 'video/x-msvideo'
    EXTENSION = 'avi'

    def __init__(self):
        super(Avi, self).__init__(
            mime=Avi.MIME,
            extension=Avi.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 10 and
                buf[0] == 0x52 and
                buf[1] == 0x49 and
                buf[2] == 0x46 and
                buf[3] == 0x46 and
                buf[8] == 0x41 and
                buf[9] == 0x56 and
                buf[10] == 0x49)


class Wmv(Type):
    """
    Implements the WMV video type matcher.
    """
    MIME = 'video/x-ms-wmv'
    EXTENSION = 'wmv'

    def __init__(self):
        super(Wmv, self).__init__(
            mime=Wmv.MIME,
            extension=Wmv.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 9 and
                buf[0] == 0x30 and
                buf[1] == 0x26 and
                buf[2] == 0xB2 and
                buf[3] == 0x75 and
                buf[4] == 0x8E and
                buf[5] == 0x66 and
                buf[6] == 0xCF and
                buf[7] == 0x11 and
                buf[8] == 0xA6 and
                buf[9] == 0xD9)


class Flv(Type):
    """
    Implements the FLV video type matcher.
    """
    MIME = 'video/x-flv'
    EXTENSION = 'flv'

    def __init__(self):
        super(Flv, self).__init__(
            mime=Flv.MIME,
            extension=Flv.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x46 and
                buf[1] == 0x4C and
                buf[2] == 0x56 and
                buf[3] == 0x01)


class Mpeg(Type):
    """
    Implements the MPEG video type matcher.
    """
    MIME = 'video/mpeg'
    EXTENSION = 'mpg'

    def __init__(self):
        super(Mpeg, self).__init__(
            mime=Mpeg.MIME,
            extension=Mpeg.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x0 and
                buf[1] == 0x0 and
                buf[2] == 0x1 and
                buf[3] >= 0xb0 and
                buf[3] <= 0xbf)


# AUDIO

class Midi(Type):
    """
    Implements the Midi audio type matcher.
    """
    MIME = 'audio/midi'
    EXTENSION = 'midi'

    def __init__(self):
        super(Midi, self).__init__(
            mime=Midi.MIME,
            extension=Midi.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x4D and
                buf[1] == 0x54 and
                buf[2] == 0x68 and
                buf[3] == 0x64)


class Mp3(Type):
    """
    Implements the MP3 audio type matcher.
    """
    MIME = 'audio/mpeg'
    EXTENSION = 'mp3'

    def __init__(self):
        super(Mp3, self).__init__(
            mime=Mp3.MIME,
            extension=Mp3.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 2 and
                ((buf[0] == 0x49 and
                  buf[1] == 0x44 and
                  buf[2] == 0x33) or
                 (buf[0] == 0xFF and
                  buf[1] == 0xfb)))


class M4a(Type):
    """
    Implements the M4A audio type matcher.
    """
    MIME = 'audio/m4a'
    EXTENSION = 'm4a'

    def __init__(self):
        super(M4a, self).__init__(
            mime=M4a.MIME,
            extension=M4a.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 10 and
                ((buf[4] == 0x66 and
                  buf[5] == 0x74 and
                  buf[6] == 0x79 and
                  buf[7] == 0x70 and
                  buf[8] == 0x4D and
                  buf[9] == 0x34 and
                  buf[10] == 0x41) or
                 (buf[0] == 0x4D and
                  buf[1] == 0x34 and
                  buf[2] == 0x41 and
                  buf[3] == 0x20)))


class Ogg(Type):
    """
    Implements the OGG audio type matcher.
    """
    MIME = 'audio/ogg'
    EXTENSION = 'ogg'

    def __init__(self):
        super(Ogg, self).__init__(
            mime=Ogg.MIME,
            extension=Ogg.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x4F and
                buf[1] == 0x67 and
                buf[2] == 0x67 and
                buf[3] == 0x53)


class Flac(Type):
    """
    Implements the FLAC audio type matcher.
    """
    MIME = 'audio/x-flac'
    EXTENSION = 'flac'

    def __init__(self):
        super(Flac, self).__init__(
            mime=Flac.MIME,
            extension=Flac.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x66 and
                buf[1] == 0x4C and
                buf[2] == 0x61 and
                buf[3] == 0x43)


class Wav(Type):
    """
    Implements the WAV audio type matcher.
    """
    MIME = 'audio/x-wav'
    EXTENSION = 'wav'

    def __init__(self):
        super(Wav, self).__init__(
            mime=Wav.MIME,
            extension=Wav.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 11 and
                buf[0] == 0x52 and
                buf[1] == 0x49 and
                buf[2] == 0x46 and
                buf[3] == 0x46 and
                buf[8] == 0x57 and
                buf[9] == 0x41 and
                buf[10] == 0x56 and
                buf[11] == 0x45)


class Amr(Type):
    """
    Implements the AMR audio type matcher.
    """
    MIME = 'audio/amr'
    EXTENSION = 'amr'

    def __init__(self):
        super(Amr, self).__init__(
            mime=Amr.MIME,
            extension=Amr.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 11 and
                buf[0] == 0x23 and
                buf[1] == 0x21 and
                buf[2] == 0x41 and
                buf[3] == 0x4D and
                buf[4] == 0x52 and
                buf[5] == 0x0A)


# FONT

class Woff(Type):
    """
    Implements the WOFF font type matcher.
    """
    MIME = 'application/font-woff'
    EXTENSION = 'woff'

    def __init__(self):
        super(Woff, self).__init__(
            mime=Woff.MIME,
            extension=Woff.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 7 and
                buf[0] == 0x77 and
                buf[1] == 0x4F and
                buf[2] == 0x46 and
                buf[3] == 0x46 and
                buf[4] == 0x00 and
                buf[5] == 0x01 and
                buf[6] == 0x00 and
                buf[7] == 0x00)


class Woff2(Type):
    """
    Implements the WOFF2 font type matcher.
    """
    MIME = 'application/font-woff'
    EXTENSION = 'woff2'

    def __init__(self):
        super(Woff2, self).__init__(
            mime=Woff2.MIME,
            extension=Woff2.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 7 and
                buf[0] == 0x77 and
                buf[1] == 0x4F and
                buf[2] == 0x46 and
                buf[3] == 0x32 and
                buf[4] == 0x00 and
                buf[5] == 0x01 and
                buf[6] == 0x00 and
                buf[7] == 0x00)


class Ttf(Type):
    """
    Implements the TTF font type matcher.
    """
    MIME = 'application/font-sfnt'
    EXTENSION = 'ttf'

    def __init__(self):
        super(Ttf, self).__init__(
            mime=Ttf.MIME,
            extension=Ttf.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 4 and
                buf[0] == 0x00 and
                buf[1] == 0x01 and
                buf[2] == 0x00 and
                buf[3] == 0x00 and
                buf[4] == 0x00)


class Otf(Type):
    """
    Implements the OTF font type matcher.
    """
    MIME = 'application/font-sfnt'
    EXTENSION = 'otf'

    def __init__(self):
        super(Otf, self).__init__(
            mime=Otf.MIME,
            extension=Otf.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 4 and
                buf[0] == 0x4F and
                buf[1] == 0x54 and
                buf[2] == 0x54 and
                buf[3] == 0x4F and
                buf[4] == 0x00)


# ARCHIVE 压缩包


class Epub(Type):
    """
    Implements the EPUB archive type matcher.
    """
    MIME = 'application/epub+zip'
    EXTENSION = 'epub'

    def __init__(self):
        super(Epub, self).__init__(
            mime=Epub.MIME,
            extension=Epub.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 57 and
                buf[0] == 0x50 and buf[1] == 0x4B and
                buf[2] == 0x3 and buf[3] == 0x4 and
                buf[30] == 0x6D and buf[31] == 0x69 and
                buf[32] == 0x6D and buf[33] == 0x65 and
                buf[34] == 0x74 and buf[35] == 0x79 and
                buf[36] == 0x70 and buf[37] == 0x65 and
                buf[38] == 0x61 and buf[39] == 0x70 and
                buf[40] == 0x70 and buf[41] == 0x6C and
                buf[42] == 0x69 and buf[43] == 0x63 and
                buf[44] == 0x61 and buf[45] == 0x74 and
                buf[46] == 0x69 and buf[47] == 0x6F and
                buf[48] == 0x6E and buf[49] == 0x2F and
                buf[50] == 0x65 and buf[51] == 0x70 and
                buf[52] == 0x75 and buf[53] == 0x62 and
                buf[54] == 0x2B and buf[55] == 0x7A and
                buf[56] == 0x69 and buf[57] == 0x70)


class Zip(Type):
    """
    Implements the Zip archive type matcher.
    """
    MIME = 'application/zip'
    EXTENSION = 'zip'

    def __init__(self):
        super(Zip, self).__init__(
            mime=Zip.MIME,
            extension=Zip.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x50 and buf[1] == 0x4B and
                (buf[2] == 0x3 or buf[2] == 0x5 or
                 buf[2] == 0x7) and
                (buf[3] == 0x4 or buf[3] == 0x6 or
                 buf[3] == 0x8))


class Tar(Type):
    """
    Implements the Tar archive type matcher.
    """
    MIME = 'application/x-tar'
    EXTENSION = 'tar'

    def __init__(self):
        super(Tar, self).__init__(
            mime=Tar.MIME,
            extension=Tar.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 261 and
                buf[257] == 0x75 and
                buf[258] == 0x73 and
                buf[259] == 0x74 and
                buf[260] == 0x61 and
                buf[261] == 0x72)


class Rar(Type):
    """
    Implements the RAR archive type matcher.
    """
    MIME = 'application/x-rar-compressed'
    EXTENSION = 'rar'

    def __init__(self):
        super(Rar, self).__init__(
            mime=Rar.MIME,
            extension=Rar.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 6 and
                buf[0] == 0x52 and
                buf[1] == 0x61 and
                buf[2] == 0x72 and
                buf[3] == 0x21 and
                buf[4] == 0x1A and
                buf[5] == 0x7 and
                (buf[6] == 0x0 or
                 buf[6] == 0x1))


class Gz(Type):
    """
    Implements the GZ archive type matcher.
    """
    MIME = 'application/gzip'
    EXTENSION = 'gz'

    def __init__(self):
        super(Gz, self).__init__(
            mime=Gz.MIME,
            extension=Gz.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 2 and
                buf[0] == 0x1F and
                buf[1] == 0x8B and
                buf[2] == 0x8)


class Bz2(Type):
    """
    Implements the BZ2 archive type matcher.
    """
    MIME = 'application/x-bzip2'
    EXTENSION = 'bz2'

    def __init__(self):
        super(Bz2, self).__init__(
            mime=Bz2.MIME,
            extension=Bz2.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 2 and
                buf[0] == 0x42 and
                buf[1] == 0x5A and
                buf[2] == 0x68)


class SevenZ(Type):
    """
    Implements the SevenZ (7z) archive type matcher.
    """
    MIME = 'application/x-7z-compressed'
    EXTENSION = '7z'

    def __init__(self):
        super(SevenZ, self).__init__(
            mime=SevenZ.MIME,
            extension=SevenZ.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 5 and
                buf[0] == 0x37 and
                buf[1] == 0x7A and
                buf[2] == 0xBC and
                buf[3] == 0xAF and
                buf[4] == 0x27 and
                buf[5] == 0x1C)


class Pdf(Type):
    """
    Implements the PDF archive type matcher.
    """
    MIME = 'application/pdf'
    EXTENSION = 'pdf'

    def __init__(self):
        super(Pdf, self).__init__(
            mime=Pdf.MIME,
            extension=Pdf.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x25 and
                buf[1] == 0x50 and
                buf[2] == 0x44 and
                buf[3] == 0x46)


class Exe(Type):
    """
    Implements the EXE archive type matcher.
    """
    MIME = 'application/x-msdownload'
    EXTENSION = 'exe'

    def __init__(self):
        super(Exe, self).__init__(
            mime=Exe.MIME,
            extension=Exe.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 1 and
                buf[0] == 0x4D and
                buf[1] == 0x5A)


class Swf(Type):
    """
    Implements the SWF archive type matcher.
    """
    MIME = 'application/x-shockwave-flash'
    EXTENSION = 'swf'

    def __init__(self):
        super(Swf, self).__init__(
            mime=Swf.MIME,
            extension=Swf.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 2 and
                (buf[0] == 0x43 or
                 buf[0] == 0x46) and
                buf[1] == 0x57 and
                buf[2] == 0x53)


class Rtf(Type):
    """
    Implements the RTF archive type matcher.
    """
    MIME = 'application/rtf'
    EXTENSION = 'rtf'

    def __init__(self):
        super(Rtf, self).__init__(
            mime=Rtf.MIME,
            extension=Rtf.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 4 and
                buf[0] == 0x7B and
                buf[1] == 0x5C and
                buf[2] == 0x72 and
                buf[3] == 0x74 and
                buf[4] == 0x66)


class Nes(Type):
    """
    Implements the NES archive type matcher.
    """
    MIME = 'application/x-nintendo-nes-rom'
    EXTENSION = 'nes'

    def __init__(self):
        super(Nes, self).__init__(
            mime=Nes.MIME,
            extension=Nes.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x4E and
                buf[1] == 0x45 and
                buf[2] == 0x53 and
                buf[3] == 0x1A)


class Crx(Type):
    """
    Implements the CRX archive type matcher.
    """
    MIME = 'application/x-google-chrome-extension'
    EXTENSION = 'crx'

    def __init__(self):
        super(Crx, self).__init__(
            mime=Crx.MIME,
            extension=Crx.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x43 and
                buf[1] == 0x72 and
                buf[2] == 0x32 and
                buf[3] == 0x34)


class Cab(Type):
    """
    Implements the CAB archive type matcher.
    """
    MIME = 'application/vnd.ms-cab-compressed'
    EXTENSION = 'cab'

    def __init__(self):
        super(Cab, self).__init__(
            mime=Cab.MIME,
            extension=Cab.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                ((buf[0] == 0x4D and
                  buf[1] == 0x53 and
                  buf[2] == 0x43 and
                  buf[3] == 0x46) or
                 (buf[0] == 0x49 and
                  buf[1] == 0x53 and
                  buf[2] == 0x63 and
                  buf[3] == 0x28)))


class Eot(Type):
    """
    Implements the EOT archive type matcher.
    """
    MIME = 'application/octet-stream'
    EXTENSION = 'eot'

    def __init__(self):
        super(Eot, self).__init__(
            mime=Eot.MIME,
            extension=Eot.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 35 and
                buf[34] == 0x4C and
                buf[35] == 0x50 and
                ((buf[8] == 0x02 and
                  buf[9] == 0x00 and
                  buf[10] == 0x01) or
                 (buf[8] == 0x01 and
                  buf[9] == 0x00 and
                  buf[10] == 0x00) or
                 (buf[8] == 0x02 and
                  buf[9] == 0x00 and
                  buf[10] == 0x02)))


class Ps(Type):
    """
    Implements the PS archive type matcher.
    """
    MIME = 'application/postscript'
    EXTENSION = 'ps'

    def __init__(self):
        super(Ps, self).__init__(
            mime=Ps.MIME,
            extension=Ps.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 1 and
                buf[0] == 0x25 and
                buf[1] == 0x21)


class Xz(Type):
    """
    Implements the XS archive type matcher.
    """
    MIME = 'application/x-xz'
    EXTENSION = 'xz'

    def __init__(self):
        super(Xz, self).__init__(
            mime=Xz.MIME,
            extension=Xz.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 5 and
                buf[0] == 0xFD and
                buf[1] == 0x37 and
                buf[2] == 0x7A and
                buf[3] == 0x58 and
                buf[4] == 0x5A and
                buf[5] == 0x00)


class Sqlite(Type):
    """
    Implements the Sqlite DB archive type matcher.
    """
    MIME = 'application/x-sqlite3'
    EXTENSION = 'sqlite'

    def __init__(self):
        super(Sqlite, self).__init__(
            mime=Sqlite.MIME,
            extension=Sqlite.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x53 and
                buf[1] == 0x51 and
                buf[2] == 0x4C and
                buf[3] == 0x69)


class Deb(Type):
    """
    Implements the DEB archive type matcher.
    """
    MIME = 'application/x-deb'
    EXTENSION = 'deb'

    def __init__(self):
        super(Deb, self).__init__(
            mime=Deb.MIME,
            extension=Deb.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 20 and
                buf[0] == 0x21 and
                buf[1] == 0x3C and
                buf[2] == 0x61 and
                buf[3] == 0x72 and
                buf[4] == 0x63 and
                buf[5] == 0x68 and
                buf[6] == 0x3E and
                buf[7] == 0x0A and
                buf[8] == 0x64 and
                buf[9] == 0x65 and
                buf[10] == 0x62 and
                buf[11] == 0x69 and
                buf[12] == 0x61 and
                buf[13] == 0x6E and
                buf[14] == 0x2D and
                buf[15] == 0x62 and
                buf[16] == 0x69 and
                buf[17] == 0x6E and
                buf[18] == 0x61 and
                buf[19] == 0x72 and
                buf[20] == 0x79)


class Ar(Type):
    """
    Implements the AR archive type matcher.
    """
    MIME = 'application/x-unix-archive'
    EXTENSION = 'ar'

    def __init__(self):
        super(Ar, self).__init__(
            mime=Ar.MIME,
            extension=Ar.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 6 and
                buf[0] == 0x21 and
                buf[1] == 0x3C and
                buf[2] == 0x61 and
                buf[3] == 0x72 and
                buf[4] == 0x63 and
                buf[5] == 0x68 and
                buf[6] == 0x3E)


class Z(Type):
    """
    Implements the Z archive type matcher.
    """
    MIME = 'application/x-compress'
    EXTENSION = 'Z'

    def __init__(self):
        super(Z, self).__init__(
            mime=Z.MIME,
            extension=Z.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 1 and
                ((buf[0] == 0x1F and
                  buf[1] == 0xA0) or
                 (buf[0] == 0x1F and
                  buf[1] == 0x9D)))


class Lz(Type):
    """
    Implements the Lz archive type matcher.
    """
    MIME = 'application/x-lzip'
    EXTENSION = 'lz'

    def __init__(self):
        super(Lz, self).__init__(
            mime=Lz.MIME,
            extension=Lz.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x4C and
                buf[1] == 0x5A and
                buf[2] == 0x49 and
                buf[3] == 0x50)


TYPES = [v() for v in locals().values() if type(v) == type(object) and issubclass(v, Type) and v != Type]


# utils

def get_sig_by_path(path):
    with open(path, 'rb') as fp:
        return bytearray(fp.read(262))


def get_sig_by_file_like(file_obj):
    byte = bytearray(file_obj.read(262))
    if byte:
        return byte
    elif hasattr(file_obj, 'getvalue'):
        return bytearray(file_obj.getvalue())[:262]


def get_sig_by_str_like(str_obj):
    return bytearray(str_obj)[:262]


def signature(array):
    """
    Returns the first 262 bytes of the given bytearray
    as part of the file header signature.

    Args:
        array: bytearray to extract the header signature.

    Returns:
        First 262 bytes of the file content as bytearray type.
    """
    length = len(array)
    index = 262 if length > 262 else length

    return array[:index]


def get_bytes(obj):
    """
    Infers the input type and reads the first 262 bytes,
    returning a sliced bytearray.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        First 262 bytes of the file content as bytearray type.

    Raises:
        TypeError: if obj is not a supported type.
    """
    kind = type(obj)
    print kind
    if kind is str:
        try:
            open(obj)
        except Exception:
            kind = "str_like"
    if hasattr(obj, "read"):
        kind = "file_like"
    print kind
    adapt_map = {
        bytearray: signature,
        bytes: signature,
        str: get_sig_by_path,
        "str_like": get_sig_by_str_like,
        "file_like": get_sig_by_file_like,
        memoryview: lambda x: signature(x).tolist(),
    }
    default = lambda xz: TypeError('Unsupported type as file input: %s' % kind)
    return adapt_map.get(kind, default)(obj)


def match(obj, matchers=TYPES):
    """
    Matches the given input againts the available
    file type matchers.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        Type instance if type matches. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    buf = get_bytes(obj)

    for matcher in matchers:
        if matcher.match(buf):
            return matcher

    return None


def is_extension_supported(ext):
    """
    Checks if the given extension string is
    one of the supported by the file matchers.

    Args:
        ext (str): file extension string. E.g: jpg, png, mp4, mp3

    Returns:
        True if the file extension is supported.
        Otherwise False.
    """
    for kind in TYPES:
        if kind.extension is ext:
            return True
    return False


def guess(obj):
    """
    Infers the type of the given input.

    Function is overloaded to accept multiple types in input
    and peform the needed type inference based on it.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        The matched type instance. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match(obj) if obj else None


def guess_mime(obj):
    """
    Infers the file type of the given input
    and returns its MIME type.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        The matched MIME type as string. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    kind = guess(obj)
    return kind.mime if kind else kind


def guess_extension(obj):
    """
    Infers the file type of the given input
    and returns its RFC file extension.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        The matched file extension as string. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    kind = guess(obj)
    return kind.extension if kind else kind


def get_type(mime=None, ext=None):
    """
    Returns the file type instance searching by
    MIME type or file extension.

    Args:
        ext: file extension string. E.g: jpg, png, mp4, mp3
        mime: MIME string. E.g: image/jpeg, video/mpeg

    Returns:
        The matched file type instance. Otherwise None.
    """
    for kind in TYPES:
        if kind.extension is ext or kind.mime is mime:
            return kind
    return None


def add_type(instance):
    """
    Adds a new type matcher instance to the supported types.

    Args:
        instance: Type inherited instance.

    Returns:
        None
    """
    if not isinstance(instance, Type):
        raise TypeError('instance must inherit from filetype.types.Type')

    TYPES.insert(0, instance)





if __name__ == "__main__":
    from io import BytesIO

    file_path = "tests/files/1.tar.gz"
    # kind = guess(file_path)
    # kind = guess(open(file_path, 'rb').read())
    stash = BytesIO()
    stash.write(open(file_path, 'rb').read())
    kind = guess(stash)

    print kind

    if kind is None:
        print('Cannot guess file type!')

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)
