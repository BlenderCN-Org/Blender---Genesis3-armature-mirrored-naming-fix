bl_info = {"name": "Fix Daz3D Genesis3 Armature Naming", "category": "Rigging"}

import bpy

class Fix_Genesis3_Armature_Names(bpy.types.Operator):
    bl_idname = "object.mirror_armature"
    bl_label = "Fix Genesis Armature Names"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent = bpy.context.active_pose_bone
        for b in [parent]+parent.children_recursive:
            if b.name[0] == 'l':
                new_name = b.name[1:] + ".l"
                b.name = new_name
            elif b.name[0] == 'r':
                new_name = b.name[1:] + ".r"
                b.name = new_name
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(Fix_Genesis3_Armature_Names)

def unregister():
    bpy.utils.unregister_class(Fix_Genesis3_Armature_Names)

if __name__ == "__main__":
    register()