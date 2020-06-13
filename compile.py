import os
os.system( 'python clean.py' ) 
os.system( 'pdflatex master.tex' )
os.system( 'bibtex master.aux' )
os.system( 'pdflatex master.tex' )
os.system( 'pdflatex master.tex' )
