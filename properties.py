import bpy

def register():
    bpy.types.Scene.SSFC_change_res = bpy.props.BoolProperty(name="Change resolution", default=True)

    # bool - change timeline range
    bpy.types.Scene.SSFC_change_range = bpy.props.BoolProperty(name="Change timeline range", default=True)

    # int - framerate
    bpy.types.Scene.SSFC_framerate = bpy.props.IntProperty(name="Framerate", default=25, min=1, max=120)

def unregister():
    del bpy.types.Scene.SSFC_change_res
    del bpy.types.Scene.SSFC_change_range
    del bpy.types.Scene.SSFC_framerate