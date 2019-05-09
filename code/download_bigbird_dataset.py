import config
import requests, bs4, urllib, os

dest_dir = os.path.join(config.DATASET_DIR, 'model_zip')
queries_dir = os.path.join(config.DATASET_DIR, 'queries_zip')

url = 'http://rll.berkeley.edu/bigbird/aliases/a47741b172/'

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
if not os.path.exists(queries_dir):
    os.makedirs(queries_dir)

page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'html.parser')

download_links = [x.get('href') for x in soup.find_all('a') if x.get_text() == 'High res (.tgz)']
for d in download_links:
    urllib.urlretrieve(url + d, os.path.join(dest_dir, d.split('/')[-2] + '.tgz'))

download_links = [x.get('href') for x in soup.find_all('a') if x.get_text() == 'RGB-D (.tgz)']
for d in download_links:
    urllib.urlretrieve(url + d, os.path.join(queries_dir, d.split('/')[-2] + '.tgz'))
