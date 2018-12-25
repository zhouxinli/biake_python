import urllib.request
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


#print(urllib)
class HtmlDownloader(object):
    def download(self,url):
        #print("xinli:%s" %(url))
        if url is None:
            return None
        response=urllib.request.urlopen(url)
        #print(response.getcode())
        if response.getcode()!=200:
            return None
        #print(200)
        return response.read()
