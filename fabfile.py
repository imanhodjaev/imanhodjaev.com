# -*- coding: utf-8 -*-
from fabric.api import run, local, env, cd
from fabric.contrib.files import exists


PROJECT_NAME = 'akihiro'

env.hosts = ['85.17.25.80']
env.user = 'imanhodjaev'
env.home = '/home/%s' % env.user
env.project = '%s/webapps/%s' % (env.home, PROJECT_NAME)
env.project_url = 'https://github.com/imanhodjaev/imanhodjaev.com'
env.build_dir = '%s/build/%s' % (env.home, PROJECT_NAME)


def pull(local_run=False):
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
    if remote:
        with cd(env.build_dir):
            run('liquidluck build -v')
    else:
        local('liquidluck build -v')


def s():
    local('liquidluck server')


def make_build_dir():
    run('mkdir -p %s' % env.build_dir)


def update_static():
    with cd(env.build_dir):
        run('rm -rf %s/*' % env.project)                    # Remove old contents
        run('cp -rf %s/* %s/' % ('deploy', env.project))   # Copy generated static site into webroot


def launch():
    local('git push')
    pull()
    g(remote=True)
    update_static()
