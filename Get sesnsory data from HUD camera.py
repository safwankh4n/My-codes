import globe
import os
import sys
import random
import numpy as np
import time
import cv2


#EXCEPTION HANDLING
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' %s)
        sys.version_info.major,
        sys.version_infrp.minor,
        'win-amd64' if os.name == nt else 'linux-x86_64')) [0])
expect IndexError:
pass
import carla

IM_WIDTH = 640
IM_HEIGHT = 480

def process_img(image):
    i=np.array(image.raw_data)
    #print(i.shape)
    i2 = i.reshape((IM_HEIGTH, IM_WIDTH, 4))
    i3 = i2 [: , : , 3]
    cv2.imshow("", i3)
    cv2.waitKey(1)
    return i3/255.0

#COMPUTER VISION FUNCTION TO IMAGE 




actor_list = []



try:
    client = carla.Client("localhost", 2000)
    client.set_timeout(2.0)

    world = client.get_world()

    blueprint_library = world.get_blueprint_library()
    bp = blueprint_library.filter("model3")[0]
    print(bp)


    spawn_point = random.choice(world.get_map().get_spawn_points())

    vehicle = world.spawn_actor(bp, spawn_point)
    #vehicle.set_autopilot(True)
    vehicle.apply_control(carla.vehicle_control(throttle = 1.0, steer = 0.0))
    actor_list.append(vehicle)

#------------------------------------------------------------------------------------------------------------# 

    cam_bp = blueprint_library.find("sensor.camera.rgb")
    cam_bp.set_attributes("image_size_x", f"{IM_WIDTH}")
    cam_bp.set_attributes("image_size_y", f"{IM_HEIGHT}")
    cam_bp.set_attributes("fov", "110")

    spawn_point = carla.Transform(carla.Location(x=2.5, z=0.7))

    sensor = world.spawn_actor(cam_bp, spawn_point, attach_to=vehicle)

    actor_list.append(sensor)

#------------------------------------------------------------------------------------------------#

    camera.listen(lambda data : process_img(data))


    time.sleep(5)

  



finally:
    for actor in actor_list:
        actor.destroy()
        print(" all cleaned up!")
