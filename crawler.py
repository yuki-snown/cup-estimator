import requests
from bs4 import BeautifulSoup
from PIL import ImageFile
from io import BytesIO
import base64
import time


def clawl(csize):
    try:
        url = f'https://xvideo001.com/actress_boobs/{csize}_cup'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        actress = soup.select('#actress_index_ru')[0]
        for a in actress.find_all('img'):
            time.sleep(0.5)
            data = requests.get(a.attrs['data-src'])
            p = ImageFile.Parser()
            p.feed(data._content)
            img = p.close()
            w, h = img.size
            s = BytesIO()
            img.save(s, "JPEG")
            encode_data = base64.b64encode(s.getvalue())
            print(f'{csize}\t{w}\t{h}\t{encode_data.decode()}')
        time.sleep(1)
    except OSError:
        pass


def main():
    for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        clawl(csize=c)


if __name__ == '__main__':
    main()
