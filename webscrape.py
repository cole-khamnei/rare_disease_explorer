import io
import time
import requests
import re

from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup as bsoup
from tqdm.notebook import tqdm
# from tqdm import tqdm


REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/39.0.2171.95 Safari/537.36'
}
ANTI_DOS_DELAY = 0.1


def safe_request(url: str, headers: dict = REQUEST_HEADERS,
                 anti_dos_delay: float = ANTI_DOS_DELAY):
    """"""
    time.sleep(anti_dos_delay)
    try:
        data = requests.get(url, headers=headers)
        return data
    except requests.exceptions.ConnectionError as e:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return requests.get(url, headers=headers, verify=False)

        
def get_html(url: str):
    """"""
    request_content = safe_request(url)
    return bsoup(request_content.content, features="html.parser")


def str_remover(string: str, *tokens):
    """"""
    for token in tokens:
        string = string.replace(token, "")
    return string
