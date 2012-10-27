# What is Liquidluck

- date: 2012-10-27
- category: liquidluck
- tags: tech, python, liquidluck

------

So far I considered dosens of static blog generation engines [Pelican][], [Hyde][], [Jekyll][]
(even [more][] list of static website generation engines) and finally chosed [Liquidluck][].


### Criterias for the engine:

1. Easy to startup
2. Easy to use
3. Support for Markdown
4. Theming features
5. Simple documentation
6. Stable


Now I'll describe how I bootstrapped my blog using [Liquidluck][] with regard to the criterias enlisted above


### So simple to startup a new blog

Its really cool and comfortable for me to execute one command and fill out a few options to startup a new blog.
Only three options on startup you need to fill out unlike when you use [Pelican][] and it buys me.

````sh
(akihiro)ninja blog: liquidluck init
Enable Livereload Server by installing tornado
Select a config format ([yaml], python, json):
posts folder (content):
output folder (deploy):
````


### Easy to generate and view you static blog

A single command to generate the entire blog

````sh
(akihiro)ninja akihiro: liquidluck build -v
````

The output of the command will look like

````sh
Enable Livereload Server by installing tornado
[I 121026 21:38:44 generator:88] Load Settings Finished
[D 121026 21:38:44 markdown:48] read blog-engine.md
[D 121026 21:38:44 markdown:48] read hello.md
[D 121026 21:38:44 markdown:48] read about/index.md
[D 121026 21:38:44 markdown:48] read projects/index.md
[I 121026 21:38:44 generator:122] Load Posts Finished
[D 121026 21:38:44 base:65] write 2012/blog-engine.html
[D 121026 21:38:44 base:65] write 2012/hello.html
[I 121026 21:38:44 base:47] PostWriter Finished
````


### Built-in dev-server
[Liquidluck][] has a built in dev server which is really great when you prepare new articles.
Though you still can manually open **index.html** file using your browser.

````sh
(akihiro)ninja akihiro: liquidluck server
Enable Livereload Server by installing tornado
[I 121026 21:40:22 generator:88] Load Settings Finished
[I 121026 21:40:22 server:298] Start server at 127.0.0.1:8000
````

### Deployment

I host my blog at <http://webfaction.com> and the sources of this blog are on [GitHub][].
To deploy changes I use [Fabric][] below how my fabfile looks

````python
# -*- coding: utf-8 -*-
from fabric.api import run, local, env, cd
from fabric.contrib.files import exists


PROJECT_NAME = 'akihiro'

env.hosts = ['URL']
env.user = 'USER'
env.home = '/home/%s' % env.user
env.project = '%s/webapps/%s' % (env.home, PROJECT_NAME)
env.project_url = 'https://github.com/imanhodjaev/imanhodjaev.com'
env.build_dir = '%s/build/%s' % (env.home, PROJECT_NAME)


def pull(local_run=False):
    """ Pulls changes from GitHub """
    if local_run:
        local('git pull')
    else:
        if not exists(env.build_dir):
            make_build_dir()

        with cd(env.build_dir):
            if not exists('%s/.git' % env.build_dir):
                run('git clone %s %s' % (env.project_url, env.build_dir))
            else:
                run('git pull')


def g(remote=False):
    """
    Used to generate static pages
    :param remote:
        Specifies whether to generate pages locally or on remote host
    """

    if remote:
        with cd(env.build_dir):
            run('liquidluck build -v')
    else:
        local('liquidluck build -v')


def server():
    local('liquidluck server')


def make_build_dir():
    run('mkdir -p %s' % env.build_dir)


def update_static():
    """ Removes old contents and puts newly generated contents """
    with cd(env.build_dir):
        run('rm -rf %s/*' % env.project)                    # Remove old contents
        run('cp -rf %s/* %s/' % ('deploy', env.project))    # Copy generated static site into webroot


def deploy():
    """ Makes deployment, pulls from GitHub and updates contents """
    pull()
    g(remote=True)
    update_static()
````


### Themes

You can find some basic [themes][] at <http://lab.lepture.com/liquidluck/>.
[Liquidluck][] uses [Jinja2][] templating engine so it is not so hard to render a new theme if you wish one.

To install a theme just type

````sh
(akihiro)ninja akihiro: liquidluck install moment -g
````
option "g" for global installation


### Committing & publishing changes
All contents are stored at [GitHub][].
When need to publish new post, article etc. I

1. commit and push changes to [GitHub][] repo
2. execute fab deploy command

Thats it!


I'm pretty happy with [Liquidluck][] so far.


Enjoy!


[themes]: https://github.com/lepture/liquidluck/wiki/Themes
[jinja2]: http://jinja.pocoo.org/docs/
[Fabric]: http://fabfile.org
[GitHub]: https://github.com/imanhodjaev/imanhodjaev.com
[hyde]: http://ringce.com/hyde "Hyde"
[jekyll]: https://github.com/mojombo/jekyll
[pelican]: http://pelican.notmyidea.org "Pelican"
[liquidluck]: http://lab.lepture.com/liquidluck/ "Felix Felicis"
[more]: http://iwantmyname.com/blog/2011/02/list-static-website-generators.html
