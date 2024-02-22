class Utils:

    def __init__(self):
        pass

    @staticmethod
    def make_vindex(quantidade_de_vertices):
        i = 0
        vertices = quantidade_de_vertices
        vindex = [""]*vertices

        while i < vertices:
            vindex[i] = i
            i = i+1

        return vindex
