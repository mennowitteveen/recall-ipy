from srs_format import db as srs_db
import json
from IPython.display import HTML

from .jinja import env


def show_decks(max_depth=3):
    return HTML(env.get_template('ShowDecks.html').render(
        deckDict=json.dumps(
            srs_db.Deck.get_deck_dict(),
            ensure_ascii=False, indent=2,
            default=lambda o: o.id
        ),
        maxDepth=max_depth
    ))
