# В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
# (например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
# домен выделен полужирным).

import re

with open('radio_stations.txt', encoding='utf-8') as f:
    lines = f.readlines()

p = r'https?://([^/:]+)'

domains = []
for line in lines:
    matches = re.findall(p, line)
    for match in matches:
        domains.append(match)

print('Найдены домены: ')
for domain in domains:
    print(domain)