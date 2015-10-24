import sys
import pyperclip
import importlib
import optparse

class Copusher:
    def __init__(self):
        self.config = {
            'storage': 'github_gist'
        }

    def run(self):
        storage_module = importlib.import_module("storages." + self.config['storage'])
        storage = storage_module.Storage()

        p = optparse.OptionParser()
        p.add_option("-f", action="store", dest="filename")
        p.set_defaults(filename = "my_terminal_output.txt")
        opts, args = p.parse_args()

        content = ""

        for line in sys.stdin:
            content += line

        uri = storage.store(opts.filename, content)

        pyperclip.copy(uri)
        print(uri)
