from urllib.parse import urlparse
from urllib.request import urlopen

f = urlopen('http://google.co.kr')
print(f.read(500).decode('utf-8'))
