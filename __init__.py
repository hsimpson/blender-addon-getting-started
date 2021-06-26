# pylint: disable=import-self
""" My Addon, a Blender addon """

import bpy
from bpy.types import (Operator, Panel, PropertyGroup)
from bpy.props import (PointerProperty)
from . import MyAddon_Props
from . import MyAddon_PT_my_panel
from . import MyAddon_OT_my_operator


bl_info = {
    "name": "My Addon",
    "author": "Daniel Toplak",
    "version": (1, 0, 0),
    "blender": (2, 93, 0),
    "category": "Object",
}


# ------------------------------------------------------
# Registration
# ------------------------------------------------------
classes = (
    MyAddon_OT_my_operator,
    MyAddon_PT_my_panel,
    MyAddon_Props
)


def register():
    # pylint: disable=assignment-from-no-return
    """register the classes"""
    
    print("register My Addon")
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.my_addon = PointerProperty(type=MyAddon_Props)


def unregister():
    """unregister the classes"""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.my_addon


if __name__ == "__main__":
    register()
