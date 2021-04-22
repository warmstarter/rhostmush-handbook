# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'RhostMUSH Handbook'
author = 'wstarter'
copyright = '2021, wstarter'
version = '0.03a'
master_doc = 'index'

# -- General configuration ---------------------------------------------------

smartquotes = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinx.ext.todo', 'sphinx.ext.autosectionlabel'
]

todo_include_todos = True
todo_emit_warnings = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_title = "RhostMUSH Handbook"
html_static_path = ['_static']

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme_path = ['_themes']
html_theme = 'nature'
html_sidebars = {
        '**': ['searchbox.html', 'sourcelink.html', 'relations.html', 'localtoc.html'],
}
html_logo = "_static/logo.jpg"
html_style = "style.css"
html_last_updated_fmt = '%b %d, %Y'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# Include at the beginning of every file.
rst_prolog = """
.. include:: /.substitutions
"""

# Include at the end of every file.
rst_epilog = """
"""
