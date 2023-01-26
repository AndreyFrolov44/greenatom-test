import requests

from bs4 import BeautifulSoup


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'cookie': 'yashr=2537404371674146950; yandexuid=7206266641671627033; yuidss=7206266641671627033; yp=1674326032.yu.2645282651674146130; ymex=1676831632.oyu.2645282651674146130#1989506130.yrts.1674146130#1989506130.yrtsi.1674146130; i=UeOCKDO40qc6y5h9fe6RA9G1yzaMrn9iODiquOJvkOmf+9vNksdftWUzIutoo8DvpPBWQdvTYUySad0gcW86KL1IIWc=; is_gdpr=0; is_gdpr_b=CMjpUhC+ogE=; yabs-sid=2591463911674755770'
}


def get_html_greenatom() -> str:
    return requests.get('https://greenatom.ru/', headers=headers).text


def get_count_tags(html: str) -> dict:
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all()
    count_tags_attrs = 0
    for tag in soup.find_all():
        if tag.attrs:
            count_tags_attrs += 1

    return {'tags_count': len(tags), 'count_tags_attrs': count_tags_attrs}


print(get_count_tags(get_html_greenatom()))
