def generate_latex_table(data):
    def format_cell(cell):
        return str(cell).\
            replace('&', r'\&').\
            replace('%', r'\%').\
            replace('#', r'\#').\
            replace('_', r'\_').\
            replace('$', r'\$').\
            replace('{', r'\{').\
            replace('}', r'\}')
    
    def format_row(row):
        return ' & '.join(format_cell(cell) for cell in row) + r' \\'
    
    latex_table = r'\begin{tabular}{|' + '|'.join('c' * len(data[0])) + '|}'
    for row in data:
        latex_table += '\n\\hline\n' + format_row(row)
    latex_table += '\n\\hline\\end{tabular}'
    
    return latex_table
