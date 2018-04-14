# import library
import pygame, sys, math
from pygame.locals import *
import cv2

# import python files

# Basic configuration of pygame
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
pygame.init()

# read box image file
rw_img = cv2.imread('surface1.png')
rw_pyg = pygame.image.load('surface1.png')

# set up window
[img_width, img_height, img_channels] = rw_img.shape
screen = pygame.display.set_mode((img_height + 10, img_width + 10))
pygame.display.set_caption('Single View Modeling -- Multi-Image')

# control variables
import c_proc_control as cpc
procsvm_rw = cpc.proc_control()

# image information
import c_rwimg as crw
imgsvm_rw = crw.rwimg(rw_img)
max_plane = 2
ttt = [imgsvm_rw] * max_plane
current_plane = 0

# real world information

true_point = [\
    [[22, 31, 0], [22, 0, 0], [0, 31, 0]], # surface C
    [[-10,31,20], [0, 31, 0], [-10,0,20]], # surface B
]

''' true_point = [\
    [[-10,31,20], [0, 31, 0], [-10,0,20]], # surface B
] '''



# initize proc struct
print('Please choose points on two parallel lines.')
print('Firstly, click on the left point of first line on stairs')

# main loop
while True:
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
    


    # update display
    pygame.display.update()
