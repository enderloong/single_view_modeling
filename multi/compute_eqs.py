import sys

def compute_equations(a, b, c, d, y1, y2):
# [ a b ][x1] = [y1]
# [ c d ][x2]   [y2]
    if a * d - b * c == 0:
        print('rank < 2!')
        sys.exit()
    else:
        x1 = (d * y1 - b * y2)/(a * d - b * c)
        x2 = (a * y2 - c * y1)/(a * d - b * c)
        return [x1, x2]

def compute_upper_plane(vp, box):
    a = vp[1][0] - box.info_2d.click_pos[2][0]
    b = vp[0][0] - box.info_2d.click_pos[4][0]
    c = vp[1][1] - box.info_2d.click_pos[2][1]
    d = vp[0][1] - box.info_2d.click_pos[4][1]
    y1 = box.info_2d.click_pos[4][0] - box.info_2d.click_pos[2][0]
    y2 = box.info_2d.click_pos[4][1] - box.info_2d.click_pos[2][1]
    [k1, k2] = compute_equations(a, b, c, d, y1, y2)
    box.info_2d.click_pos[6][0] = k1 * (vp[1][0] - box.info_2d.click_pos[2][0]) + box.info_2d.click_pos[2][0]
    box.info_2d.click_pos[6][1] = k1 * (vp[1][1] - box.info_2d.click_pos[2][1]) + box.info_2d.click_pos[2][1]
    return box