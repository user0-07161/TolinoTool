import zipfile
import shutil
import os
import requests

def generatenookolinopackage(nookfw: str, tolinofw: str, output: str, uboot: str):
    with zipfile.ZipFile(nookfw, 'r') as zip_ref:
        zip_ref.extractall("work")
    with zipfile.ZipFile(nookfw, 'r') as zip_ref:
        zip_ref.extractall("nook")
    with zipfile.ZipFile(tolinofw, 'r') as zip_ref:
        zip_ref.extractall("tolino")
    shutil.rmtree('work/system')
    shutil.copytree('tolino/system', 'work/system')
    os.remove('work/system/app/EPubProd.apk')
    os.remove('work/system/build.prop')
    os.remove('work/boot.img')
    os.remove('work/META-INF/com/google/android/updater-script')
    os.remove('work/recovery.img')
    os.remove('work/system/media/bootanimation.zip')
    os.remove('work/u-boot.bin')
    recovery = requests.get("https://user0.is-a.dev/TolinoTool/recovery.img")
    boot = requests.get("https://user0.is-a.dev/TolinoTool/boot.img")
    script = requests.get("https://user0.is-a.dev/TolinoTool/updater-script")
    with open("work/recovery.img", 'wb') as file:
        file.write(recovery.content)
    with open("work/boot.img", 'wb') as file:
        file.write(boot.content)
    with open('work/META-INF/com/google/android/updater-script', 'wb') as file:
        file.write(script.content)
    shutil.copyfile("nook/system/priv-app/bnereader.apk", "work/system/priv-app/bnereader.apk")
    shutil.copyfile("nook/system/priv-app/partner.apk", "work/system/priv-app/partner.apk")
    shutil.copyfile("nook/system/priv-app/NookHWTestPiperapp.apk", "work/system/priv-app/NookHWTestPiperapp.apk")
    shutil.copyfile('nook/system/media/bootanimation.zip', 'work/system/media/bootanimation.zip')
    shutil.copyfile('nook/system/build.prop', 'work/system/build.prop')
    shutil.copyfile(f'tolino/u-boot_{uboot}.bin', 'work/u-boot.bin')
    shutil.make_archive(output, 'zip', "work/")
    shutil.rmtree('work')
    shutil.rmtree('tolino')
    shutil.rmtree('nook')
