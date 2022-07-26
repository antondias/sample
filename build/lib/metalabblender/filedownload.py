import os
import requests
import uuid

def download_from_url(url):
    print("Downloading file from url")
    path = os.makedirs("user_data", exist_ok=True)
    if (is_downloadable(url) == False):
      raise Exception("cannot download file from url. please enter valid url")
    name = url.split('/')[-1]
    newName = str(uuid.uuid4()) + ".blend"
    fileName = 'user_data/'+newName
    r = requests.get(url, allow_redirects=True)

    open(fileName, 'wb').write(r.content)
    print("File Downloaded")
    return "/content/" + fileName

def is_downloadable(url):
    h = None
    try:
      h = requests.head(url, allow_redirects=True)
    except:
      raise Exception("Cannot download file from the given url.")    
    header = h.headers
    content_type = header.get('content-type')
    print(content_type)
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True