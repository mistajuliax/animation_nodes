import bpy, random, mathutils
from ... base_types.node import AnimationNode
from ... mn_execution import nodePropertyChanged


class GridArrange(bpy.types.Node, AnimationNode):
    bl_idname = "mn_GridArrange"
    bl_label = "Grid Arrange"
    node_category = "Arrange"
    isDetermined = True
    
    def create(self):
        self.inputs.new("mn_IntegerSocket", "Index")
        self.inputs.new("mn_IntegerSocket", "Width").value = 10
        self.inputs.new("mn_FloatSocket", "Distance").value = 3
        self.outputs.new("mn_VectorSocket", "Vector")
        
    def getInputSocketNames(self):
        return {"Index" : "index",
                "Width" : "width",
                "Distance" : "distance"}
    def getOutputSocketNames(self):
        return {"Vector" : "vector"}

    def execute(self, index, width, distance):
        width = max(width, 1)
        vector = mathutils.Vector((0, 0, 0))
        vector[0] = index % width * distance
        vector[1] = int(index / width) * distance
        return vector
        
