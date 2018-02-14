# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.
# time calculate version, compare with single thread download version

import requests, os, bs4, threading, time

os.makedirs('xkcd_my', exist_ok=True)  # store comics in ./XKCD

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % (url_number))
        res = requests.get('http://xkcd.com/%s' % (url_number))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml')

        # Find the URL of the comic image.
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('Could not find comic image.')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()

            # Save the image to ./xkcd.
            image_file = open(os.path.join('xkcd_my', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

start_time = time.time()
print ('start time is %s' % (start_time))
download_xkcd(1, 101)

# # TODO: Create and start the Thread objects.
# download_threads = []   # a list of all the Thread objects
# start_time = time.time()
# for i in range(1, 101, 10):   # loops 14 times, creates 14 threads
#     download_thread = threading.Thread(target=download_xkcd, args=(i, i+10))
#     download_threads.append(download_thread)
#     download_thread.start()
#
# # TODO: Wait for all threads to end.
# for download_thread in download_threads:
#     download_thread.join()

end_time = time.time()
print('Done.')
print('You download 100 images and cost %s seconds' % (end_time - start_time))
