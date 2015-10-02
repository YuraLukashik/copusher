import sys
import pyperclip
import importlib

class Copusher:
    def __init__(self):
        self.config = {
            'storage': 'github_gist'
        }

    def run(self):
        storage_module = importlib.import_module("copusher.storages." + self.config['storage'])
        storage = storage_module.Storage()

        content = ""

        for line in sys.stdin:
            content += line

        uri = storage.store(content)

        pyperclip.copy(uri)
        print(uri)
