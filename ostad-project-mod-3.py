


import os
import qrcode

def read_from_file(inputFileName):
    with open(inputFileName, "r") as file:
        lines = file.readlines()
        url = lines[0].strip()
        fileName = lines[1].strip()
        return url, fileName

def generate_qrcode(url, fileName):
    fileName = "-".join(fileName.split(" "))
    qr = qrcode.make(url)
    qr.save(fileName + ".png")
    print(f"QR code generated and saved as {fileName}")

[url , fileName] = read_from_file(os.path.abspath("user_data.txt"))

print(url + "\n" + fileName)

generate_qrcode(url, fileName)

