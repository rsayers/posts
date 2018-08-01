#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rob Sayers'
SITENAME = u'RobSayers.Com'
SITEURL = 'http://www.robsayers.com'

GITHUB_URL = 'https://github.com/rsayers'
TWITTER_URL = 'https://twitter.com/rsayers'
SITETITLE = 'Rob Sayers'
SITESUBTITLE = ''
SITEDESCRIPTION = 'Assorted Geekery'
SITELOGO = 'http://www.robsayers.com/profile.png'
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = "atom.xml"
FEED_RSS = "rss.xml"

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

SOCIAL = (('linkedin', 'https://www.linkedin.com/pub/robert-sayers/4/7a9/60a'),
                    ('github', 'https://github.com/rsayers'),('twitter','http://twitter.com/rsayers'),('rss', '//www.robsayers.com/feeds/all.atom.xml'))

MAIN_MENU = True
DEFAULT_PAGINATION = 10
MENUITEMS = (('Archives', '/archives.html'),
                          ('Categories', '/categories.html'),)
ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']
THEME = "themes/motherfuckingwebsite"
