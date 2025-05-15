


import os
import qrcode

def read_from_file(fileName):
    with open(fileName, "r") as file:
        data = file.read()
    return data

def generate_qrcode(data):
    qr = qrcode.make(data)
    qr.save("image.png")

absFilePath = os.path.abspath("File.txt")
fileName = os.path.basename(absFilePath)

print(absFilePath)
print(fileName)

data = read_from_file(fileName)

qr_code = generate_qrcode(data)

