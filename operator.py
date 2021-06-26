""" Addon Operator """

from bpy.types import (Operator)

class MyAddon_OT_my_operator(Operator):
    # pylint: disable=invalid-name
    """My Addon operator"""
    bl_idname = "myaddon.create"
    bl_label = "Create mesh"
    bl_description = "Create a selected mesh"

    def execute(self, context):
        scene = context.scene
        my_addon = scene.my_addon

        print("mesh type: {}".format(my_addon.mesh_type))
        print("at cursor: {}".format(my_addon.at_3d_cursor))

        return {'FINISHED'}
