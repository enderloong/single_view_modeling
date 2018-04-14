import math, cv2
import numpy as np

# 2-d information
class info_2d():
    vp = [[0,0]] * 2
    max_points = 7
    click_pos = [[0,0]] * max_points
    cc_num = 0

# 3-d information
class info_3d():
    base_point = [0, 0]
    # x z y
    # \ | /
    pos_3d = [[0,0,0]] * 4
    current_node = 0

    def set3dpos(self, p1, p2, p3):
        assert len(p1) == 3
        assert len(p2) == 3
        assert len(p3) == 3
        is_valid_pos = p3[0] == p1[0] or p3[1] == p1[1] or p3[2] == p1[2]
        assert is_valid_pos
        self.pos_3d[0] = p1
        self.pos_3d[1] = p2
        self.pos_3d[2] = p3
        for i in range(3):
            self.pos_3d[3][i] = p3[i] + p2[i] - p1[i]

class rwimg():
    info_2d = None
    info_3d = None
    img = None

    def __init__(self, img):
        self.img = img
        self.info_2d = info_2d()
        self.info_3d = info_3d()

    def extract_texture(self, rw, fileName):
        reference_line = [rw.clk_pt[0], rw.clk_pt[1]]
        reference_length = int(math.sqrt((reference_line[0][0] - reference_line[1][0])**2 + (reference_line[0][1] - reference_line[1][1])**2))
        ref_width_sq = [(self.info_3d.pos_3d[0][i] - self.info_3d.pos_3d[2][i])**2 for i in range(3)]
        ref_dist_sq  = [(self.info_3d.pos_3d[0][i] - self.info_3d.pos_3d[1][i])**2 for i in range(3)]
        reference_width = int(math.sqrt(sum(ref_width_sq)) / math.sqrt(sum(ref_dist_sq)) * reference_length)
        ul = [0, 0]
        ur = [reference_length, 0]
        bl = [0, reference_width]
        br = [reference_length, reference_width]
        print([reference_length, reference_width])
        blimg = [rw.clk_pt[0][0] - 5, rw.clk_pt[0][1] - 5]
        brimg = [rw.clk_pt[1][0] - 5, rw.clk_pt[1][1] - 5]
        ulimg = [rw.clk_pt[2][0] - 5, rw.clk_pt[2][1] - 5]
        urimg = [rw.clk_pt[3][0] - 5, rw.clk_pt[3][1] - 5]
        plane = np.float32([blimg, brimg, ulimg, urimg])
        rect = np.float32([bl, br, ul, ur])
        mat = cv2.getPerspectiveTransform(plane, rect)
        texture = cv2.warpPerspective(self.img, mat, (reference_length, reference_width))
        cv2.imwrite(fileName, texture)
        