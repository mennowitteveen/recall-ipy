from srs_format import db as srs_db
import json

from .jinja import env
from .util import js_once


class ReviewDeck:
    def __init__(self, deck, **kwargs):
        self.card_ids = [c.id for c in srs_db.Card.iter_quiz(deck=deck, **kwargs)]

    def _repr_html_(self):
        return env.get_template('ReviewDeck.html').render(
            cardIdsJson=json.dumps(self.card_ids)
        )

    @property
    def current(self):
        return js_once('''
        alert(currentCardIndex + ' of ' + cardIds.length);
        ''')

    @staticmethod
    def get_current():
        return js_once('''
        executePythonOutputInNextCell(`
            from srs_format import db as srs_db
            srs_card = srs_db.Card.get(id=${cardIds[currentCardIndex]})
        `)
        ''')
