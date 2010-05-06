import os

import pystache

class ComplexView(pystache.View):
    template_path = os.path.dirname(__file__)

    def header(self):
        return "Colors"

    def item(self):
        items = []
        items.append({ 'name': 'red', 'current': True, 'url': '#Red' })
        items.append({ 'name': 'green', 'link': True, 'url': '#Green' })
        items.append({ 'name': 'blue', 'link': True, 'url': '#Blue' })
        return items

    def list(self):
        return not self.empty()

    def empty(self):
        return len(self.item()) == 0
