import re
import urllib.request

class WebBrowser:
    instances = {}

    def __new__(cls, *args, **kwargs):
        url = args[0]
        if url in cls.instances:
            return cls.instances[url]
        return super().__new__(cls)

    def __init__(self, url):
        self.url = url
        self.__text = None
        self.__links = None
        self.instances.update({url: self})

    @property
    def text(self):
        if self.__text == None:
            req = urllib.request.urlopen(self.url)
            html = req.read()
            self.__text = html.decode('utf-8')
        return self.__text

    @property
    def links(self):
        if self.__links == None:
            pat = 'href="(http://.*?)"'
            links = re.findall(pat, self.text)
            self.__links = [WebBrowser(link) for link in links]
        return self.__links


    def __repr__(self):
        return "\033[31;2m" + self.url + "\033[0m"



wb1 = WebBrowser("http://www.python.org")
wb2 = WebBrowser("http://www.python.org")

try:
    print(wb1.links[1].links)
except urllib.error.URLError:
    print("cannot open page")

#
# for i in range(10):
#     t3 = time.time()
#     text2 = wb1.text
#     t4 = time.time()
#
#     print("read text     time = {}".format(t4-t3))

