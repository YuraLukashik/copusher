# /usr/bin/env python

import sys
import pyperclip
import importlib

default_config = {
    'storage': 'github_gist'
}

storage_module = importlib.import_module("storages." + default_config['storage'])
storage = storage_module.Storage()

content = ""

for line in sys.stdin:
    content += line

uri = storage.store(content)

pyperclip.copy(uri)
print(uri)
