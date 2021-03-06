# import library
import pygame, sys, math
from pygame.locals import *
from PIL import Image
import cv2

# import python files
import f_mousedown as fmd
import vp_box as vp
import extract_texture as ett
import vrml
# import mousenow as msn

# Basic configuration of pygame
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
pygame.init()

# read box image file
box_img = cv2.imread('box.bmp')
box_pyg = pygame.image.load('box.bmp')

# set up window
[img_width, img_height, img_channels] = box_img.shape
screen = pygame.display.set_mode((img_height + 10, img_width + 10))
pygame.display.set_caption('Single View Modeling -- Box')
myfont = pygame.font.Font(None, 60)

# control variables
current_mode = 'i'

# 2-d information
class proc_2d():
    input_mode = 'h'
    click_pos = [[0,0]] * 7
    cc_num = 0

    def __init__(self, img):
        self.raw_image = img


# 3-d information
class proc_3d():
    base_point = [0, 0]
    # x z y
    # \ | /
    x_dist = 4
    y_dist = 3
    z_dist = 1.83
    cp_3d = [[0,0,0]] * 8
    current_node = 0

    def build3d(self, info_2d):
        self.cp_3d[0] = [0, 0, self.z_dist]
        self.cp_3d[1] = [0, 0, 0]
        self.cp_3d[2] = [self.x_dist, 0, self.z_dist]
        self.cp_3d[3] = [self.x_dist, 0, 0]
        if self.y_dist == 0:
            cos_ratio = (info_2d.click_pos[1][1] - info_2d.click_pos[0][1]) / math.sqrt((info_2d.click_pos[1][1])**2 + (info_2d.click_pos[0][1])**2)
            self.y_dist = (1 - (info_2d.click_pos[5][1] - info_2d.click_pos[4][1])/ (cos_ratio * self.z_dist)) / (1 - (info_2d.click_pos[3][1] - info_2d.click_pos[2][1])/(cos_ratio * self.z_dist)) * self.x_dist
            self.cp_3d[4] = [0, self.y_dist, self.z_dist]
            self.cp_3d[5] = [0, self.y_dist, 0]
            self.cp_3d[6] = [self.x_dist, self.y_dist, self.z_dist]
            self.cp_3d[7] = [self.x_dist, self.y_dist, 0]
        else:
            self.cp_3d[4] = [0, self.y_dist, self.z_dist]
            self.cp_3d[5] = [0, self.y_dist, 0]
            self.cp_3d[6] = [self.x_dist, self.y_dist, self.z_dist]
            self.cp_3d[7] = [self.x_dist, self.y_dist, 0]

# proc data
class proc_img():
    info_3d = proc_3d()
    
    def __init__(self, box_img):
        self.info_2d = proc_2d(box_img)

# initize proc struct
box = proc_img(box_img)
print('Please choose points on the two parallel line, first to click on the top point of first line')
if current_mode == 'i':
    current_mode = 'in_p1'

# main loop
while True:
    screen.fill(black)
    screen.blit(box_pyg, (5,5))
    for event in pygame.event.get():
        # close window
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            [box, current_mode, vp] = fmd.mousedown(mouse_x, mouse_y, current_mode, box)
            # debug
            print('[DEBUG] current mode:', current_mode)

    if current_mode == 'f_vp':
        box.info_3d.build3d(box.info_2d)
        print(box.info_3d.cp_3d[6])
        current_mode = 'f_3d'
    
    # draw reference shapes
    line_width = 3
    if current_mode in ['f_3d', 'f_warp']:
        pygame.draw.line(screen, red, box.info_2d.click_pos[0], box.info_2d.click_pos[1], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[2], box.info_2d.click_pos[3], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[4], box.info_2d.click_pos[5], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[0], vp[0], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[0], vp[1], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[1], vp[0], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[1], vp[1], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[2], box.info_2d.click_pos[6], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[4], box.info_2d.click_pos[6], line_width)
        pygame.draw.line(screen, red, vp[0], vp[1], line_width)
    for i in range(box.info_2d.cc_num):
        draw_x = int(box.info_2d.click_pos[i][0]) + 5
        draw_y = int(box.info_2d.click_pos[i][1]) + 5
        pygame.draw.circle(screen, blue, (draw_x, draw_y), 4, 0)

    if current_mode == 'f_warp':
        vr_box = vrml.Vrml()
        world = box.info_3d.cp_3d

        texture = []
        for i in range(2):
            texture.append([i, 0])
            texture.append([i, 1])

        faces = []
        faces.append([world[0], world[1], world[3], world[2]])
        faces.append([world[4], world[5], world[1], world[0]])
        faces.append([world[4], world[0], world[2], world[6]])
        faces.append([world[2], world[3], world[7], world[6]])
        faces.append([world[7], world[3], world[1], world[5]])
        faces.append([world[6], world[7], world[5], world[4]])

        vr_box.startVrml()
        vr_box.appendPolygon('texture1.jpg', faces[0], texture)
        vr_box.appendPolygon('texture2.jpg', faces[1], texture)
        vr_box.appendPolygon('texture3.jpg', faces[2], texture)
        vr_box.appendPolygon('grey.jpg', faces[3], texture)
        vr_box.appendPolygon('grey.jpg', faces[4], texture)
        vr_box.appendPolygon('grey.jpg', faces[5], texture)
        vr_box.endVrml()

    # extract textures
    if current_mode == 'f_3d':
        ett.extract_texture(box)
        current_mode = 'f_warp'
        

    # update display
    pygame.display.update()
