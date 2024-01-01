import bpy

class SetSceneFromClipPanel(bpy.types.Panel):
    bl_label = "Set scene from clip"
    bl_idname = "OBJECT_PT_set_scene_from_clip"
    bl_space_type = 'CLIP_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Footage"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        if not context.edit_movieclip:
            layout.label(text="No clip selected")
            return
        
        # checkbox
        layout.prop(scene, "SSFC_change_res")
        layout.prop(scene, "SSFC_change_range")

        # framerate
        layout.prop(scene, "SSFC_framerate")

        # button
        layout.operator("scene.set_scene_from_clip_operator")

def register():
    bpy.utils.register_class(SetSceneFromClipPanel)

def unregister():
    bpy.utils.unregister_class(SetSceneFromClipPanel)