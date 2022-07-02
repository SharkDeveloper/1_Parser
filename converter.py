import base64
import requests

from urllib.parse import unquote
from requests.auth import HTTPProxyAuth



with open("proxy.txt","r+") as proxy_file:
    file = open("SOCKS5.txt","w")
    for i,proxy in enumerate(proxy_file):
        #Дешифровка логина и пароля
        proxy = proxy.replace("ss://","")
        proxy = proxy.split("@")
        proxy[0] = proxy[0].encode('ascii') 
        proxy[0] = base64.b64decode(proxy[0] + b'=' * (-len(proxy[0]) % 4))
        proxy[0] = proxy[0].decode("ascii")
        proxy[1] = proxy[1].split("#")    
        proxy[0] = proxy[0].split(":")
        print(proxy)
        # создать HTTP‑сеанс
        password = proxy[0][1]
        login = proxy[1][1]
        login = unquote(login)
        login = login.replace(" ","_")
        login = login.replace("\n","")
        login = "🇩🇪_DE_@wbnet_90"
        print(login , password)
        
        s = requests.Session()

        """proxies = {
        "http": proxy[1][0],
        "https": proxy[1][0]
        }"""
        

        auth = HTTPProxyAuth(login,password)
        s.auth = auth
        proxies = {"http":"http://93.186.201.158:810"}
        s.proxies = proxies
       # Set authorization parameters globally

        #ext_ip = s.get('http://2ip.ru')
        #print(ext_ip.text)
        #Запись в файл 
        proxy = proxy[0][0]+":"+proxy[0][1]+"@"+proxy[1][0]
        file.write(proxy+"\n")
        #print(i,proxy)
"""except:
    file = open("SOCKS5.txt","w")
    file.write("Файл proxy.txt ненайден в рабочей директории.Расположите parser.exe файл вместе с файлом proxy.txt")"""


