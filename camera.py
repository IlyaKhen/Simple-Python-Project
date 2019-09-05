# ilya khenkin 43/3 final project
# camera class
import webbrowser  # importing a web browser


class CameraClass:
    name = ""
    latitude = 0.0
    longitude = 0.0
    grad_circle = 0
    last_photo = ""

    def __init__(self, name, lat, long, grad, photo):
        self.name = name
        self.latitude = lat
        self.longitude = long
        self.grad_circle = grad
        self.last_photo = photo

    def get_camera_last_photo(self):  # opening a last camera photo in chrome
        url = 'cam_last/' + self.last_photo
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    def to_string(self):
        return "Camera Type: " + self.name + "\nLatitude: " + self.latitude + "\nLongitude: " + self.longitude + "\nDegrees: " + self.grad_circle
