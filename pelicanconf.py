AUTHOR = 'Josh Sawyer'
SITENAME = 'Stumpside Cottage'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

SITEURL = 'https://www.stumpsidecottage.com'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = '../stumpside-cottage-theme'

# this can be changed to true at some point
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".hg", ".git", ".bzr", "CNAME", ".gitignore", "README.md", ".nojekyll"]

OUTPUT_PATH = '../stumpside-cottage/'

from datetime import date
CURRENTYEAR = date.today().year


ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'

MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

CATEGORY_SAVE_AS = 'categories/{slug}.html'
CATEGORY_URL = 'categories/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAG_URL = 'tags/{slug}.html'

IGNORE_FILES = ['*.unpublished']