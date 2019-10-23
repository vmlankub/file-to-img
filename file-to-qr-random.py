import base64
import qrcode
import random
import time
import math


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
    rand = random.Random()
    rand.seed(time.time_ns())
    data = str(base64_data)
    data = "base64:\'" + data[2:-1]+"\'Powered_by_MinecraftFuns"
    data_len = len(data)
    basic_file_name = file_name
    end = 0
    start = 0
    cnt = 0
    while (end != data_len):
        end += rand.randint(math.floor(max_size * min_range), max_size)
        if (end > data_len):
            end = data_len
        qr = qrcode.make(
            data[start:end], version=4, error_correction=qrcode.constants.ERROR_CORRECT_L)
        file_name = basic_file_name + "_" + str(cnt) + ".jpg"
        qr.save(file_name)
        cnt += 1
        start = end


if __name__ == "__main__":
    file_name = str(input())
    ToQrcode(ToBase64(file_name), file_name)
