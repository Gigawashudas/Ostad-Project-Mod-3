import os
import qrcode

def read_from_file(inputFileName):  
    with open(inputFileName, "r") as file:  
        lines = map(str.strip, file.readlines())
        return lines

def generate_qrcode(url, fileName):
    qr = qrcode.make(url)
    qr.save("_".join(fileName.split(" ")) + ".png")
    print(f"QR code generated and saved as {fileName}")

[url, fileName] = read_from_file(os.path.abspath("user_data.txt"))

generate_qrcode(url, fileName)