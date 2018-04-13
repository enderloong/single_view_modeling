

def compute_vp(rw):
    p1 = rw.clk_pt[0]
    p2 = rw.clk_pt[1]
    p3 = rw.clk_pt[2]
    p4 = rw.clk_pt[3]
    # vp = (p11 * p22 - p12 * p21) / (p11 + p22 - p12 - p21)
    # y1==y2, y3==y4 => vpy = ((x22 - x21)*y2 - (x12 - x11)*y1) / (x22 + x12 - x21 - x11)
    if p1[0] == p2[0]:
        vpx = ( (p4[1] - p3[1]) * p1[0] - (p2[1] - p1[1]) * p3[0] ) / (p1[1] + p4[1] - p2[1] - p3[1])
    else:
        vpx = (p1[0] * p4[0] - p2[0] * p3[0]) / (p1[0] + p4[0] - p2[0] - p3[0])
    if p1[1] == p2[1]:
        vpy = ((p4[0] - p3[0]) * p1[1] - (p2[0] - p1[0]) * p3[1] ) / (p1[0] + p4[0] - p2[0] - p3[0])
    else:
        vpy = (p1[1] * p4[1] - p2[1] * p3[1]) / (p1[1] + p4[1] - p2[1] - p3[1])
    return [vpx, vpy]


if __name__ == '__main__':
    class temp_rw1():
        clk_pt = [
            [5, 10],
            [3, 10],
            [2, 9],
            [1, 9]
        ]
        # should vanished at [-1, 8]
    
    rw1 = temp_rw1()
    vp1 = compute_vp(rw1)
    print(vp1)

