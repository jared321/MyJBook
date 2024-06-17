# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import json

from stuff import __version__

project = 'stuff'
copyright = "2024, Me"
author = "Me"
version = __version__
release = version

latex_packages = [
    'xspace',
    'mathtools',
    'amsfonts', 'amsmath', 'amssymb', 'amsthm'
]
latex_macro_files = ['base', 'notation']

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# General
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.todo',
              'sphinx.ext.mathjax',
              'sphinxcontrib.bibtex']
numfig = True

# Extensions
autoclass_content = "init"
autodoc_member_order = "bysource"

autosectionlabel_prefix_document = True

todo_include_todos = True

mathjax3_config = {
    'loader': {},
    'tex': {
        'macros': {}
    }
}

bibtex_bibfiles = ['stuff.bib']

# -- Options for Math --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-math

math_numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']

# -- LaTeX configuration -----------------------------------------------------
# Some of this configuration is from
# https://stackoverflow.com/questions/9728292/creating-latex-math-macros-within-sphinx

latex_engine = "pdflatex"
latex_elements = {
    "papersize": "letterpaper",
    "pointsize": "10pt",
    "preamble": ""
}
for package in latex_packages:
    latex_elements['preamble'] += f'\\usepackage{{{package}}}\n'
