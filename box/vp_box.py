import sys

def vanished_point_box(box):
    vp1 = [0, 0]
    vp2 = [0, 0]
    mode = 'vp'
    if box.info_2d.cc_num >= 5:
        p1 = (box.info_2d.click_pos[0][0] + 5, box.info_2d.click_pos[0][1] + 5)
        p2 = (box.info_2d.click_pos[1][0] + 5, box.info_2d.click_pos[1][1] + 5)
        p3 = (box.info_2d.click_pos[2][0] + 5, box.info_2d.click_pos[2][1] + 5)
        p4 = (box.info_2d.click_pos[3][0] + 5, box.info_2d.click_pos[3][1] + 5)
        p5 = (box.info_2d.click_pos[4][0] + 5, box.info_2d.click_pos[4][1] + 5)
        p6 = (box.info_2d.click_pos[5][0] + 5, box.info_2d.click_pos[5][1] + 5)
        if abs(p1[0] + p4[0] - p2[0] - p3[0]) < 1:
            mp = (p1[0], int((p1[1] + p2[1])/2))
            vp1_x = mp[0] + 20 * (p3[0] - p1[0])
            vp1_y = mp[1] + 20 * (p3[1] - p1[1])
            vp1 = (vp1_x, vp1_y)
        else:
            vp1_x = (p1[0] * p4[0] - p2[0] * p3[0]) / (p1[0] + p4[0] - p2[0] - p3[0])
            vp1_y = ((p4[0] - p3[0]) * p1[1] - (p2[0] - p1[0]) * p3[1] ) / (p1[0] + p4[0] - p2[0] - p3[0])
        if abs(p1[0] + p6[0] - p2[0] - p5[0]) < 1:
            mp = (p1[0], int((p1[1] + p2[1])/2))
            vp2_x = mp[0] + 20 * (p5[0] - p1[0])
            vp2_y = mp[1] + 20 * (p5[1] - p1[1])
            vp2 = (vp2_x, vp2_y)
        else:
            vp2_x = (p1[0] * p6[0] - p2[0] * p5[0]) / (p1[0] + p6[0] - p2[0] - p5[0])
            vp2_y = ((p6[0] - p5[0]) * p1[1] - (p2[0] - p1[0]) * p5[1] ) / (p1[0] + p6[0] - p2[0] - p5[0])
            vp2 = (vp2_x, vp2_y)
        print('vanished point 1:', vp1)
        print('vanished point 2:', vp2)
        mode = 'f_vp'
        return [mode, vp1, vp2]
    else:
        print('use vp_box in the wrong place!')
        sys.exit()
        