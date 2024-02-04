#!/usr/bin/python3
"""Deploy archive!"""
from fabric.api import *
from os.path import exists


env.hosts = ['54.152.181.77', '100.25.220.209']


def do_deploy(archive_path):
    """do_deploy class"""
    if not exists(archive_path):
        return False
    file_arch = archive_path.split('/')[-1]
    name_arch = file_arch.split('.')[0]
    tmp_path = "/tmp/{}".format(file_arch)
    release_path = "/data/web_static/releases/{}".format(name_arch)
    current_path = "/data/web_static/current"
    put(archive_path, tmp_path)
    run("mkdir -p {}".format(release_path))
    run("tar -xzf {} -C {}".format(tmp_path, release_path))
    run("rm {}".format(tmp_path))
    run("mv {}/web_static/* {}".format(release_path, release_path))
    run("rm -rf {}/web_static".format(release_path))
    run("rm -rf {}".format(current_path))
    run("ln -s {} {}".format(release_path, current_path))
    return True
