# ilya khenkin 43/3 final project
# function of main menu

from cameras_data_file import get_data

"""

def camera_data(command):  # getting data of camera with latitude and longitude
    cameras = get_data()  # getting a list of cameras 
    user_lat = input("Write latitude:")
    user_long = input("Write longitude:")
    flag = False
    for cam in cameras:
        if cam.longitude == user_long and cam.latitude == user_lat:
            flag = True
            print("\n" + cam.to_string())
    if not flag:
        print("\nNo security camera was found.")
            
def open_lst_photo(command):
    cameras = get_data()  # getting a list of cameras
    user_lat = input("Write latitude:")
    user_long = input("Write longitude:")
    flag = False
    for cam in cameras:
        if cam.longitude == user_long and cam.latitude == user_lat:
            flag = True
            cam.get_camera_last_photo()
    if not flag:
        print("\nNo security camera was found.")
        
def get_nsame_types(command):
    cameras = get_data()  # getting a list of cameras
    # creating a new list, getting a object if this object doesn't exist in a new list,
    # append it to him
    temp_list = [cameras[0].name]
    for i in range(0, cameras.__len__()):
        flag = True
        for j in range(0, temp_list.__len__()):
            if cameras[i].name == temp_list[j]:
                flag = False
        if flag:
            temp_list.append(cameras[i].name)
            
def calc_deg(command):
    try:
        deg = int(input("Write degree: "))
    except ValueError:
        print("Error. Invalid input data.")
    while deg > 360 or deg < 1:
        print("Wrong rotation degrees value")
        try:
            deg = int(input("Write degree: "))
        except ValueError:
            print("Error. Invalid input data.")
            
def count_cam_name(command):  # getting count if camera name
    cameras = get_data()  # getting a list of cameras
    name = input("Write name of the camera: ")
    count = 0
    for i in range(0, cameras.__len__()):
        if name == cameras[i].name:
            count += 1
    print("We've found " + str(count) + " security cameras")


"""

def main_menu(command):
    cameras = get_data()  # getting a list of cameras

    if command == '1':  # getting data of camera with latitude and longitude
        user_lat = input("Write latitude:")
        user_long = input("Write longitude:")
        flag = False
        for cam in cameras:
            if cam.longitude == user_long and cam.latitude == user_lat:
                flag = True
                print("\n" + cam.to_string())
        if not flag:
            print("\nNo security camera was found.")

    elif command == '2':  # opening a last photo of camera with latitude and longitude in chrome
        user_lat = input("Write latitude:")
        user_long = input("Write longitude:")
        flag = False
        for cam in cameras:
            if cam.longitude == user_long and cam.latitude == user_lat:
                flag = True
                cam.get_camera_last_photo()
        if not flag:
            print("\nNo security camera was found.")

    elif command == '3':  # printing all aren't same names of cameras
        # creating a new list, getting a object if this object doesn't exist in a new list,
        # append it to him
        temp_list = [cameras[0].name]
        for i in range(0, cameras.__len__()):
            flag = True
            for j in range(0, temp_list.__len__()):
                if cameras[i].name == temp_list[j]:
                    flag = False
            if flag:
                temp_list.append(cameras[i].name)

        print(temp_list)
    elif command == '4':  # calculating degree with user degree
        try:
            deg = int(input("Write degree: "))
        except ValueError:
            print("Error. Invalid input data.")
        while deg > 360 or deg < 1:
            print("Wrong rotation degrees value")
            try:
                deg = int(input("Write degree: "))
            except ValueError:
                print("Error. Invalid input data.")

        for ans in cameras:
            if int(ans.grad_circle) + int(deg) > 360:
                ans.grad_circle = 360 - int(deg)
            else:
                ans.grad_circle = int(ans.grad_circle) + int(deg)
            print("" + ans.name + " " + str(ans.grad_circle))

    elif command == '5':  # getting count if camera name
        name = input("Write name of the camera: ")
        count = 0
        for i in range(0, cameras.__len__()):
            if name == cameras[i].name:
                count += 1
        print("We've found " + str(count) + " security cameras")
    elif command != '6':  # wrong command
        print("Not such command.")
        
