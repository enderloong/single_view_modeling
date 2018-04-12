class Vrml():
    vrml_file = ""
    header = ""
    initial_position = ""

    def __init__(self):
        self.header = ("#VRML V1.0 ascii\n"
                  "PointLight{ intensity 1 location 50 100 300 }\n"
                  "PointLight{ intensity 1 location 40 100 250 }\n"
                  "PointLight{ intensity 1 location 60 100 250 }\n"
                  "PointLight{ intensity 1 location 20 100 100 }\n"
                  "PointLight{ intensity 3 location 80 100 100 }\n"
                  "PointLight{ intensity 5 location 50 400 50 }\n"
                  "ShapeHints { \n"
                  " vertexOrdering  COUNTERCLOCKWISE \n"
                  " shapeType       SOLID \n"
                  " }\n")

        self.initial_position = ("Separator { \n"
                            "Transform {      translation -15 -30 -300}\n"
                            "Transform {      rotation 0 1 0 -1.27   }\n"
                            "Transform {      rotation 1 0 0 0  } \n"
                            "Transform {      rotation 0 0 1 -0.45  }\n")
    def startVrml(self):
        self.vrml_file = self.header + self.initial_position

    def endVrml(self):
        self.vrml_file += "}\n"

    def appendPolygon(self, filename, world_pts, texture_pts):
        ground_counter = 0

        separator = "Separator {\n"
        coordinate3 = "Coordinate3 { point [\n"
        for i in range(len(world_pts)):
            coordinate3 += "\t"
            coordinate3 += str(world_pts[i][0])
            coordinate3 += " "
            coordinate3 += str(world_pts[i][1])
            coordinate3 += " "
            coordinate3 += str(world_pts[i][2])
            coordinate3 += " ,\n"

            if world_pts[i][2] == 0:
                ground_counter += 1

        coordinate3 += "]}\n"

        texture2 = "Texture2 { filename \"" + filename + "\" }\n"

        texture_coordinate2 = "TextureCoordinate2 { point [\n"
        for i in range(len(texture_pts)):
            x = texture_pts[i][0]
            y = texture_pts[i][1]

            if x == 0 and y == 0:
                texture_coordinate2 += "0 1 ,\n"
            elif x == 0 and y != 0:
                texture_coordinate2 += "0 0 ,\n"
            elif x != 0 and y == 0:
                texture_coordinate2 += "1 1 ,\n"
            elif x != 0 and y != 0:
                texture_coordinate2 += "1 0 ,\n"

        texture_coordinate2 += "]}\n"

        indexed_faceset = "IndexedFaceSet { coordIndex [0, 1, 2, 3]}\n"
        end_separator = "}\n\n"
        self.vrml_file += \
            separator + \
            coordinate3 + \
            texture2 + \
            texture_coordinate2 + \
            indexed_faceset + \
            end_separator

    def debug(self):
        texture = []
        world = []

        for i in range(4):
            texture.append([i, 0])
            texture.append([i, 1])

        world.append([0, 0, 0])
        world.append([100, 0, 0])
        world.append([0, 100, 0])
        world.append([100, 100, 0])

        self.startVrml()
        self.appendPolygon('texture1.jpg', world, texture)
        self.appendPolygon('texture2.jpg', world, texture)
        self.appendPolygon('texture3.jpg', world, texture)
        self.endVrml()

vr = Vrml()
vr.debug()
print(vr.vrml_file)
