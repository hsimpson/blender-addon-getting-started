"""Addon properties"""

from bpy.props import (BoolProperty, EnumProperty)
from bpy.types import (PropertyGroup)


class MyAddon_Props(PropertyGroup):
    # pylint: disable=invalid-name
    """Properties class"""
    mesh_type: EnumProperty(
        items=(
            ('0', "Cube", ""),
            ('1', "Sphere", ""),
            ('2', "Monkey", ""),
        ),
        name="Mesh type",
        description="Select the type of mesh"
    )
    at_3d_cursor: BoolProperty(
        name="At 3D cursor",
        description="Create mesh at 3D cursor",
        default=True
    )
