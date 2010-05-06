import os

import pystache

class Inverted(pystache.View):
    template_path = os.path.dirname(__file__)

    def t(self):
        return True

    def f(self):
        return False

    def two(self):
        return 'two'
