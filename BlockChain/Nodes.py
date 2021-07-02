class Nodes:

    def __init__(self):
        self.Nodes = []

    def AddNode(self,NewNode):
        self.Nodes += [NewNode]

    def GetNodes(self):
        Nodes = """{}""".format("\n".join(self.Nodes))
        return Nodes
