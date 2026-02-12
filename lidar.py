import numpy as np
import pybullet as p

def get_3d_lidar(robot_id, ray_length=6):
    pos, _ = p.getBasePositionAndOrientation(robot_id)
    ray_starts, ray_ends = [], []

    for pitch in [-15, -7, 0, 7, 15]:
        for yaw in range(0, 360, 20):
            y_rad, p_rad = np.deg2rad(yaw), np.deg2rad(pitch)

            ray_starts.append(pos)
            ray_ends.append([
                pos[0] + ray_length * np.cos(y_rad) * np.cos(p_rad),
                pos[1] + ray_length * np.sin(y_rad) * np.cos(p_rad),
                pos[2] + ray_length * np.sin(p_rad)
            ])

    return p.rayTestBatch(ray_starts, ray_ends)
