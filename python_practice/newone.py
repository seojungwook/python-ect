import re
from binascii import hexlify
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

import requests
import rsa
from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser

user_id = ""
user_pw = ""

with requests.session() as sel:


    keys_url = 'http://static.nid.naver.com/loginv3/js/keys_js.nhn'
    r = sel.get(keys_url)

    key_re = re.compile(r"(sessionkey|keyname|evalue|nvalue)\s*=\s*'(.+?)';")
    keys = dict(key_re.findall(r.text))
    keys['nvalue'] = int(keys['nvalue'], 16)
    keys['evalue'] = int(keys['evalue'], 16)

    #print(keys)

    public_key = rsa.PublicKey(keys['evalue'], keys['nvalue'])
    raw_data = (
        chr(len(keys['sessionkey'])) + keys['sessionkey']
        + chr(len(user_id)) + user_id
        + chr(len(user_pw)) + user_pw
    ).encode()

    #print(raw_data)

    enc_data = rsa.encrypt(raw_data, public_key)

    login_url = 'https://nid.naver.com/nidlogin.login'
    data = {
            'enctp': 1,
            'encpw': hexlify(enc_data),
            'encnm': keys['keyname'],
            'svctype': 0,
            'url': 'https://www.naver.com/',
            'enc_url': quote('http://www.naver.com/'),
            'postDataKey': '',
            'nvlong': '',
            'saveID': '',
            'smart_level': '1',
            'id': '',
            'pw': ''
            }

    r = sel.post(login_url, data=data, headers={'User-Agent': 'python-naverlogin'})

    if 'https://nid.naver.com/login/sso/finalize.nhn' in r.text:
            location_replace_re = re.compile(r'location\.replace\("(.+?)"\)')
            finalize_url = location_replace_re.search(r.text).group(1)

            r = sel.get(finalize_url)

            location_replace_re.search(r.text) is not None

    #co = r.headers.get('Set-Cookie')
    soup = BeautifulSoup(r.text,'html.parser')
    #print(co)
    #print(soup)
    durl=soup.select_one('form').get('action')
    okey = soup.find('input',{'id':'key'}).get('value')
    data = {
        'regyn': 'N',
        'nvlong': '',
        'mode': 'device',
        'key': okey,
        'enctp': '2',
        'encpw': '',
        'encnm': '',
        'svctype': '0',
        'svc': '',
        'viewtype': '0',
        'locale': 'ko_KR',
        'postDataKey': '',
        'smart_LEVEL':'1',
        'logintp':'',
        'url':'https://www.naver.com/',
        'secret_yn' : '',
        'pre_id' : '',
        'resp' : '',
        'exp': '' ,
        'ru' : ''
    }

    r = sel.post(durl, data=data, headers={'User-Agent': 'python-naverlogin'})
    real = BeautifulSoup(r.text,'html.parser')
    #print(real.text)
    #print(real.text.find(')'))
    start = int(real.text.find('https'))
    end = int(real.text.find(')')-1)
    last_url = str(real.text)[start:end]
    print(last_url)

    webbrowser.open(last_url)














