import os

import pystache

class Simple(pystache.View):
    template_path = os.path.dirname(__file__)

    def thing(self):
        return "pizza"

    def blank(self):
        pass
