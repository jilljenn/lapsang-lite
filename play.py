import random
import falcon
import json


with open('enfr.md') as f:
    fr = [line.split('::')[1] for line in f.read().splitlines()]
random.shuffle(fr)

with open('enjp.md') as f:
    jp = [line.split('::')[1] for line in f.read().splitlines()]
random.shuffle(jp)

class QuoteResource:
    def on_get(self, req, resp, order, quote_id):
        """
        Handles GET requests
        """
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
        quote_id = int(quote_id)
        pos = int(order[quote_id // 2])
        if quote_id % 2 == 0:
            sentence = jp[pos]
        else:
            sentence = fr[pos]
        resp.body = sentence


api = falcon.API()
api.add_route('/quote/{order}/{quote_id}', QuoteResource())
