#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import date

from minchin.pelican.plugins import autoloader

AUTHOR = "Strathcona Power Ltd"
SITENAME = "Strathcona Power"
SITEURL = ""
SITE_ROOT_URL = "/"

TIMEZONE = "America/Edmonton"

DEFAULT_LANG = "en"


# # Caching
# CACHE_CONTENT = True
# LOAD_CONTENT_CACHE = True

DEFAULT_PAGINATION = 10
# USE_PAGER = False
PAGINATOR_LIMIT = 6


# static paths will be copied under the same name
# these are relative to the base CONTENT folder
STATIC_PATHS = [
    "images",
    "../extras",
    # "css",
    # "design",
    # "js",
    # "fonts",
    # "pages/img",
    "../.gitattributes",
    "../.gitignore",
    # "../README.txt",
]

# A list of files to copy from the source to the destination
EXTRA_PATH_METADATA = {
    "../.gitattributes": {"path": ".gitattributes"},
    "../.gitignore": {"path": ".gitignore"},
    "../README.txt": {"path": "README.txt"},
    # "../extras/favicon.ico": {"path": "favicon.ico"},
    "images/strathcona-power-16x16.png": {"path": "favicon.png"},
    "../extras/BingSiteAuth.xml": {"path": "BingSiteAuth.xml"},
}

# MARKUP = ("rst", "md", "markdown", "mkd", "mdown", "html", "htm")
PATH = "content"
# OUTPUT_PATH = '../strathcona-power-website-temp/'  # default is 'output/'

# Set URL's
TAG_URL = "label/{slug}/"
TAG_SAVE_AS = "label/{slug}/index.html"
TAGS_URL = "label/"
TAGS_SAVE_AS = "label/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
CATEGORIES_URL = "category/"
CATEGORIES_SAVE_AS = "category/index.html"
ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"
AUTHORS_URL = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = "archives/index.html"
YEAR_ARCHIVE_URL = "{date:%Y}/"
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"
MONTH_ARCHIVE_URL = "{date:%Y}/{date:%m}/"
MONTH_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"


# # Add Blog to sidebar
# MENUITEMS = (
#     ("Blog", SITEURL + "/", "fa fa-fw fa-pencil"),
#     ("Genealogy", "http://minchin.ca/genealogy", "glyphicon glyphicon-tree-deciduous"),
#     ("My Projects", "http://minchin.ca/projects/", "fa fa-fw fa-flask"),
#     ("Search", "http://minchin.ca/search/", "fa fa-fw fa-search"),
#     ("About", "http://minchin.ca/about/", "fa fa-fw fa-info-circle"),
#     ("Contact Me", "http://minchin.ca/contact/", "fa fa-fw fa-envelope"),
# )

# MENUITEMS_2_AT = "Blog"
# MENUITEMS_2_AT_LINK = ""  # this is added to SITEURL

# MENUITEMS_2 = (
#     # ('Archives',  SITEURL + '/' + ARCHIVES_URL,  'fa fa-fw fa-archive'),
#     ("Labels", SITEURL + "/" + TAGS_URL, "fa fa-fw fa-tags"),
# )

# DISPLAY_PAGES_ON_MENU = False

# Theme Related
SEAFOAM_DEV_MODE = True
TYPOGRIFY = True
SITELOGO = "images/strathcona-power-250x150-white-crop.png"
SITELOGO_SIZE = "100%"
PYGMENTS_STYLE = "friendly"
DISPLAY_BREADCRUMBS = False
FAVICON = "favicon.ico"
BOOTSTRAP_THEME = "strathcona"
USE_OPEN_GRAPH = True
# CUSTOM_CSS = 'css/strathcona-power.css'
DOCUTIL_CSS = False
CUSTOM_JS_LIST = []
# update copyright date automatically
INDEX_COPY_DATE = "20{}".format(str(date.today().year)[-2:])
TAGS_TEXT = "Labels"
NAVBAR_ON_TOP = True
DISPLAY_ARCHIVES_ON_MENU = False

AVATAR = "images/strathcona-power-64x64.png"

# TEMPLATE_PAGES = {
#     "404.html": "404.html",
# }

# list categories here in lowercase
CATEGORY_IMAGES = {
    # "electricity": "images/electricity.png",
    # "natural-gas": "images/natural-gas.png",
    # "fixed-vs-floating": "images/fixed-vs-floating",
}

# Plugins
# PLUGIN_PATHS = ("../pelican-plugins",)
AUTOLOADER_NAMESPACES = autoloader.DEFAULT_NAMESPACE_LIST + [
    "pelican.plugins",
]
PLUGINS = [
    autoloader,
    "pelican_alias",
]

ASSET_CSS = False
ASSET_JS = False
NEIGHBORS = True

IMAGE_PROCESS = {
    # set for 12 col width
    "article-feature": ["scale_in 1140 1140 False"],
    "9-col": {
        "type": "picture",
        "sources": [
            {
                "name": "default",
                "srcset": [
                    (
                        "768w",
                        ["scale_in 750 562.5 True"],
                    ),  # actually 12 cols (full width) on smallest screens
                    ("992w", ["scale_in 727.5 545.5 True"]),
                    ("1200w", ["scale_in 877.5 658 True"]),
                ],
                "sizes": "100vw",
            },
        ],
        "default": ("default", "1200w"),
    },
    "index-thumbnail": {
        "type": "picture",
        "sources": [
            {
                "name": "default",
                "srcset": [
                    (
                        "768w",
                        ["scale_in 187.5 140.5 True"],
                    ),  # actually 12 cols (full width) on smallest screens
                    # 157.5
                    ("992w", ["scale_in 212.5 182 True"]),
                    ("1200w", ["scale_in 262.5 219.5 True"]),
                ],
                "sizes": "100vw",
            },
        ],
        "default": ("default", "1200w"),
    },
}
IMAGE_PROCESS_PARSER = SEAFOAM_PARSER = "html5lib"

SUMMARY_USE_FIRST_PARAGRAPH = True
SUMMARY_END_MARKER = "<!-- read more -->"

# Make things disappear
DISPLAY_CATEGORIES_ON_MENU = False
HIDE_SITENAME = True
HIDE_SIDEBAR = True
GITHUB_USER = False
ADDTHIS_PROFILE = False
DISQUS_SITENAME = False
PDF_PROCESSOR = False

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
# FEED_ATOM = None
# FEED_ALL_ATOM = None
FEED_RSS = None
FEED_ALL_RSS = None
# CATEGORY_FEED_ATOM = None
# CATEGORY_FEED_RSS = None
# AUTHOR_FEED_ATOM = None
AUTHOR_FEED_ATOM = "feeds/author.{slug}.atom.xml"
# AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = "feeds/label.{slug}.atom.xml"  # not automatically generated
# TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
# FEED_MAX_ITEMS = 0
