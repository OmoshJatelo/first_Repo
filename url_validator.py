#create a program tha checks if a URL is valid

import re

def check_validity(url):
    url_pattern= r"^(https?://)(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})(/[a-zA-Z0-9#&%_.-]*)?$"

    if re.match(url_pattern,url):
        return True
    else:
        return False
  
url=input("enter a URL to check its validity\n: ").strip()
print(f"{url} : {' the URL Is valid' if check_validity(url) else ' the Url Is invalid'}")
#if check_validity(url):
    #print(f"{url} is a valid url")
#else:
   # print(f"{url} is an invalid url")    