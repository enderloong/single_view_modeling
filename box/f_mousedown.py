from PIL import Image
import sys

import vp_box as vpb

def pred_x(box, mouse_y):
    if box.info_2d.cc_num == 3 and box.info_2d.click_pos[0][1] < box.info_2d.click_pos[1][1]:
        if box.info_2d.click_pos[0][0] == box.info_2d.click_pos[1][0]:
            pred_x = box.info_2d.click_pos[3][0]
        else:
            k = (box.info_2d.click_pos[0][1] - box.info_2d.click_pos[1][1])/(box.info_2d.click_pos[0][0] - box.info_2d.click_pos[1][0])
            pred_x = box.info_2d.click_pos[2][0] - (box.info_2d.click_pos[2][1] - mouse_y + 5)/k + 5
        return pred_x
    else:
        print('should not use function pred_x')
        sys.exit()

def mode_in_p1(box, mouse_x, mouse_y):
    mode = 'in_p1'
    if box.info_2d.cc_num == 0:
        box.info_2d.click_pos[0] = (mouse_x - 5, mouse_y - 5)
        box.info_2d.cc_num = 1
        print('Please choose the bottom point of this line')
    elif box.info_2d.cc_num == 1:
        if mouse_y < box.info_2d.click_pos[0][1]:
            print('Please choose the point carefully')
        else:
            box.info_2d.click_pos[1] = (mouse_x - 5, mouse_y - 5)
            box.info_2d.cc_num = 2
            print('Please choose the top point of second line')
    elif box.info_2d.cc_num == 2:
        box.info_2d.click_pos[2] = (mouse_x - 5, mouse_y - 5)
        box.info_2d.cc_num = 3
        print('Please choose the bottom point of second line')
    elif box.info_2d.cc_num == 3:
        if mouse_y < box.info_2d.click_pos[2][1]:
            print('Please choose the point carefully')
        else:
            x_pred = pred_x(box, mouse_y)
            if abs(x_pred - mouse_x) < 20:
                mouse_x = x_pred
                box.info_2d.click_pos[3] = (mouse_x - 5, mouse_y - 5)
                box.info_2d.cc_num = 4
                mode = 'in_p2'
                print('Please choose the top point of second line on the second plane')
            else:
                print('Please choose the point carefully')
    return mode

def mode_in_p2(box, mouse_x, mouse_y):
    mode = 'in_p2'
    if box.info_2d.cc_num == 4:
        if abs(mouse_x - box.info_2d.click_pos[0][0]) > abs(mouse_x - box.info_2d.click_pos[2][0]):
            print('Please choose the point carefully')
        else:
            box.info_2d.click_pos[4] = (mouse_x - 5, mouse_y - 5)
            box.info_2d.cc_num = 5
            print('Please choose the bottom point of second line on the second plane')
    elif box.info_2d.cc_num == 5:
        if mouse_y < box.info_2d.click_pos[4][1]:
            print('Please choose the point carefully')
        else:
            if box.info_2d.click_pos[0][0] == box.info_2d.click_pos[1][0]:
                pred_x = box.info_2d.click_pos[3][0]
            else:
                k = (box.info_2d.click_pos[0][1] - box.info_2d.click_pos[1][1])/(box.info_2d.click_pos[0][0] - box.info_2d.click_pos[1][0])
                pred_x = box.info_2d.click_pos[4][0] - (box.info_2d.click_pos[4][1] - mouse_y + 5)/k + 5
            if abs(pred_x - mouse_x) < 20:
                mouse_x = pred_x
                box.info_2d.click_pos[5] = (mouse_x - 5, mouse_y - 5)
                box.info_2d.cc_num = 5
                mode = 'f_p2'
                print('finish_p2')
            else:
                print('Please choose the point carefully')

    return mode

def mousedown(mouse_x, mouse_y, mode, box):
    vp = [[0, 0]] * 2
    print([mouse_x - 5, mouse_y - 5])
    if mode == 'in_p1':
        mode = mode_in_p1(box, mouse_x, mouse_y)
    elif mode == 'in_p2':
        mode = mode_in_p2(box, mouse_x, mouse_y)
    elif mode == 'f_p2':
        [mode, vp1, vp2] = vpb.vanished_point_box(box)
        vp[0] = vp1
        vp[1] = vp2
    return [box, mode, vp]

