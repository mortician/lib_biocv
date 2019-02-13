########################################################################################################################
# IO_RDX - BIOHAZARD CODE VERONICA X BLENDER IMPORT ADDON
#=======================================================================================================================
# 2015, 2019 MORTICIAN (THE_MORTICIAN@HOTMAIL.DE)
########################################################################################################################
import bpy
import imp
import lib_biocv.lib_rdx as lib_rdx

imp.reload(lib_rdx)

def fix_id(id):
    return "{0:0>2}".format(id)

def import_data_2(data):
    if len(data.object) != 0:
        for i in range(len(data.object)):

            obj = data.object[i]
            empty = bpy.data.objects.new('DATA_2_' + fix_id(i) + '_XYZ', None)
            bpy.context.scene.objects.link(empty)
            empty.location = (obj.x, -obj.z, obj.y)

            empty.select = True
            #bpy.data.objects['AOT_' + fix_id(i)]['Id'] = obj.id
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag1'] = unk1
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag2'] = unk2
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag3'] = unk3
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag4'] = unk4

            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.move_to_layer(layers=(False, False, True, False, False, False, False, False, False, False,
                                                 False, False, False, False, False, False, False, False, False, False))
            empty.select = False
            bpy.context.scene.update()
def import_obj(data):
    if len(data.object) != 0:
        for i in range(len(data.object)):

            obj = data.object[i]
            empty = bpy.data.objects.new('OBJ_' + fix_id(i) + '_XYZ', None)
            bpy.context.scene.objects.link(empty)
            empty.location = (obj.x, -obj.z, obj.y)

            empty.select = True
            #bpy.data.objects['AOT_' + fix_id(i)]['Id'] = obj.id
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag1'] = unk1
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag2'] = unk2
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag3'] = unk3
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag4'] = unk4

            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.move_to_layer(layers=(False, False, False, True, False, False, False, False, False, False,
                                                 False, False, False, False, False, False, False, False, False, False))
            empty.select = False
            bpy.context.scene.update()
def import_data_4(data):
    if len(data.object) != 0:
        for i in range(len(data.object)):

            obj = data.object[i]
            empty = bpy.data.objects.new('DATA_4_' + fix_id(i) + '_XYZ', None)
            bpy.context.scene.objects.link(empty)
            empty.location = (obj.x, -obj.z, obj.y)

            empty.select = True
            #bpy.data.objects['AOT_' + fix_id(i)]['Id'] = obj.id
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag1'] = unk1
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag2'] = unk2
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag3'] = unk3
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag4'] = unk4

            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.move_to_layer(layers=(False, False, False, False, True, False, False, False, False, False,
                                                 False, False, False, False, False, False, False, False, False, False))
            empty.select = False
            bpy.context.scene.update()
def import_data_5(data):
    if len(data.object) != 0:
        for i in range(len(data.object)):

            obj = data.object[i]
            verts = [(obj.x, -obj.z, obj.y),
                     (obj.x + obj.width, -obj.z, obj.y),
                     (obj.x + obj.width, -obj.z - obj.density, obj.y),
                     (obj.x, -obj.z - obj.density, obj.y),
                     (obj.x, -obj.z, obj.height),
                     (obj.x + obj.width, -obj.z, obj.height),
                     (obj.x + obj.width, -obj.z - obj.density, obj.height),
                     (obj.x, -obj.z - obj.density, obj.height)]

            faces = [(0, 1, 2, 3),
                     (0, 4, 5, 1),
                     (0, 3, 7, 4),
                     (2, 3, 7, 6),
                     (4, 5, 6, 7),
                     (1, 2, 6, 5)]

            mesh = bpy.data.meshes.new('DATA_5_' + fix_id(i) + '_MESH')
            aot_ob = bpy.data.objects.new('DATA_5_' + fix_id(i), mesh)
            bpy.context.scene.objects.link(aot_ob)
            mesh.from_pydata(verts, [], faces)
            mesh.update()

            aot_ob.select = True
            #bpy.data.objects['AOT_' + fix_id(i)]['Id'] = obj.id
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag1'] = unk1
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag2'] = unk2
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag3'] = unk3
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag4'] = unk4

            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.move_to_layer(layers=(False, False, False, False, False, True, False, False, False, False,
                                                 False, False, False, False, False, False, False, False, False, False))
            aot_ob.select = False
            bpy.context.scene.update()
def import_sca(data):
    if len(data.object) != 0:
        for i in range(len(data.object)):

            obj = data.object[i]
            verts = [(obj.x, -obj.z, obj.y),
                     (obj.x + obj.width, -obj.z, obj.y),
                     (obj.x + obj.width, -obj.z - obj.density, obj.y),
                     (obj.x, -obj.z - obj.density, obj.y),
                     (obj.x, -obj.z, obj.height),
                     (obj.x + obj.width, -obj.z, obj.height),
                     (obj.x + obj.width, -obj.z - obj.density, obj.height),
                     (obj.x, -obj.z - obj.density, obj.height)]

            faces = [(0, 1, 2, 3),
                     (0, 4, 5, 1),
                     (0, 3, 7, 4),
                     (2, 3, 7, 6),
                     (4, 5, 6, 7),
                     (1, 2, 6, 5)]

            mesh = bpy.data.meshes.new('SCA_' + fix_id(i) + '_MESH')
            sca_ob = bpy.data.objects.new('SCA_' + fix_id(i), mesh)
            bpy.context.scene.objects.link(sca_ob)
            mesh.from_pydata(verts, [], faces)
            mesh.update()

            sca_ob.select = True
            #bpy.data.objects['AOT_' + fix_id(i)]['Id'] = obj.id
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag1'] = unk1
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag2'] = unk2
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag3'] = unk3
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag4'] = unk4

            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.move_to_layer(layers=(False, False, False, False, False, False, True, False, False, False,
                                                 False, False, False, False, False, False, False, False, False, False))
            sca_ob.select = False
            bpy.context.scene.update()
def import_aot(data):
    if len(data.object) != 0:
        for i in range(len(data.object)):

            obj = data.object[i]
            verts = [(obj.x, -obj.z, obj.y),
                     (obj.x + obj.width, -obj.z, obj.y),
                     (obj.x + obj.width, -obj.z - obj.density, obj.y),
                     (obj.x, -obj.z - obj.density, obj.y),
                     (obj.x, -obj.z, obj.height),
                     (obj.x + obj.width, -obj.z, obj.height),
                     (obj.x + obj.width, -obj.z - obj.density, obj.height),
                     (obj.x, -obj.z - obj.density, obj.height)]
      
            faces = [(0, 1, 2, 3),
                     (0, 4, 5, 1),
                     (0, 3, 7, 4),
                     (2, 3, 7, 6),
                     (4, 5, 6, 7),
                     (1, 2, 6, 5)]
    
            mesh = bpy.data.meshes.new('AOT_' + fix_id(i) + '_MESH')
            aot_ob = bpy.data.objects.new('AOT_' + fix_id(i), mesh)
            bpy.context.scene.objects.link(aot_ob)
            mesh.from_pydata(verts, [], faces)
            mesh.update()

            aot_ob.select = True
            #bpy.data.objects['AOT_' + fix_id(i)]['Id'] = obj.id
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag1'] = unk1
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag2'] = unk2
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag3'] = unk3
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag4'] = unk4

            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.move_to_layer(layers=(False, False, False, False, False, False, False, True, False, False,
                                                 False, False, False, False, False, False, False, False, False, False))
            aot_ob.select = False
            bpy.context.scene.update()
def import_data_8(data):
    if len(data.object) != 0:
        for i in range(len(data.object)):

            obj = data.object[i]
            verts = [(obj.x, -obj.z, obj.y),
                     (obj.x + obj.width, -obj.z, obj.y),
                     (obj.x + obj.width, -obj.z - obj.density, obj.y),
                     (obj.x, -obj.z - obj.density, obj.y),
                     (obj.x, -obj.z, obj.height),
                     (obj.x + obj.width, -obj.z, obj.height),
                     (obj.x + obj.width, -obj.z - obj.density, obj.height),
                     (obj.x, -obj.z - obj.density, obj.height)]

            faces = [(0, 1, 2, 3),
                     (0, 4, 5, 1),
                     (0, 3, 7, 4),
                     (2, 3, 7, 6),
                     (4, 5, 6, 7),
                     (1, 2, 6, 5)]

            mesh = bpy.data.meshes.new('DATA_8_' + fix_id(i) + '_MESH')
            aot_ob = bpy.data.objects.new('DATA_8_' + fix_id(i), mesh)
            bpy.context.scene.objects.link(aot_ob)
            mesh.from_pydata(verts, [], faces)
            mesh.update()

            aot_ob.select = True
            #bpy.data.objects['AOT_' + fix_id(i)]['Id'] = obj.id
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag1'] = unk1
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag2'] = unk2
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag3'] = unk3
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag4'] = unk4

            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.move_to_layer(layers=(False, False, False, False, False, False, False, False, True, False,
                                                 False, False, False, False, False, False, False, False, False, False))
            aot_ob.select = False
            bpy.context.scene.update()
def import_player_positions(data):
    if len(data.object) != 0:
        for i in range(len(data.object)):

            obj = data.object[i]
            empty = bpy.data.objects.new('PLAYER_POSITION_' + fix_id(i) + '_XYZ', None)
            bpy.context.scene.objects.link(empty)
            empty.location = (obj.x, -obj.z, obj.y)

            empty.select = True
            #bpy.data.objects['AOT_' + fix_id(i)]['Id'] = obj.id
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag1'] = unk1
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag2'] = unk2
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag3'] = unk3
            #bpy.data.objects['AOT_' + fix_id(i)]['Flag4'] = unk4

            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.move_to_layer(layers=(False, False, False, False, False, False, False, False, False, True,
                                                 False, False, False, False, False, False, False, False, False, False))
            empty.select = False
            bpy.context.scene.update()

def import_file(context, filepath):
    print('\n' + ("=" * 64))
    print("BIOHAZARD CODE VERONICA X .RDX FILE IMPORT")
    print("=" * 64)
    print("\t2015, MORTICIAN (THE_MORTICIAN@HOTMAIL.DE)")
    print(("=" * 64) + '\n')
    print('IMPORTING FILE: ' + filepath)
    
    global tmp_rdx
    tmp_rdx = lib_rdx.rdx_file()
    tmp_rdx = lib_rdx.rdx_file.read(tmp_rdx, filepath)

    import_data_2(tmp_rdx.data_2)
    import_obj(tmp_rdx.obj)
    import_data_4(tmp_rdx.data_4)
    import_data_5(tmp_rdx.data_5)
    import_aot(tmp_rdx.aot)
    import_sca(tmp_rdx.sca)

    for i in range(len(tmp_rdx.sca.object)):
        print(str(i) + ':\t' + str(tmp_rdx.sca.object[i].tag) + ', ' + str(tmp_rdx.sca.object[i].id) + ', '
              + str(tmp_rdx.sca.object[i].unknown_0) + ', ' + str(tmp_rdx.sca.object[i].unknown_1) + ', '
              + str(tmp_rdx.sca.object[i].unknown_2) + ', ' + str(tmp_rdx.sca.object[i].unknown_3) + ', '
              + str(tmp_rdx.sca.object[i].unknown_4) + ', ' + str(tmp_rdx.sca.object[i].unknown_5) + ', ')

    tmp_rdx.sca.extract('d:/testnow.sca')
    tmp_rdx.aot.extract('d:/testnow.aot')
    import_data_8(tmp_rdx.data_8)
    import_player_positions(tmp_rdx.player_positions)



    return {'FINISHED'}

from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator

class rdx_importer(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "recv_tools.rdx_import"  # important since its how bpy.ops.recv_tools.rdx_import is constructed
    bl_label = "Import RDX"

    filename_ext = ".rdx"

    filter_glob = StringProperty(
            default="*.rdx",
            options={'HIDDEN'},
            )

    opt_cam = BoolProperty(
            name="00 - CAM",
            description="Import cameras",
            default=False,
            )
    opt_lit = BoolProperty(
            name="01 - LIT",
            description="Import lights",
            default=False,
            )
    opt_data_2 = BoolProperty(
            name="02 - DATA_2",
            description="Import ???",
            default=False,
            )
    opt_obj = BoolProperty(
            name="03 - OBJ?",
            description="Import object positions",
            default=False,
            )
    opt_data_4 = BoolProperty(
            name="04 - DATA_4",
            description="Import lights",
            default=False,
            )
    opt_data_5 = BoolProperty(
            name="05 - DATA_5",
            description="Import ???",
            default=False,
            )
    def execute(self, context):
        return import_file(context, self.filepath)


# Only needed if you want to add into a dynamic menu
def menu_func_import(self, context):
    self.layout.operator(rdx_importer.bl_idname, text="Text Import Operator")


def register():
    bpy.utils.register_class(rdx_importer)
    bpy.types.INFO_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(rdx_importer)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.recv_tools.rdx_import('INVOKE_DEFAULT')
