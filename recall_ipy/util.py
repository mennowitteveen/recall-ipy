from IPython.display import HTML, display

from .jinja import env


# noinspection PyTypeChecker
def js_once(js_string):
    display(HTML(env.get_template('jupyter.js.html').render() + '''
    <script>
    var nb = Jupyter.notebook;
    var anchorIndex = nb.get_anchor_index();
    var nbCell = nb.get_cell(anchorIndex - 1);
    %s
    setTimeout(function(){
        Jupyter.notebook.get_cell(nb.find_cell_index(nbCell)).clear_output();
    }, 1000);
    
    </script>
    ''' % js_string))
