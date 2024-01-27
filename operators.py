import bpy

class SetSceneFromClipOperator(bpy.types.Operator):
    bl_idname = "scene.set_scene_from_clip_operator"
    bl_label = "Set scene from clip"

    def execute(self, context):
        scene = context.scene
        pass

        # clip from movie clip editor, not sequencer
        clip = context.edit_movieclip

        # set resolution
        if scene.SSFC_change_res:
            scene.render.resolution_x = clip.size[0]
            scene.render.resolution_y = clip.size[1]

        # set timeline range
        if scene.SSFC_change_range:
            scene.frame_start = clip.frame_start
            scene.frame_end = clip.frame_start + clip.frame_duration - 1

        # set framerate
        scene.render.fps = scene.SSFC_framerate


        return {'FINISHED'}

def register():
    bpy.utils.register_class(SetSceneFromClipOperator)

def unregister():
    bpy.utils.unregister_class(SetSceneFromClipOperator)
