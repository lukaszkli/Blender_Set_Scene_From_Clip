bl_info = {
    "name": "Set scene from clip",
    "blender": (4, 0, 0),
    "author": "Lukasz Klimkiewicz",
    "description": "Sets scene parameters from clip",
    "version": (0, 0, 1)
}

def register():
    from . import properties
    properties.register()

    from . import operators
    operators.register()

    from . import panels
    panels.register()


def unregister():
    from . import properties
    properties.unregister()

    from . import operators
    operators.unregister()

    from . import panels
    panels.unregister()