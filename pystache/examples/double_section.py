import os

import pystache

class DoubleSection(pystache.View):
    template_path = os.path.dirname(__file__)

    def t(self):
        return True

    def two(self):
        return "second"
