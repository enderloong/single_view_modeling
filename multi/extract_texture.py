import cv2, math
from PIL import Image
import numpy as np

def extract_texture(box):
    reference_line = [box.info_2d.click_pos[0], box.info_2d.click_pos[1]]
    reference_length = math.sqrt((reference_line[0][0] - reference_line[1][0])**2 + (reference_line[0][1] - reference_line[1][1])**2)
    x_length = reference_length / box.info_3d.z_dist * box.info_3d.x_dist
    y_length = reference_length / box.info_3d.z_dist * box.info_3d.y_dist
    x = round(x_length)
    y = round(y_length)
    z = round(reference_length)
    # plane 1
    plane1 = np.float32([ box.info_2d.click_pos[2], box.info_2d.click_pos[0], box.info_2d.click_pos[3], box.info_2d.click_pos[1]])
    rect1 = np.float32([ [0, 0], [x, 0], [0, z], [x, z] ])
    mat1 = cv2.getPerspectiveTransform(plane1, rect1)
    texture1 = cv2.warpPerspective(box.info_2d.raw_image, mat1, (x, z))
    cv2.imwrite('texture1.jpg', texture1)
    # plane 2
    plane2 = np.float32([ box.info_2d.click_pos[0], box.info_2d.click_pos[4], box.info_2d.click_pos[1], box.info_2d.click_pos[5]])
    rect2 = np.float32([ [0, 0], [y, 0], [0, z], [y, z] ])
    mat2 = cv2.getPerspectiveTransform(plane2, rect2)
    texture2 = cv2.warpPerspective(box.info_2d.raw_image, mat2, (y, z))
    cv2.imwrite('texture2.jpg', texture2)
    
    # plane 3
    plane3 = np.float32([ box.info_2d.click_pos[6], box.info_2d.click_pos[4], box.info_2d.click_pos[2], box.info_2d.click_pos[0]])
    rect3 = np.float32([ [0, 0], [x, 0], [0, y], [x, y] ])
    mat3 = cv2.getPerspectiveTransform(plane3, rect3)
    texture3 = cv2.warpPerspective(box.info_2d.raw_image, mat3, (x, y))
    cv2.imwrite('texture3.jpg', texture3)

