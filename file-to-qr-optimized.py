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


def generate_file_name(file_name: str):
    name = file_name
    name = name.replace('\\', '_')
    name = name.replace('/', '_')
    name = name.replace(':', '_')
    name = name.replace('*', '_')
    name = name.replace('?', '@')
    name = name.replace('\"', '@')
    name = name.replace('<', '(')
    name = name.replace('>', ')')
    name = name.replace('|', '_')
    return name


def ToQrcode(base64_data, file_name: str, max_size=2500, min_range=0.8):
    rand = random.Random()
    rand.seed(time.time_ns())
    data = str(base64_data)
    data = "base64:\"" + data[2:-1] + "\";file_name:\"" + \
        file_name + "\";generate_time:\"" + \
        str(time.time_ns()) + "\";powered_by:\"MinecraftFuns\""
    data_len = len(data)
    basic_file_name = generate_file_name(file_name)
    end = 0
    start = 0
    cnt = 0
    while (end != data_len):
        end += rand.randint(math.floor(max_size * min_range), max_size)
        if (end > data_len):
            end = data_len
        try:
            qr = qrcode.make(
                data[start:end], version=4, error_correction=qrcode.constants.ERROR_CORRECT_L)
        except:
            print("Error while generating QR Code. ")
        file_name = basic_file_name + "_" + str(cnt) + ".jpg"
        try:
            qr.save(file_name)
            print(file_name + " saved. ")
        except:
            print(file_name + " unsaved. Please check. ")
        cnt += 1
        start = end


if __name__ == "__main__":
    is_opt_out = 0
    while(is_opt_out == 0):
        file_name = str(
            input("Please input filename or a single string ( Enter exit() to exit ) : "))
        if "exit()" in file_name:
            is_opt_out = 1
        else:
            ToQrcode(ToBase64(file_name), file_name)
