import bpy
from ... base_types.node import AnimationNode

class TranslationMatrix(bpy.types.Node, AnimationNode):
    bl_idname = "an_TranslationMatrix"
    bl_label = "Translation Matrix"

    def create(self):
        self.inputs.new("an_VectorSocket", "Translation", "translation")
        self.outputs.new("an_MatrixSocket", "Matrix", "matrix")

    def getExecutionCode(self):
        return "matrix = mathutils.Matrix.Translation(translation)"

    def getModuleList(self):
        return ["mathutils"]

    def duplicate(self, sourceNode):
        self.inputs[0].value = [0, 0, 0]
