import base64
import qrcode
import random


def ToBase64(file_name):
    try:
        with open(file_name, 'rb') as fileObj:
            file_data = fileObj.read()
            base64_data = base64.b64encode(file_data)
            return base64_data
    except:
        base64_data = base64.b64encode(file_name.encode())
        return base64_data


def ToQrcode(base64_data, file_name, max_size=2500, min_range=0.8):
    data = str(base64_data)
    basic_file_name = file_name
    end = 0
    start = 0
    cnt = 0
    while (end != len(data) - 1):
        end += random.randint(max_size * min_range, max_size)
        if (end > len(data) - 1):
            end = len(data) - 1
        qr = qrcode.make(
            data[start:end], version=4, error_correction=qrcode.constants.ERROR_CORRECT_L)
        file_name = basic_file_name + "_" + str(cnt) + ".jpg"
        qr.save(file_name)
        cnt += 1
        start = end + 1
    qr.save(file_name)


if __name__ == "__main__":
    string = input()
    file_name = str(input())
    ToQrcode(ToBase64(file_name), file_name)
