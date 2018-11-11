from srs_format import api as srs_api

from .util import js_once


def init(filename):
    srs_api.init(filename)

    return js_once('''
    executePythonOutputInNextCell(`
        from recall_ipy.deck import show_decks
        show_decks()
    `)
    ''')
