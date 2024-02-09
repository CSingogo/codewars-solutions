'''

Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"

'''

## solution

def remove_url_anchor(url):
    for char in url:
        if char == '#':
            i = url.index('#')
            return url[0:i]
        else:
            continue
    return url