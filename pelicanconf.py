#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mustafa Ray'
SITENAME = u'Portfolio'
SITEURL = ''

PATH = './content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# MARKUP = ('md', 'ipynb')

# PLUGIN_PATH = './plugins'
MARKUP = ('md', 'pelican-ipynb')

# Path to the folder containing the plugins
PLUGIN_PATHS = ['./pelican-plugins']

# Enabled plugins
PLUGINS = ['sitemap', 'pelican-ipynb.markup', 'liquid_tags.notebook', 'liquid_tags.generic']

LIQUID_CONFIGS = (('PATH', '.', "The default path"), ('THEME', '', 'The theme in use'),
                  ('SITENAME', 'Default Sitename', 'The name of the site'), ('AUTHOR', '', 'Name of the blog author'))

 
# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]  
IPYNB_USE_METACELL = True
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True