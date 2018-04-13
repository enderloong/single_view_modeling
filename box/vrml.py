class Vrml():
    vrml_file = ""
    header = ""
    initial_position = ""

    def __init__(self):
        self.header = ("#VRML V2.0 utf8\n"
                  "PointLight{ intensity 1 location 50 100 300 }\n"
                  "PointLight{ intensity 1 location 40 100 250 }\n"
                  "PointLight{ intensity 1 location 60 100 250 }\n"
                  "PointLight{ intensity 1 location 20 100 100 }\n"
                  # "PointLight{ intensity 3 location 80 100 100 }\n"
                  # "PointLight{ intensity 5 location 50 400 50 }\n"
                       )
                  # "ShapeHints { \n"
                  # " vertexOrdering  COUNTERCLOCKWISE \n"
                  # " shapeType       SOLID \n"
                  # " }\n"
        # self.initial_position = ("Separator { \n"
        #                     "Transform {      translation -15 -30 -300}\n"
        #                     "Transform {      rotation 0 1 0 -1.27   }\n"
        #                     "Transform {      rotation 1 0 0 0  } \n"
        #                     "Transform {      rotation 0 0 1 -0.45  }\n")
    def startVrml(self):
        # self.vrml_file = self.header + self.initial_position
        self.vrml_file = self.header + self.initial_position

    def endVrml(self):
        with open('polygons.wrl', 'w+') as f:
            f.write(self.vrml_file)


    def appendPolygon(self, filename, world_pts, texture_pts):
        ground_counter = 0

        shape = "Shape {\n"
        coordinate3 = "coord Coordinate { point [\n"
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

        texture = "appearance Appearance { texture ImageTexture { url \"" + filename + "\" }}\n"

        texture_coordinate = "texCoord TextureCoordinate { point [\n"
        for point in texture_pts:
            x = point[0]
            y = point[1]
            if x == 0 and y == 0:
                texture_coordinate += "0 1 ,\n"
            elif x == 0 and y != 0:
                texture_coordinate += "0 0 ,\n"
            elif x != 0 and y == 0:
                texture_coordinate += "1 0 ,\n"
            elif x != 0 and y != 0:
                texture_coordinate += "1 1 ,\n"

        texture_coordinate += "]}\n"
        end_faceset = "}\n\n"

        indexed_faceset = "geometry IndexedFaceSet { coordIndex [0, 1, 2, 3, -1]\n"
        end_shape = "}\n\n"
        self.vrml_file += \
            shape + \
            texture + \
            indexed_faceset + \
            coordinate3 + \
            texture_coordinate + \
            end_faceset + \
            end_shape


        # self.vrml_file += \
        #     shape + \
        #     coordinate3 + \
        #     texture + \
        #     texture_coordinate + \
        #     indexed_faceset + \
        #     end_shape

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
