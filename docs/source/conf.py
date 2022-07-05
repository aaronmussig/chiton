import os
import sys
from datetime import datetime
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('../..'))
from chiton import __author__, __version__, __title__, __url__

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


# The full version, including alpha/beta/rc tags
release = __version__
project = __title__
copyright = f'{datetime.now().year}, {__author__}'
author = __author__

# The full version, including alpha/beta/rc tags
version = __version__

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

github_url = __url__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon',
              'sphinx_rtd_theme', 'sphinx_autodoc_typehints'     ]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

autodoc_typehints = 'none'
autodoc_typehints_format = 'short'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme_options = {# 'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False, 'logo_only': False, 'display_version': True,
    'prev_next_buttons_location': 'bottom', 'style_external_links': False, 'vcs_pageview_mode': '',
    'style_nav_header_background': 'white', # Toc options
    'collapse_navigation': True, 'sticky_navigation': True, 'navigation_depth': 4, 'includehidden': True,
    'titles_only': False}

#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_style = 'css/custom.css'

html_context = {'display_github': True, 'github_user': 'aaronmussig', 'github_repo': 'chiton',
    'github_version': 'master/docs/source/'}