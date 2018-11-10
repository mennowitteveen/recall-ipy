from srs_format import db as srs_db
import json

from .jinja import env


class ReviewDeck:
    def __init__(self, deck, **kwargs):
        self.card_ids = [c.id for c in srs_db.Card.iter_quiz(deck=deck, **kwargs)]

    def _repr_html_(self):
        return env.get_template('ReviewDeck.html').render(
            cardIdsJson=json.dumps(self.card_ids)
        )
