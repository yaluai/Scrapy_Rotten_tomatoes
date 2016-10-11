import urllib
import json
import csv

num = 3000
base_url = 'https://www.rottentomatoes.com'
link_set = []

i = 1

while True:
    link = '/api/private/v1.0/m/list/find?page=' + str(i) + '&limit=100&type=dvd-all&services=amazon%3Bamazon_prime%3Bflixster%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu&sortBy=release'

    sock = urllib.urlopen(base_url + link)
    html = sock.read()
    sock.close()

    js = json.loads(unicode(html, errors='ignore'))

    # print html

    for result in js['results']:

        data = dict()
        data['runtime'] = result['runtime']
        data['popcornScore'] = result['popcornScore']
        data['title'] = result['title']
        data['mpaaRating'] = result ['mpaaRating']
        data['theaterReleaseDate'] = result['theaterReleaseDate']
        data['tomatoIcon']=result['tomatoIcon']
        data['actors'] = ''
        for actor in result['actors']:
            data['actors'] += actor



        link_set.append(data)
        if len(link_set) >= num:
            break

    if len(link_set) >= num:
        break

    print len(link_set)

    i += 1

with open('tomato.csv', 'wb') as csvfile:
    fieldnames = ['title', 'runtime', 'popcornScore', 'theaterReleaseDate','actors','tomatoIcon','mpaaRating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for link in link_set:
        writer.writerow(link)