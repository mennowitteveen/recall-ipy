from uuid import uuid4
from IPython.display import HTML, display

from .jinja import env


# noinspection PyTypeChecker
def js_once(js_string):
    uuid = uuid4()

    display(HTML(env.get_template('jupyter.js.html').render() + f'''
    <script id={uuid}>
    {js_string}
    $('#{uuid}').remove();
    </script>
    '''))
