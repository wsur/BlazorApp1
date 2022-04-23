from typing import Optional

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def delete(title: str) -> bool:
    # setting_up()

    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file in file_list:
        if file['title'] == f'{title}.jpg':
            file.Delete()

            return True

    return False


def upload(binary_image_code, title: str) -> bool:
    # setting_up()


    with open(f'{title}.jpg', "wb") as f:
        f.write(binary_image_code)

    file = drive.CreateFile({'title': f'{title}.jpg'})
    file.SetContentFile(f'{title}.jpg')
    file.Upload()

    return True


def download(title: str) -> Optional[bytes]:
    # setting_up()

    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file in file_list:
        if file['title'] == f'{title}.jpg':
            file.GetContentFile(file['title'])
            with open(file['title'], "rb") as f:
                encoded_string = file

            return encoded_string


def setting_up() -> None:
    global drive

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)


def testing_upload() -> None:
    with open("./image/abc.jpg", "rb") as f:
        encoded_string = f.read()

    upload(encoded_string, "abc")


def testing_download() -> None:
    download("abc")


def testing_delete() -> None:
    delete("abc")


#gauth = GoogleAuth()
#gauth.LocalWebserverAuth()

#drive = GoogleDrive(gauth)

testing_download()
testing_upload()
