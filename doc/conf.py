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
import os
import sys
import glob
#import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'M05_miniProject'
copyright = '2023, Cedric Lienhard & Mustapha Al-Dabboussi'
author = 'Cedric Lienhard & Mustapha Al-Dabboussi'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	"sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.graphviz",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx_rtd_theme",
]



# Generates auto-summary automatically
autosummary_generate = True

# Create numbers on figures with captions
numfig = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["links.rst", "README.rst"]


# Some variables which are useful for generated material
project_variable = project.replace(".", "_")
short_description = u"M05 mini-project about reproducibility"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"



# Add any paths that contain custom static files (such as style sheets) here,
# relative to 	this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# Output file base name for HTML help builder.
htmlhelp_basename = project_variable + u"_doc"

# -- Post configuration --------------------------------------------------------



intersphinx_mapping = dict(
    python=('https://docs.python.org/3', None),
    numpy=("https://numpy.org/doc/stable/", None),
    scipy=("https://docs.scipy.org/doc/scipy/reference", None),
)
