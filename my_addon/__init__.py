""" My Addon, a Blender addon """

import bpy
from bpy.props import (PointerProperty)

from .operators import MyAddon_OT_my_operator
from .panels import MyAddon_PT_my_panel
from .props import MyAddon_Props

bl_info = {
    'name': 'My Addon',
    'author': 'Daniel Toplak',
    'version': (1, 0, 0),
    'blender': (2, 93, 0),
    'category': 'Object',
}


# ------------------------------------------------------
# Registration
# ------------------------------------------------------
classes = (
    MyAddon_OT_my_operator,
    MyAddon_PT_my_panel,
    MyAddon_Props,
)


def register():
    """register the classes"""
    print("register...")
    for cls in classes:
        print("register class: " + cls.__name__)
        bpy.utils.register_class(cls)

    # pylint: disable=assignment-from-no-return
    bpy.types.Scene.my_addon = PointerProperty(type=MyAddon_Props)


def unregister():
    """unregister the classes"""
    print("unregister ...")
    for cls in reversed(classes):
        print("unregister class: " + cls.__name__)
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.my_addon


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
