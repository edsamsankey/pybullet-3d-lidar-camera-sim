import pybullet as p
import pybullet_data

def setup_simulation(gui=True):
    if gui:
        p.connect(p.GUI)
    else:
        p.connect(p.DIRECT)

    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.81)

    p.loadURDF("plane.urdf")
    robot_id = p.loadURDF("cube.urdf", [0, 0, 0.5])
    p.loadURDF("r2d2.urdf", [2, 2, 0.5])

    return robot_id
