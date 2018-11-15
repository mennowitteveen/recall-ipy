from srs_format import api as srs_api
import json
from IPython.display import HTML

from .jinja import env


def show_decks(filter_='', max_depth=3):
    return HTML(env.get_template('ShowDecks.html').render(
        deckDict=json.dumps(
            srs_api.get_deck_dict(filter_=filter_),
            ensure_ascii=False, indent=2
        ),
        maxDepth=max_depth,
        filter=filter_
    ))
