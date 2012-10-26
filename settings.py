# -*- coding: utf-8 -*-
#: settings for liquidluck

#: site information
#: all variables can be accessed in template with ``site`` namespace.
#: for instance: {{site.name}}
site = {
    "name": "Sultan",  # your site name
    "url": "http://imanhodjaev.com",  # your site url
    # "prefix": "blog",
}

#: this config defined information of your site
#: 1. where the resources  2. how should the site be generated
config = {
    "source": "content",
    "output": "deploy",
    "static": "deploy/static",
    "static_prefix": "/static/",
    "permalink": "{{date.year}}/{{filename}}.html",
    "relative_url": False,
    "perpage": 30,
    "feedcount": 20,
    "timezone": "+06:00",
}


author = {
    "default": "akihiro",
    "vars": {
        "akihiro": {
            "name": "Sultan Imanhodjaev",
            "website": "http://imanhodjaev.com",
            "email": "sultan@imanhodjaev.com",
        }
    }
}

#: active readers
reader = {
    "active": [
        "liquidluck.readers.markdown.MarkdownReader",
        # uncomment to active rst reader.
        # but you need to install docutils by yourself
        # "liquidluck.readers.restructuredtext.RestructuredTextReader",
    ],
    "vars": {}
}

#: active writers
writer = {
    "active": [
        "liquidluck.writers.core.PostWriter",
        "liquidluck.writers.core.PageWriter",
        "liquidluck.writers.core.ArchiveWriter",
        "liquidluck.writers.core.ArchiveFeedWriter",
        "liquidluck.writers.core.FileWriter",
        "liquidluck.writers.core.StaticWriter",
        "liquidluck.writers.core.YearWriter",
        "liquidluck.writers.core.CategoryWriter",
        "liquidluck.writers.core.CategoryFeedWriter",
        "liquidluck.writers.core.TagWriter",
        "liquidluck.writers.core.TagCloudWriter",
    ],
    "vars": {
        #"archive_output": "archive/index.html",
    }
}

#: theme variables
theme = {
    "name": "default",

    # theme variables are defined by theme creator
    # you can access theme in template with ``theme`` namespace
    # for instance: {{theme.disqus}}
    "vars": {
        "navigation": [
            {"name": "About", "link": "/about/"},
            {"name": "Projects", "link": "/projects/"},
        ],
        'descriptions': {
            'life': u'生命是一襲華美的袍，爬滿了虱子 －－ 張愛玲',
            'work': 'works in python, javascript, vim, and everything else'
        },
        #"disqus": "your_short_name",
        "analytics": "UA-35887744-1",
    }
}

#: template variables
template = {
    "vars": {},
    "filters": {},
}