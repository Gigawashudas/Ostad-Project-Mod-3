import os
import qrcode

def read_from_file(inputFileName):  
    with open(inputFileName, "r") as file:  
        return list(map(str.strip, file.readlines()))

def generate_qrcode(lines):
    qrcode.make(lines[0]).save("-".join(lines[1].split(" ")) + ".png")
    print(f"QR code generated and saved as {lines[1]}")

generate_qrcode(read_from_file(os.path.abspath("user_data.txt")))