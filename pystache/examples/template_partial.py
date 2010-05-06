import os

import pystache

class TemplatePartial(pystache.View):
    template_path = os.path.dirname(__file__)

    def title(self):
        return "Welcome"

    def title_bars(self):
        return '-' * len(self.title())
