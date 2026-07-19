"""
Status Handler
Project PEGASUS
"""

import random
from modules.nlp.responses import RESPONSES

from modules.router.base_handler import BaseHandler


class StatusHandler(BaseHandler):
   def execute(self, decision):

        return {

            "type": "response",

            "message": random.choice(
                RESPONSES["status"]
            )

        }