from srs_format import db as srs_db
import json

from .jinja import env
from .util import js_once


class ReviewDeck:
    def __init__(self, deck, filter_='', **kwargs):
        self.card_ids = [c.id for c in srs_db.Card.iter_quiz(deck=deck, q_str=filter_, **kwargs)]

    def _repr_html_(self):
        return env.get_template('ReviewDeck.html').render(
            cardIdsJson=json.dumps(self.card_ids)
        )

    @staticmethod
    def get_stat():
        js_once('''
        alert(currentCardIndex + ' of ' + cardIds.length);
        ''')

    def get_current(self):
        self.get(0)

    @staticmethod
    def get(rel_index):
        js_once('''
        executePythonOutputInNextCell(`
            from srs_format import db as srs_db
            srs_card = srs_db.Card.get(id=${cardIds[currentCardIndex + (%d)]})
        `);
        ''' % rel_index)

    def __getitem__(self, item):
        return self.get(item)
