from srs_format import api as srs_api

from .util import js_once


def init(filename, silent=False):
    srs_api.init(filename)

    if not silent:
        js_once('''
        executePythonOutputInNextCell(`
            from recall_ipy.deck import show_decks
            show_decks()
        `);
        ''')
