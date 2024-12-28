import requests
import traceback

supportedhardware = {
    "page2": "tolino_page_2",
    "shine3": "tolino_shine_3",
    "vision5": "tolino_vision_5",
    "epos2": "tolino_epos_2",
    "vision2": "tolino_vision_2",
    "page": "tolino_page"
}

def download(filename: str, hardware: str):
    try:
        response = requests.post(
            url = "https://bosh.pageplace.de/bosh/rest/v2/versioncheck",
            headers = {
                "hardware_type": str(supportedhardware[hardware]),
                "os_version": "4.4.2",
                "language_code": "de",
                "hardware_id": "00000000000000000000000000000000",
                "client_type": str(supportedhardware[hardware]).upper(),
                "client_version": "14.2.0",
                "Content-Type": "text/plain; charset=UTF-8"
            },
            verify=False
        ).json()
        config = response['initAppResponse']['config']
        for element in config:
            if element['key'] == 'CHANGELOG_EN':
                description = element['value']
            elif element['key'] == 'DOWNLOAD_URL':
                url = element['value']
        package = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(package.content)
        return
    except:
        raise ValueError(str(traceback.format_exc()))
def downloadnookfw(filename: str):
    try:
        url = "http://su.barnesandnoble.com/nook/piper/5.0/piper/0.118/update.zip"
        package = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(package.content)
        return
    except:
        raise ValueError(str(traceback.format_exc()))