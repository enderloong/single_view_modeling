def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def pred_p(p1, p2, p3, p4):
    assert len(p1) == 2
    assert len(p2) == 2
    assert len(p3) == 2
    assert len(p4) == 2
    x4 = p4[0]
    y4 = p4[1]
    if abs(x4 - p3[0]) > abs(p2[0] - p1[0]):
        x4 = p3[0] + p2[0] - p1[0] - 0.01 * sgn(p2[0] - p1[0]) * abs(p2[0] - p1[0])
    if abs(y4 - p3[1]) > abs(p2[1] - p1[1]):
        y4 = p3[1] + p2[1] - p1[1] - 0.01 * sgn(p2[1] - p1[1]) * abs(p2[1] - p1[1])
    if p1[0] == p2[0]:
        x4 = p3[0]
    elif p1[1] == p2[1]:
        y4 = p3[1]
    else:
        k = (p2[1] - p1[1]) / (p2[0] - p1[0])
        y4 = int(k * (x4 - p3[0]) + p3[1])
    return [x4, y4]
        


if __name__ == "__main__":
    p1 = [1, 10]
    p2 = [2, 10]
    p3 = [3, 8 ]
    p4 = [5, 6 ]
    print(pred_p(p1, p2, p3, p4))