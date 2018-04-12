# import library
import pygame, sys
from pygame.locals import *
from PIL import Image

# import python files
import f_mousedown as fmd
import vp_box as vp

# Basic configuration of pygame
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
pygame.init()

# read box image file
box_img = Image.open('box.bmp')
box_pyg = pygame.image.load('box.bmp')

# set up window
[img_height, img_width] = box_img.size
screen = pygame.display.set_mode((img_height + 10, img_width + 10))
pygame.display.set_caption('Single View Modeling -- Box')
myfont = pygame.font.Font(None, 60)

# control variables
current_mode = 'i'

# 2-d information
class proc_2d():
    mode = 'i'
    click_pos = [[0,0]] * 6
    cc_num = 0

    def __init__(self, img):
        self.raw_image = img


# 3-d information


# proc data
class proc_img():
    
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
            print('current mode:', current_mode)
        
    # draw reference line
    line_width = 3
    if current_mode == 'f_vp':
        pygame.draw.line(screen, red, box.info_2d.click_pos[0], box.info_2d.click_pos[1], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[2], box.info_2d.click_pos[3], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[4], box.info_2d.click_pos[5], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[0], vp[0], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[0], vp[1], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[1], vp[0], line_width)
        pygame.draw.line(screen, red, box.info_2d.click_pos[1], vp[1], line_width)
        pygame.draw.line(screen, red, vp[0], vp[1], line_width)

    # update display
    pygame.display.update()
