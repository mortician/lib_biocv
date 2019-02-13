########################################################################################################################
# LIB_BIOCV.LIB_TEX - BIOHAZARD CODE VERONICA X TEXTURE DATA
#=======================================================================================================================
# 2015, 2019 MORTICIAN (THE_MORTICIAN@HOTMAIL.DE)
########################################################################################################################
import struct

class tex_file:

    def __init__(self):
        self.magic = ''
        self.size = 0
        self.dummy_0 = 0 #uint32, dummy? 0x43444344
        self.dummy_1 = 0 #uint32, dummy? 0x43444344
        self.dummy_2 = 0 #uint32, dummy? 0x43444344
        self.dummy_3 = 0 #uint32, dummy? 0x43444344
        self.dummy_4 = 0 #uint32, dummy? 0x43444344
        self.dummy_5 = 0 #uint32, dummy? 0x43444344

    def read(self, file, offset):
        file.seek(offset)
