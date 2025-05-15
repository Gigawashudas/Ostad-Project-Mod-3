


import os
import qrcode

def read_from_file(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
        url = lines[0].strip()
        filename = lines[1].strip()
        return url, filename

def generate_qrcode(data, qrcode_file_name):
    qr = qrcode.make(data)
    qr.save(qrcode_file_name + ".png")
    print(f"QR code generated and saved as {qrcode_file_name}")

absFilePath = os.path.abspath("File.txt")
fileName = os.path.basename(absFilePath)

print(absFilePath)
print(fileName)

data = read_from_file(fileName)

print(data[0])
qrcode_file_name = data[1]

qr_code = generate_qrcode(data, qrcode_file_name)

