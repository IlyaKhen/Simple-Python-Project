# ilya khenkin 43/3 final project
# file of cameras data
# getting data from a file and creating a list of cameras


from camera import CameraClass  # importing module for camera class


def get_data():
    try:
        f = open('sec_cameras.dat')
    except FileExistsError:
        print("Error. Cannot open a file.")
    cameras = []
    for line in f:
        parameters = line.split(',')  # split a line for getting values of cameras
        cam_name = parameters[0]
        lat = parameters[1]
        long = parameters[2]
        deg = parameters[3]
        photo = parameters[4]
        cam = CameraClass(cam_name, lat, long, deg, photo)
        cameras.append(cam)
    f.close()

    return cameras
