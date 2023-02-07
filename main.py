from urllib.request import urlopen
url = "https://webstersdictionary1828.com/Dictionary/Abaddon"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
