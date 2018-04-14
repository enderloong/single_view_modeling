# import library
import pygame, sys, math
from pygame.locals import *
import cv2

# import python files
import vrml

# Basic configuration of pygame
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
pygame.init()

# read box image file
rw_img = cv2.imread('painting.png')
rw_pyg = pygame.image.load('painting.png')

# set up window
[img_width, img_height, img_channels] = rw_img.shape
screen = pygame.display.set_mode((img_height + 10, img_width + 10))
pygame.display.set_caption('Single View Modeling -- Painting')

# control variables
import c_proc_control as cpc
procsvm_rw = cpc.proc_control()

# image information
import c_rwimg as crw
imgsvm_rw = crw.rwimg(rw_img)
max_plane = 4
ttt = [imgsvm_rw] * max_plane
current_plane = 0
model_control = True
world = []

# real world information
true_point = [\
    [[-2, 0, 0], [-2, 5, 0], [20, 0, 0]], # way
    [[-2, 0, 5], [-2, 0, 0], [20, 0, 5]], # left lamps
    [[-2, 5, 5], [-2, 5, 0], [20, 5, 5]], # right lamps
    [[10, 25, 17], [10, 25, 2], [30, 0, 17]] # house
    #[[5, 0, -2], [5, 2.5, -2], [5, 0, -1]] # front wall
]

# initize proc struct
print('Please choose points on two parallel lines.')
print('Firstly, click on the left point of first line on stairs')

# main loop
while model_control:
    if procsvm_rw.mode == 'i':
        procsvm_rw.mode = 'in_plane'
    screen.fill(black)
    screen.blit(rw_pyg, (5,5))
    for event in pygame.event.get():
        # close window
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            procsvm_rw.mouse_pos = event.pos
            procsvm_rw.mousedown()
            # debug
            # if procsvm_rw.debug:
            #     print('[DEBUG] current mode:', procsvm_rw.mode)
            if procsvm_rw.mode == 'fp':
                procsvm_rw.mode_vp(ttt[current_plane])
            if procsvm_rw.mode == 'f' and current_plane < max_plane:
                procsvm_rw.reset()
                current_plane += 1
                
    if procsvm_rw.mode == 'f_vp':
        p1 = true_point[current_plane][0]
        p2 = true_point[current_plane][1]
        p3 = true_point[current_plane][2]
        ttt[current_plane].info_3d.set3dpos(p1, p2, p3)
        procsvm_rw.mode = 'f_3d'
    
    # # draw reference shapes
    line_width = 3
    if procsvm_rw.mode == 'f':
        pygame.draw.line(screen, red, procsvm_rw.clk_pt[0], procsvm_rw.clk_pt[1], line_width)
        pygame.draw.line(screen, red, procsvm_rw.clk_pt[2], procsvm_rw.clk_pt[3], line_width)
        pygame.draw.line(screen, red, procsvm_rw.clk_pt[0], ttt[current_plane].info_2d.vp, line_width)
        pygame.draw.line(screen, red, procsvm_rw.clk_pt[1], ttt[current_plane].info_2d.vp, line_width)

    for i in range(procsvm_rw.cc_num):
        draw_x = int(procsvm_rw.clk_pt[i][0])
        draw_y = int(procsvm_rw.clk_pt[i][1])
        pygame.draw.circle(screen, blue, (draw_x, draw_y), 4, 0)

    # extract textures
    if procsvm_rw.mode == 'f_3d':
        texture_name = 'texture' + str(current_plane + 1) + '.jpg'
        ttt[current_plane].extract_texture(procsvm_rw, texture_name)
        procsvm_rw.mode = 'f'
        if current_plane == 3 and model_control:
            procsvm_rw.mode = 'model'
            for i in range(max_plane):
                world.append(ttt[i].info_3d.pos_3d)

    # modeling
    if procsvm_rw.mode == 'model':
        vr_pt = vrml.Vrml()
        faces = []
        texture = []
        for i in range(2):
            texture.append([i, 0])
            texture.append([i, 1])
        print(world)
        faces.append([world[0][3], world[0][2], world[0][0], world[0][1]])
        faces.append([world[1][3], world[1][2], world[1][0], world[1][1]])
        faces.append([world[2][0], world[2][2], world[2][3], world[2][1]])
        faces.append([world[3][0], world[3][2], world[3][3], world[3][1]])

        vr_pt.startVrml()
        vr_pt.appendPolygon('texture1.jpg', faces[0], texture)
        vr_pt.appendPolygon('texture2.jpg', faces[1], texture)
        vr_pt.appendPolygon('texture3.jpg', faces[2], texture)
        vr_pt.appendPolygon('texture4.jpg', faces[3], texture)
        vr_pt.endVrml()
        print("model done")
        model_control = False


    # update display
    pygame.display.update()
