import sys

def vanished_point_box(box):
    vp1 = [0, 0]
    vp2 = [0, 0]
    mode = 'vp'
    if box.info_2d.cc_num == 5:
        if (box.info_2d.click_pos[0][0] - box.info_2d.click_pos[1][0] + box.info_2d.click_pos[0][1] - box.info_2d.click_pos[1][1]) == \
            (box.info_2d.click_pos[2][0] - box.info_2d.click_pos[3][0] + box.info_2d.click_pos[2][1] - box.info_2d.click_pos[3][1]):
            print('cannot find vanished point, please repeat choosing points')
            mode = 'in_p1'
        elif (box.info_2d.click_pos[0][0] - box.info_2d.click_pos[1][0] + box.info_2d.click_pos[0][1] - box.info_2d.click_pos[1][1]) == \
            (box.info_2d.click_pos[4][0] - box.info_2d.click_pos[5][0] + box.info_2d.click_pos[4][1] - box.info_2d.click_pos[5][1]):
            print('cannot find vanished point, please repeat choosing points')
            mode = 'in_p1'
        else:
            # vp = (p11 * p22 - p12 * p21) / (p11 + p22 - p12 - p21)
            vp1_x = (box.info_2d.click_pos[0][0] * box.info_2d.click_pos[3][0] - box.info_2d.click_pos[1][0] * box.info_2d.click_pos[2][0]) / (box.info_2d.click_pos[0][0] + box.info_2d.click_pos[3][0] - box.info_2d.click_pos[1][0] - box.info_2d.click_pos[2][0])
            vp1_y = (box.info_2d.click_pos[0][1] * box.info_2d.click_pos[3][1] - box.info_2d.click_pos[1][1] * box.info_2d.click_pos[2][1]) / (box.info_2d.click_pos[0][1] + box.info_2d.click_pos[3][1] - box.info_2d.click_pos[1][1] - box.info_2d.click_pos[2][1])
            vp1 = [vp1_x, vp1_y]
            vp2_x = (box.info_2d.click_pos[0][0] * box.info_2d.click_pos[5][0] - box.info_2d.click_pos[1][0] * box.info_2d.click_pos[4][0]) / (box.info_2d.click_pos[0][0] + box.info_2d.click_pos[5][0] - box.info_2d.click_pos[1][0] - box.info_2d.click_pos[4][0])
            vp2_y = (box.info_2d.click_pos[0][1] * box.info_2d.click_pos[5][1] - box.info_2d.click_pos[1][1] * box.info_2d.click_pos[4][1]) / (box.info_2d.click_pos[0][1] + box.info_2d.click_pos[5][1] - box.info_2d.click_pos[1][1] - box.info_2d.click_pos[4][1])
            vp2 = [vp2_x, vp2_y]
            print('vanished point 1:', vp1)
            print('vanished point 2:', vp2)
            mode = 'f_vp'
        return [mode, vp1, vp2]
    else:
        print('use vp_box in the wrong place!')
        sys.exit()
        