import os

import pystache

class Comments(pystache.View):
    template_path = os.path.dirname(__file__)

    def title(self):
        return "A Comedy of Errors"
