""" My Addon operators """

import bpy
from bpy.types import Operator


class MyAddon_OT_my_operator(Operator):
    # pylint: disable=invalid-name
    """ My Addon operator"""
    bl_idname = "myaddon.create"
    bl_label = "Create mesh"
    bl_description = "Create a selected mesh"

    def execute(self, context):
        scene = context.scene
        my_addon = scene.my_addon

        print("mesh type: {}".format(my_addon.mesh_type))
        print("at cursor: {}".format(my_addon.at_3d_cursor))

        loc = (0, 0, 0)
        if my_addon.at_3d_cursor is True:
            loc = bpy.context.scene.cursor.location

        if my_addon.mesh_type == '0':
            # create cube
            bpy.ops.mesh.primitive_cube_add(align='WORLD', location=loc)
        elif my_addon.mesh_type == '1':
            # create sphere
            bpy.ops.mesh.primitive_uv_sphere_add(align='WORLD', location=loc)
        elif my_addon.mesh_type == '2':
            # create Monkey
            bpy.ops.mesh.primitive_monkey_add(align='WORLD', location=loc)
        else:
            print("wrong mesh type!")

        return {'FINISHED'}
