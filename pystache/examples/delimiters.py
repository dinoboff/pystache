import os

import pystache

class Delimiters(pystache.View):
    template_path = os.path.dirname(__file__)

    def first(self):
        return "It worked the first time."

    def second(self):
        return "And it worked the second time."

    def third(self):
        return "Then, surprisingly, it worked the third time."
