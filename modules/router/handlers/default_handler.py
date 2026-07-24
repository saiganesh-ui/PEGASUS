from modules.router.base_handler import BaseHandler


class DefaultHandler(BaseHandler):

    def execute(self, decision):

        return decision