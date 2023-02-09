import bpy

class EFW_OT_ShowNormals(bpy.types.Operator):
    bl_idname = "object.show_normals"
    bl_label = "Show the normals"
    bl_description = "Displays the normals as blue lines, helps with visualization"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == 'EDIT':
                return True
        return False


    def execute(self, context):
        if bpy.context.space_data.overlay.show_face_normals == True:
            bpy.context.space_data.overlay.show_face_normals = False
        else:
            bpy.context.space_data.overlay.show_face_normals = True



        return {"FINISHED"}

class EFW_OT_RecalculateOutside(bpy.types.Operator):
    bl_idname = "object.recalculate_outside"
    bl_label = "recalculate the outer normals"
    bl_description = "Recalculates the normals for the outer faces"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == 'EDIT':
                return True
        return False


    def execute(self, context):
        bpy.ops.mesh.normals_make_consistent(inside=False)

        return {"FINISHED"}

class EFW_OT_RecalculateInside(bpy.types.Operator):
    bl_idname = "object.recalculate_inside"
    bl_label = "recalculate the inner normals"
    bl_description = "Recalculates the normals for the inner faces"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == 'EDIT':
                return True
        return False


    def execute(self, context):
        bpy.ops.mesh.normals_make_consistent(inside=True)

        return {"FINISHED"}

class EFW_OT_ShowFaceOrientation(bpy.types.Operator):
    bl_idname = "object.show_face_orientation"
    bl_label = "show face orientation"
    bl_description = "shows the face orientation"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        if bpy.context.space_data.overlay.show_face_orientation == False:
            bpy.context.space_data.overlay.show_face_orientation = True
        else:
            bpy.context.space_data.overlay.show_face_orientation = False


        return {"FINISHED"}

class EFW_OT_SmartUV(bpy.types.Operator):
    bl_idname = "efw.smart_uv"
    bl_label = "smart unwraps the UVs"
    bl_description = "automatically unwraps the UVs"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
            

        obj = context.object

        if obj is not None:
            if obj.mode == 'EDIT':
                return True
        return False


    def execute(self, context):
        bpy.ops.uv.smart_project()

        return {"FINISHED"}

class EFW_OT_OptionsForBake(bpy.types.Operator):
    bl_idname = "wm.options_for_bake"
    bl_label = "choose the texture you wish to bake"
    bl_description = "bakes the textures to an image based on your preference"
    bl_options = {"REGISTER"}

    ofb_enum : bpy.props.EnumProperty(
        name= "",
        description= "Select an option",
        items= [
            ('OP1', "Combined", "Bake everything into one image"),
            ('OP2', "Shadow", "Bake the Shadows"),
            ('OP3', "Ambient Occlusion", "Bake the Ambient Occlusion"),
            ('OP4', "Roughness", "Bake the Roughness"),
            ('OP5', "Emission", "Bake the Emission")
        ]

    )

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "ofb_enum")

    def execute(self, context):

        #create new image and save it 
        image = bpy.data.images.new("Bake", alpha=True, width=1024, height=1024)
        image.alpha_mode = 'STRAIGHT'
        image.filepath_raw = "//Bake.png"
        image.file_format = 'PNG'
        image.save()

        #loop inside list of materials from the selected objects
        for object in bpy.context.selected_objects:
            for mat in object.data.materials:
                #activate use of nodes
                mat.use_nodes = True
                nodes = mat.node_tree.nodes
                #create new image texture node
                node = nodes.new('ShaderNodeTexImage')
                #node location in the shader editor
                node.location = (-500,100) 
                #use image in the image node = bpy.data.images
                node.image = bpy.data.images['Bake']
                #set node as active/selected, for baking
                node.select = True

        if self.ofb_enum == 'OP1':
            bpy.ops.object.bake(type="COMBINED")
        if self.ofb_enum == 'OP2':
            bpy.ops.object.bake(type="SHADOW")
        if self.ofb_enum == 'OP3':
            bpy.ops.object.bake(type="AO")
        if self.ofb_enum == 'OP4':
            bpy.ops.object.bake(type="ROUGHNESS")
        if self.ofb_enum == 'OP5':
            bpy.ops.object.bake(type="EMIT")
        
        return {"FINISHED"}
