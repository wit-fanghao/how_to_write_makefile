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

project = 'Makefile'
copyright = '2022, wit_fanghao'
author = 'fanghao'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '0.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# 扩展
extensions = [
    'myst_parser',
    'sphinx_markdown_tables', # table
    'sphinx.ext.autodoc',
#   'sphinxcontrib.mermaid',  # 绘制流程图，该插件貌似需要连接外网，否则无法打开网页或异常卡顿，先屏蔽
]

# 解决锚点报错的问题
# 解决报错：WARNING: 'myst' reference target not found: #在线转换
myst_heading_anchors = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'
#source_encoding = 'gb2312'
source_encoding = 'utf-8'
html_output_encoding = 'utf-8'

# html_search_language = 'en' 保证搜索时可以搜索到中文，两个(包含两个)以上无法搜索的问题得修改 searchtools.js
html_search_language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# 主题01：sphinx_rtd_theme  
# 主题02：sphinxdoc
# 主题03：sphinx_book_theme
html_theme = 'sphinx_rtd_theme'


# 依赖 html_static_path
# 主题01重载：sphinx_rtd_theme_overide.css  
# 主题02重载：sphinxdoc_overide.css
html_static_path = ['_static']
if html_theme == 'sphinx_rtd_theme':
    html_css_files = ["sphinx_rtd_theme/sphinx_rtd_theme_overide.css"]
elif html_theme == 'sphinxdoc':
    html_css_files = ["sphinxdoc/sphinxdoc_overide.css"]
elif html_theme == 'sphinx_book_theme':
    html_css_files = ["sphinx_book_theme/sphinx_book_theme_overide.css"]

# 依赖 html_static_path
html_js_files = ['searchtools.js']