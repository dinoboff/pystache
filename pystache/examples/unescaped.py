import os

import pystache

class Unescaped(pystache.View):
    template_path = os.path.dirname(__file__)

    def title(self):
        return "Bear > Shark"
