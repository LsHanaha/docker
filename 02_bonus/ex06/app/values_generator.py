import string
import random


def random_name():
    name = ''.join(random.choice(string.ascii_lowercase)
                   for _ in range(15)).capitalize()
    return name


prefix = ['https://', 'http://', '___']
suffix = [".com", ".net", ".ru", ",ru"]


def random_url():
    url_prefix = random.choice(prefix)
    url_body = ''.join(random.choice(string.ascii_lowercase)
                       for _ in range(8))
    url_suffix = random.choice(suffix)
    return f"{url_prefix}{url_body}{url_suffix}"
