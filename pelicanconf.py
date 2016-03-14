#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Arthur Vincent Simon'
SITENAME = u'Arthur Vincent Simon'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Manila'

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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

##############################
DELETE_OUTPUT_DIRECTORY = False

TEMPLATE_PAGES = {
    'projects.html': 'projects.html',
    'contact.html': 'contact.html'
}

THEME = './themes/arvinsim'

# Data
EXPERIENCE_HISTORY = [
    {
        'job_title': u'Frontend Web Developer',
        'company_name': u'Innovuze Solutions Inc.',
        'tool_tags': ['reactjs', 'redux', 'python', 'django', 'javascript', 'html', 'css', 'git']
    },
    {
        'job_title': u'Freelance Web Developer',
        'company_name': u'',
        'tool_tags': ['php', 'svn', 'html', 'css', 'javascrpt', 'jquery', 'mysql', 'codeigniter', 'knockout.js',
                      'expressionengine', 'twitter-bootstrap']
    },
    {
        'job_title': u'Junior Web Developer',
        'company_name': u'Global Digital Services Inc.',
        'tool_tags': ['html', 'css', 'javasacript', 'mootools', 'php', 'mysql', 'svn', 'joomla']
    }
]

ACADEMIC_ATTAINMENT = [
    {
        'degree': 'B.S. Computer',
        'school': 'Xavier University',
        'tags': {
            'tools': ['Java', 'Python', 'PHP', 'Ruby', 'HTML', 'CSS', 'Javascript']
        }
    }
]

