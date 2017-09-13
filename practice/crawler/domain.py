# processing how to distinguish domain names (from sub domains)

from urllib.parse import urlparse


# get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        # parse and get network location
        return urlparse(url).netloc
    except:
        return ''