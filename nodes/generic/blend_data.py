import bpy
from bpy.props import *
from ... base_types.node import AnimationNode
from ... events import executionCodeChanged
from ... sockets.info import toIdName

class BlendDataNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_BlendDataNode"
    bl_label = "Blend Data"

    onlySearchTags = True
    searchTags = [ ("Blend Matrices", {"dataType" : repr("Matrix")}),
                   ("Blend Vectors", {"dataType" : repr("Vector")}),
                   ("Blend Floats", {"dataType" : repr("Float")}) ]

    def dataTypeChanged(self, context):
        self.generateSockets()
        executionCodeChanged()

    dataType = StringProperty(default = "Float", update = dataTypeChanged)

    def create(self):
        self.generateSockets()

    def generateSockets(self):
        self.inputs.clear()
        self.outputs.clear()

        idName = toIdName(self.dataType)
        self.inputs.new("an_FloatSocket", "Factor", "factor").setMinMax(0.0, 1.0)
        self.inputs.new("an_InterpolationSocket", "Interpolation", "interpolation").showName = False
        self.inputs.new(idName, "A", "a")
        self.inputs.new(idName, "B", "b")
        self.outputs.new(idName, "Output", "output")

    def getExecutionCode(self):
        lines = []
        lines.append("factor = min(max(factor, 0.0), 1.0)")
        lines.append("influence = interpolation[0](factor, interpolation[1])")

        if self.dataType in ("Float", "Vector"): lines.append("output = a * (1 - influence) + b * influence")
        if self.dataType == "Matrix": lines.append("output = a.lerp(b, influence)")

        return lines
