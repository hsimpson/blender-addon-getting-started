""" Addon panel """

from bpy.types import (Panel)


class MyAddon_PT_my_panel(Panel):
    # pylint: disable=invalid-name
    """My Addon panel"""
    bl_idname = "CREATE_MESH_PT_main"
    bl_label = "Create mesh addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My Addon"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        my_addon = scene.my_addon

        row = layout.row(align=True)
        row.prop(my_addon, "mesh_type")

        row = layout.row(align=True)
        row.prop(my_addon, "at_3d_cursor")

        layout.operator("myaddon.create")
