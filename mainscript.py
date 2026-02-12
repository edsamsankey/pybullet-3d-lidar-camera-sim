import pybullet as p
import time
import cv2

from lidar import get_3d_lidar
from camera import get_camera_frame
from simulation import setup_simulation

def main():
    print("Connecting to Physics Engine...", flush=True)
    robot_id = setup_simulation(gui=True)

    print("Simulation Ready. Check the OpenCV window for Camera feed.", flush=True)

    dt = 1.0 / 240.0
    t = 0

    while t < 2000:
        p.stepSimulation()

        lidar_hits = get_3d_lidar(robot_id)

        if t % 10 == 0:
            p.removeAllUserDebugItems()
            robot_pos, _ = p.getBasePositionAndOrientation(robot_id)

            for res in lidar_hits:
                if res[2] < 1.0:
                    p.addUserDebugLine(robot_pos, res[3], [0, 1, 0])

        robot_pos, _ = p.getBasePositionAndOrientation(robot_id)
        frame = get_camera_frame(robot_pos)

        cv2.imshow("Robot 3D Sensor Suite", frame)

        if t % 30 == 0:
            active_hits = len([r for r in lidar_hits if r[2] < 1.0])
            print(
                f"Time: {t/240:.2f}s | Active 3D LiDAR Hits: {active_hits} | Camera: OK",
                end="\r",
                flush=True
            )

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(dt)
        t += 1

    cv2.destroyAllWindows()
    p.disconnect()
    print("\nSimulation Closed Safely.")

if __name__ == "__main__":
    main()
