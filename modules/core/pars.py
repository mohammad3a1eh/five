
def check_url(website_url):
    if not website_url.startswith(('http://', 'https://')):
        website_url = 'http://' + website_url

    return website_url.rstrip('/')

