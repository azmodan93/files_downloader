import requests
import argparse
from helpers import save_file
from bs4 import BeautifulSoup

# Argparse definition
parser = argparse.ArgumentParser(
    description='Download all files from links on a website', prog='main.py')
parser.add_argument('--url', help='url for search', dest='url', required=True)
parser.add_argument('--output-folder', dest='output_folder',
                    help='folder where files will be stored', required=False, default='output')

args = parser.parse_args()
url = args.url
output_folder = args.output_folder

if __name__ == '__main__':
    webpage = BeautifulSoup(requests.get(
        url, allow_redirects=True).content, "html.parser")

    for a_tag in webpage.findAll("a"):
        link = a_tag.attrs.get("href")
        if link != "" or link is not None:
            downloaded_file = requests.get(f'{url}{link}')
            if(downloaded_file.headers['Content-Type'] in ['application/pdf', 'text/plain']):
                print(f'File to be downloaded: {link}')
                save_file(downloaded_file.content, f'{output_folder}/{link}')
                print('File downloaded successfully')
            else:
                print('This link cannot be downloaded. Only pdf and txt')
        else:
            print("The link is empty")
