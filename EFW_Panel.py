import bpy


class EFW_PT_Panel(bpy.types.Panel):
    bl_idname = "Export_For_Web"
    bl_label = "Export For Web"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "EFB"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.show_face_orientation", text="show face orientation")
        layout.operator("object.show_normals", text="show normals")
        layout.operator("object.recalculate_outside", text="recalculate outside normals")
        layout.operator("object.recalculate_inside", text="recalculate inside normals")
        layout.operator("efw.smart_uv", text="UV unwrap")

class EFW_PT_Menu(bpy.types.Panel):
    bl_idname = "texture_selection"
    bl_label = "Choose the texture to Bake"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "EFB"

    def draw(self, context):
        layout = self.layout

        layout.operator("wm.options_for_bake", text="bake textures from")
        