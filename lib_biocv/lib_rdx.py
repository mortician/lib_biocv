########################################################################################################################
# LIB_BIOCV.LIB_RDX - BIOHAZARD CODE VERONICA X ROOM DATA
#=======================================================================================================================
# 2015, 2019 MORTICIAN (THE_MORTICIAN@HOTMAIL.DE)
########################################################################################################################
import struct

class rdx_sca_object:
    def __init__(self):
        self.tag = 0        #byte?,
        self.id = 0         #byte?,
        self.unknown_0 = 0  #uint16,
        self.unknown_1 = 0  #uint32,
        self.x = 0          #float,
        self.y = 0          #float,
        self.z = 0          #float,
        self.width = 0      #float,
        self.height = 0     #float,
        self.density = 0    #float,
        self.unknown_2 = 0  #byte?,
        self.unknown_3 = 0  #byte?,
        self.unknown_4 = 0  #byte?,
        self.unknown_5 = 0  #byte?,
    def read(self, file):
        self.tag = int(struct.unpack("B", file.read(1))[0])
        self.id = int(struct.unpack("B", file.read(1))[0])
        self.unknown_0 = int(struct.unpack("H", file.read(2))[0])
        self.unknown_1 = int(struct.unpack("L", file.read(4))[0])
        self.x = float(struct.unpack("f", file.read(4))[0])
        self.y = float(struct.unpack("f", file.read(4))[0])
        self.z = float(struct.unpack("f", file.read(4))[0])
        self.width = float(struct.unpack("f", file.read(4))[0])
        self.height = float(struct.unpack("f", file.read(4))[0])
        self.density = float(struct.unpack("f", file.read(4))[0])
        self.unknown_2 = int(struct.unpack("B", file.read(1))[0])
        self.unknown_3 = int(struct.unpack("B", file.read(1))[0])
        self.unknown_4 = int(struct.unpack("B", file.read(1))[0])
        self.unknown_5 = int(struct.unpack("B", file.read(1))[0])

        return self
    def write(self, file):
        file.write(struct.pack('B', int(self.tag)))
        file.write(struct.pack('B', int(self.id)))
        file.write(struct.pack('H', int(self.unknown_0)))
        file.write(struct.pack('L', int(self.unknown_1)))
        file.write(struct.pack('f', int(self.x)))
        file.write(struct.pack('f', int(self.y)))
        file.write(struct.pack('f', int(self.z)))
        file.write(struct.pack('f', int(self.width)))
        file.write(struct.pack('f', int(self.height)))
        file.write(struct.pack('f', int(self.density)))
        file.write(struct.pack('B', int(self.unknown_2)))
        file.write(struct.pack('B', int(self.unknown_3)))
        file.write(struct.pack('B', int(self.unknown_4)))
        file.write(struct.pack('B', int(self.unknown_5)))

class rdx_sca_data:
    def __init__(self):
        self.object = []
    def read(self, file, offset, count):
        self.object = []
        file.seek(offset)

        for i in range(count):
            tmp_obj = rdx_sca_object()
            tmp_obj = rdx_sca_object.read(tmp_obj, file)
            self.object.append(tmp_obj)

        return self
    def write(self, file, offset):
        file.seek(offset)

        for i in range(len(self.object)):
            self.object[i].write(file)
    def extract(self, filepath):
        file = open(filepath, 'wb')
        self.write(file, 0)
        file.close()

class rdx_aot_data:
    def __init__(self):
        self.object = []
    def read(self, file, offset, count):
        self.object = []
        file.seek(offset)

        for i in range(count):
            tmp_obj = rdx_sca_object()
            tmp_obj = rdx_sca_object.read(tmp_obj, file)
            self.object.append(tmp_obj)

        return self
    def write(self, file, offset):
        file.seek(offset)

        for i in range(len(self.object)):
            self.object[i].write(file)
    def extract(self, filepath):
        file = open(filepath, 'wb')
        self.write(file, 0)
        file.close()

class rdx_data_2_object:
    def __init__(self):
        self.tag = 0        #uint32?,
        self.id = 0         #uint32?,
        self.unknown_0 = 0  #uint32?,
        self.x = 0          #float,
        self.y = 0          #float,
        self.z = 0          #float,
        self.unknown_1 = 0  #uint32?,
        self.unknown_2 = 0  #uint32?,
        self.unknown_3 = 0  #uint32?,

    def read(self, file):
        self.tag = int(struct.unpack("L", file.read(4))[0])
        self.id = int(struct.unpack("L", file.read(4))[0])
        self.unknown_0 = int(struct.unpack("L", file.read(4))[0])
        self.x = float(struct.unpack("f", file.read(4))[0])
        self.y = float(struct.unpack("f", file.read(4))[0])
        self.z = float(struct.unpack("f", file.read(4))[0])
        self.unknown_1 = int(struct.unpack("L", file.read(4))[0])
        self.unknown_2 = int(struct.unpack("L", file.read(4))[0])
        self.unknown_3 = int(struct.unpack("L", file.read(4))[0])

        return self
class rdx_data_2:
    def __init__(self):
        self.object = []
    def read(self, file, offset, count):
        self.object = []
        file.seek(offset)

        for i in range(count):
            tmp_obj = rdx_data_2_object()
            tmp_obj = rdx_data_2_object.read(tmp_obj, file)
            self.object.append(tmp_obj)

        return self
class rdx_obj_object:
    def __init__(self):
        self.tag = 0        #uint32?,
        self.id = 0         #uint32?,
        self.unknown_0 = 0  #uint32?,
        self.x = 0          #float,
        self.y = 0          #float,
        self.z = 0          #float,
        self.unknown_1 = 0  #float?,
        self.unknown_2 = 0  #uint32?,
        self.unknown_3 = 0  #uint32?,

    def read(self, file):
        self.tag = int(struct.unpack("L", file.read(4))[0])
        self.id = int(struct.unpack("L", file.read(4))[0])
        self.unknown_0 = int(struct.unpack("L", file.read(4))[0])
        self.x = float(struct.unpack("f", file.read(4))[0])
        self.y = float(struct.unpack("f", file.read(4))[0])
        self.z = float(struct.unpack("f", file.read(4))[0])
        self.unknown_1 = float(struct.unpack("f", file.read(4))[0])
        self.unknown_2 = int(struct.unpack("L", file.read(4))[0])
        self.unknown_3 = int(struct.unpack("L", file.read(4))[0])

        return self
class rdx_obj_data:
    def __init__(self):
        self.object = []
    def read(self, file, offset, count):
        self.object = []
        file.seek(offset)

        for i in range(count):
            tmp_obj = rdx_obj_object()
            tmp_obj = rdx_obj_object.read(tmp_obj, file)
            self.object.append(tmp_obj)

        return self

class rdx_data_4: #using same as data_2?
    def __init__(self):
        self.object = []
    def read(self, file, offset, count):
        self.object = []
        file.seek(offset)

        for i in range(count):
            tmp_obj = rdx_data_2_object()
            tmp_obj = rdx_data_2_object.read(tmp_obj, file)
            self.object.append(tmp_obj)

        return self

class rdx_data_5_object:
    def __init__(self):
        self.tag = 0        #uint32?,
        self.id = 0         #uint16?,
        self.unknown_0 = 0  #uint16?;
        self.unknown_1 = 0  #uint32?,
        self.x = 0          #float,
        self.y = 0          #float,
        self.z = 0          #float,
        self.width = 0      #float,
        self.height = 0     #float,
        self.density = 0    #float,
        self.unknown_2 = 0  #uint32?,
        self.unknown_3 = 0  #uint32?,
        self.unknown_4 = 0  #uint32?,
        self.unknown_5 = 0  #uint32?,
        self.unknown_6 = 0  #uint32?,
        self.unknown_7 = 0  #uint32?,
        self.unknown_8 = 0  #uint32?,
        self.unknown_9 = 0  #uint32?,

    def read(self, file):
        self.tag = int(struct.unpack("L", file.read(4))[0])
        self.id = int(struct.unpack("H", file.read(2))[0])
        self.unknown_0 = int(struct.unpack("H", file.read(2))[0])
        self.unknown_0 = int(struct.unpack("L", file.read(4))[0])
        self.x = float(struct.unpack("f", file.read(4))[0])
        self.y = float(struct.unpack("f", file.read(4))[0])
        self.z = float(struct.unpack("f", file.read(4))[0])
        self.width = float(struct.unpack("f", file.read(4))[0])
        self.height = float(struct.unpack("f", file.read(4))[0])
        self.density = float(struct.unpack("f", file.read(4))[0])
        self.unknown_2 = int(struct.unpack("L", file.read(4))[0])
        self.unknown_3 = int(struct.unpack("L", file.read(4))[0])
        self.unknown_4 = int(struct.unpack("L", file.read(4))[0])
        self.unknown_5 = int(struct.unpack("L", file.read(4))[0])
        self.unknown_6 = int(struct.unpack("L", file.read(4))[0])
        self.unknown_7 = int(struct.unpack("L", file.read(4))[0])
        self.unknown_8 = int(struct.unpack("L", file.read(4))[0])
        self.unknown_9 = int(struct.unpack("L", file.read(4))[0])

        return self
class rdx_data_5:
    def __init__(self):
        self.object = []
    def read(self, file, offset, count):
        self.object = []
        file.seek(offset)

        for i in range(count):
            tmp_obj = rdx_data_5_object()
            tmp_obj = rdx_data_5_object.read(tmp_obj, file)
            self.object.append(tmp_obj)

        return self

class rdx_data_8:
    def __init__(self):
        self.object = []
    def read(self, file, offset, count):
        self.object = []
        file.seek(offset)

        for i in range(count):
            tmp_obj = rdx_sca_object()
            tmp_obj = rdx_sca_object.read(tmp_obj, file)
            self.object.append(tmp_obj)

        return self

class rdx_player_position_object:
    def __init__(self):
        self.x = 0          #float,
        self.y = 0          #float,
        self.z = 0          #float,
        self.rotation = 0   #int32?,

    def read(self, file):
        self.x = float(struct.unpack("f", file.read(4))[0])
        self.y = float(struct.unpack("f", file.read(4))[0])
        self.z = float(struct.unpack("f", file.read(4))[0])
        self.rotation = int(struct.unpack("L", file.read(4))[0])

        return self
class rdx_player_position_data:
    def __init__(self):
        self.object = []
    def read(self, file, offset, count):
        self.object = []
        file.seek(offset)

        for i in range(count):
            tmp_obj = rdx_player_position_object()
            tmp_obj = rdx_player_position_object.read(tmp_obj, file)
            self.object.append(tmp_obj)

        return self

class rdx_header:
    def __init__(self):
        self.tag = 0            #uint32, can be (0x00002041 = 1092616192) or (0xB81E0540 = 1074077368)
        self.dummy_0 = 0        #uint32,
        self.dummy_1 = 0        #uint32,
        self.dummy_2 = 0        #uint32,
        self.o_sub_header = 0   #uint32, points to subheader...
        self.o_mdl = 0          #uint32, points to model table...
        self.o_mtn = 0          #uint32, points to MTN (motion?) table...
        self.o_unknown = 0      #uint32, points to unknown offset table, maybe SCD?
        self.o_tex = 0          #uint32, points to texture offset table...

        self.author = ''        #string, name of file author, whole section is always 32 bytes in size

        self.o_cam = 0          #uint32,
        self.o_lit = 0          #uint32,
        self.o_data_2 = 0        #uint32,
        self.o_obj = 0          #uint32,
        self.o_data_4 = 0        #uint32,
        self.o_data_5 = 0        #uint32,
        self.o_sca = 0          #uint32,
        self.o_aot = 0          #uint32,
        self.o_data_8 = 0        #uint32,
        self.o_player_positions = 0 #uint32,
        self.o_data_10 = 0        #uint32,
        self.o_data_11 = 0    #uint32,
        self.o_data_12 = 0    #uint32,
        self.o_data_13 = 0    #uint32,
        self.o_data_14 = 0    #uint32,
        self.o_txt = 0          #uint32,
                                #64 byte gap, probably dummy data due to some data alignment...
        self.c_cam = 0          #uint32,
        self.c_lit = 0          #uint32,
        self.c_data_2 = 0        #uint32,
        self.c_obj = 0          #uint32,
        self.c_data_4 = 0    #uint32,
        self.c_data_5 = 0    #uint32,
        self.c_sca = 0          #uint32,
        self.c_aot = 0          #uint32,
        self.c_data_8 = 0    #uint32,
        self.c_player_positions = 0        #uint32,
        self.c_data_10 = 0    #uint32,
        self.c_data_11 = 0    #uint32,
        self.c_data_12 = 0    #uint32,
        self.c_data_13 = 0    #uint32,
        self.c_data_14 = 0          #uint32,
        self.c_data_15 = 0    #uint32,
        #64 byte gap, probably dummy data due to some data alignment...

    def read(self, file):
        file.seek(0)
        self.tag = int(struct.unpack("L", file.read(4))[0])
        self.dummy_0 = int(struct.unpack("L", file.read(4))[0])
        self.dummy_1 = int(struct.unpack("L", file.read(4))[0])
        self.dummy_2 = int(struct.unpack("L", file.read(4))[0])
        self.o_sub_header = int(struct.unpack("L", file.read(4))[0])
        self.o_mdl = int(struct.unpack("L", file.read(4))[0])
        self.o_mtn = int(struct.unpack("L", file.read(4))[0])
        self.o_unknown = int(struct.unpack("L", file.read(4))[0])
        self.o_tex = int(struct.unpack("L", file.read(4))[0])

        file.seek(96)
        self.author = bytes(struct.unpack("32B", file.read(32))).decode('ascii')
        self.o_cam = int(struct.unpack("L", file.read(4))[0])
        self.o_lit = int(struct.unpack("L", file.read(4))[0])
        self.o_data_2 = int(struct.unpack("L", file.read(4))[0])
        self.o_obj = int(struct.unpack("L", file.read(4))[0])
        self.o_data_4 = int(struct.unpack("L", file.read(4))[0])
        self.o_data_5 = int(struct.unpack("L", file.read(4))[0])
        self.o_sca = int(struct.unpack("L", file.read(4))[0])
        self.o_aot = int(struct.unpack("L", file.read(4))[0])
        self.o_data_8 = int(struct.unpack("L", file.read(4))[0])
        self.o_player_positions = int(struct.unpack("L", file.read(4))[0])
        self.o_data_10 = int(struct.unpack("L", file.read(4))[0])
        self.o_data_11 = int(struct.unpack("L", file.read(4))[0])
        self.o_data_12 = int(struct.unpack("L", file.read(4))[0])
        self.o_data_13 = int(struct.unpack("L", file.read(4))[0])
        self.o_data_14 = int(struct.unpack("L", file.read(4))[0])
        self.o_txt = int(struct.unpack("L", file.read(4))[0])

        file.seek(256)
        self.c_cam = int(struct.unpack("L", file.read(4))[0])
        self.c_lit = int(struct.unpack("L", file.read(4))[0])
        self.c_data_2 = int(struct.unpack("L", file.read(4))[0])
        self.c_obj = int(struct.unpack("L", file.read(4))[0])
        self.c_data_4 = int(struct.unpack("L", file.read(4))[0])
        self.c_data_5 = int(struct.unpack("L", file.read(4))[0])
        self.c_sca = int(struct.unpack("L", file.read(4))[0])
        self.c_aot = int(struct.unpack("L", file.read(4))[0])
        self.c_data_8 = int(struct.unpack("L", file.read(4))[0])
        self.c_player_positions = int(struct.unpack("L", file.read(4))[0])
        self.c_data_10 = int(struct.unpack("L", file.read(4))[0])
        self.c_data_11 = int(struct.unpack("L", file.read(4))[0])
        self.c_data_12 = int(struct.unpack("L", file.read(4))[0])
        self.c_data_13 = int(struct.unpack("L", file.read(4))[0])
        self.c_data_14 = int(struct.unpack("L", file.read(4))[0])
        self.c_data_15 = int(struct.unpack("L", file.read(4))[0])

        return self

class rdx_file:
    def __init__(self):
        self.header = rdx_header()
        self.data_2 = rdx_data_2()
        self.obj = rdx_obj_data()
        self.data_4 = rdx_data_4()
        self.data_5 = rdx_data_5()
        self.sca = rdx_sca_data()
        self.aot = rdx_aot_data()
        self.data_8 = rdx_data_8()
        self.player_positions = rdx_player_position_data()

    def read(self, filepath):
        file = open(filepath, 'rb')

        self.header = rdx_header.read(self.header, file)
        #CAM?
        #LIT?
        self.data_2 = rdx_data_2.read(self.data_2, file, self.header.o_data_2, self.header.c_data_2)        #02
        self.obj = rdx_obj_data.read(self.obj, file, self.header.o_obj, self.header.c_obj)                  #03
        self.data_4 = rdx_data_4.read(self.data_4, file, self.header.o_data_4, self.header.c_data_4)        #04
        self.data_5 = rdx_data_5.read(self.data_5, file, self.header.o_data_5, self.header.c_data_5)        #05
        self.sca = rdx_sca_data.read(self.sca, file, self.header.o_sca, self.header.c_sca)                  #06
        self.aot = rdx_aot_data.read(self.aot, file, self.header.o_aot, self.header.c_aot)                  #07
        self.data_8 = rdx_data_8.read(self.data_8, file, self.header.o_data_8, self.header.c_data_8)        #06
        self.player_positions = rdx_player_position_data.read(self.player_positions, file,
                                                              self.header.o_player_positions,
                                                              self.header.c_player_positions)               #09
        file.close()

        return self

