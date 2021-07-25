import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
import requests

class ScraperFromLink():

    def __init__(self, url):
        self.url = url
        self.tag_lib = []
        self.link_lib = []
        self.paragraphs = []
        self.content = []
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/87.0.4280.141 Safari/537.36',
            'Accept-Language': 'en-gb', 'Accept-Encoding': 'br, gzip, deflate',
            'Accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Referer': 'http://www.google.com/'}

    def list_to_string(self, bs4_content):
        str1 = " "
        return (str1.join(bs4_content))

    def get_link(self, type, name, lookup):
        www = urllib.request.urlopen(self.url, context=self.ctx).read()
        soup = BeautifulSoup(www, 'html.parser')
        div = soup.find_all(type, name)
        for elem in div:
            self.paragraphs.append(str(elem))
        soup = BeautifulSoup((self.list_to_string(self.paragraphs)), 'html.parser')
        tags = soup('a')
        for tag in tags:
            self.tag_lib.append(tag.get('href', None))
        for tag in self.tag_lib:
            if lookup in tag:
                self.link_lib.append(lookup)





def iterate_scraper(lenght, first_url, lookup, site, name):
    content = []
    links = []
    for i in range(lenght):
        obj1 = ScraperFromLink(first_url)
        obj1.get_link("div", {"class": "topictitle"})
        obj1.get_content_ncbr_link()
        content.extend(obj1.content)
        links.extend(obj1.link_lib)
        obj2 = ScraperFromLink(first_url)
        obj2.get_link("li", {"class": "last next"}, site, name)
        first_url = obj2.link_lib[0]
        print("x")
    return content, links

if __name__ == '__main__':
    iterate_scraper()
