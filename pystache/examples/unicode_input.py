import os

import pystache

class UnicodeInput(pystache.View):
    template_path = os.path.dirname(__file__)
    template_encoding = 'utf8'

    def age(self):
        return 156
