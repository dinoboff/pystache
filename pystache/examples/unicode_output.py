# encoding: utf-8
import os

import pystache

class UnicodeOutput(pystache.View):
    template_path = os.path.dirname(__file__)

    def name(self):
        return u'Henri Poincaré'
