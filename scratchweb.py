import urllib

def fetchWebPage(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

htmlContent = fetchWebPage("http://www.baidu.com")
print(htmlContent)