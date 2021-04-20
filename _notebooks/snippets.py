
import pandas as pd
import hvplot

def export_plot_fastpages(plot, filename):
    
    hvplot.save(plot, filename)
    
    import fileinput
    with open(filename, 'r') as original: data = original.read()
    with open(filename, 'w') as modified: modified.write("{% raw %}\n" + data + "\n{% endraw %}")

    for text_to_search in ["<!DOCTYPE html>", '<html lang="en">','</html>', '<head>', '</head>', '<body>','</body>']:        
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:

                    replacement_text = ""
                    print(line.replace(text_to_search, replacement_text), end='')       
                    

def export_plot_fastpages_panel(plot, filename, options=None):
    
    if options:
        plot.save(filename, **options)
    else:
        plot.save(filename)
    
    import fileinput
    with open(filename, 'r') as original: data = original.read()
    with open(filename, 'w') as modified: modified.write("{% raw %}\n" + data + "\n{% endraw %}")

    for text_to_search in ["<!DOCTYPE html>", '<html lang="en">','</html>', '<head>', '</head>', '<body>','</body>']:        
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:

                    replacement_text = ""
                    print(line.replace(text_to_search, replacement_text), end='')
