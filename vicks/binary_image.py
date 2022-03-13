
import base64

def write_image():
    with open("gillu.jpg", "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    print(converted_string, type(converted_string))

    with open('gillu.txt', "wb") as file:
        file.write(converted_string)


def read_image():
    file = open('gillu.txt', 'rb')
    byte = file.read()
    file.close()

    decodeit = open('gillu.jpeg', 'wb')
    decodeit.write(base64.b64decode((byte)))
    decodeit.close()

write_image()
read_image()