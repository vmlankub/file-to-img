import base64
import qrcode


def ToBase64(file_name):
    try:
        with open(file_name, 'rb') as fileObj:
            file_data = fileObj.read()
            base64_data = base64.b64encode(file_data)
            return base64_data
    except:
        base64_data = base64.b64encode(file_name.encode())
        return base64_data


def ToQrcode(base64_data, file_name, pkg_size=2500):
    data = str(base64_data)
    base_file_name = file_name
    for i in range(len(data) // pkg_size):
        qr = qrcode.make(
            data[i*pkg_size:(i+1)*pkg_size], version=4, error_correction=qrcode.constants.ERROR_CORRECT_L)
        file_name = base_file_name+"_"+str(i)+".jpg"
        qr.save(file_name)
    res = len(data) // pkg_size
    qr = qrcode.make(
        data[res*pkg_size:-1]+"\'", version=2, error_correction=qrcode.constants.ERROR_CORRECT_L)
    file_name = base_file_name+"_"+str(res)+".jpg"
    qr.save(file_name)


if __name__ == "__main__":
    file_name = str(input())
    ToQrcode(ToBase64(file_name), file_name, 1926)
