from list2tex import generate_latex_table


def generate_latex(*content):
    latex_template_begin = r'''\documentclass{article}
\usepackage{graphicx} % Required for inserting images

\title{ProPython_hw02}
\author{zibumzibumich }
\date{March 2024}

\begin{document}

\maketitle
'''
    latex_template_end = r'''

\section{Introduction}

\end{document}
'''
    return latex_template_begin+'\n\n'.join(content)+latex_template_end
    


if __name__ == "__main__":
    data = [
        ['Name', 'Age', 'Gender'],
        ['John', 30, 'Male'],
        ['Alice', 25, 'Female'],
        ['Bob', 35, 'Male']
    ]
    print(
        generate_latex(
            generate_latex_table(data=data), 
            generate_latex_table(data=data[::-1])))
    
