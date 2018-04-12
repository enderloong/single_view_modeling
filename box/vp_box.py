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

        return [mode, vp1, vp2]
    else:
        print('use vp_box in the wrong place!')
        sys.exit()
        