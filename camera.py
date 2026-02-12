import numpy as np
import pybullet as p
import cv2

def get_camera_frame(robot_pos, width=320, height=240):
    view_matrix = p.computeViewMatrixFromYawPitchRoll(
        cameraTargetPosition=robot_pos,
        distance=3,
        yaw=0,
        pitch=-15,
        roll=0,
        upAxisIndex=2
    )

    proj_matrix = p.computeProjectionMatrixFOV(
        fov=60,
        aspect=1,
        nearVal=0.1,
        farVal=100
    )

    _, _, rgb, _, _ = p.getCameraImage(width, height, view_matrix, proj_matrix)

    frame = np.reshape(rgb, (height, width, 4))[:, :, :3].astype(np.uint8)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame
