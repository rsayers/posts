#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rob Sayers'
SITENAME = u'RobSayers.Com'
SITEURL = 'http://www.robsayers.com'
GITHUB_URL = 'https://github.com/rsayers'
TWITTER_URL = 'https://twitter.com/rsayers'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = "atom.xml"
FEED_RSS = "rss.xml"

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
##         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']
THEME = "themes/monospace"
