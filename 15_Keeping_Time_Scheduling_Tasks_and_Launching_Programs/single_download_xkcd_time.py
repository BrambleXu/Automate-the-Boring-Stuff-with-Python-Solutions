# download_xkcd.py - Downloads every single XKCD comic.
# time calculate version, compare with single thread download version


import requests, os, bs4, time

page = 1
start_time = time.time()
url = 'http://xkcd.com'     #starting url
os.makedirs('xkcd_single', exist_ok=True)      # store comics in ./xkcd
while page <= 100:
    # TODO: Download the page
    print ('Downloading page %s...' % url)
    start_time = time.time()
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # TODO: Find the URL of the comic image.
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
        # TODO: Download the image.
        print('Downloading image %s...' % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

    # TODO: Save the image to ./xkcd.
    image_file = open(os.path.join('xkcd_single', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    # TODO: Get the Prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')
    page = page + 1

end_time = time.time()
print ('Done.')
print('You download 100 images and cost %s seconds' % (end_time - start_time))
