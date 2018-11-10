from srs_format import api as srs_api
from IPython.display import HTML

from .deck import show_decks


def init(filename):
    srs_api.init(filename)
    return HTML(show_decks())
