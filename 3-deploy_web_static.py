#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import local
from datetime import datetime
import os


env.hosts = ['54.152.181.77', '100.25.220.209']


def do_pack():
    """do pack"""
    if not os.path.exists("versions"):
        local("mkdir -p versions")

    now = datetime.utcnow()
    date_time = now.strftime("%Y%m%d%H%M%S")
    path_arch = "versions/web_static_{}.tgz".format(date_time)
    archive = local("tar -cvzf {} web_static".format(path_arch))

    if archive.succeeded:
        return path_arch
    else:
        return None


def do_deploy(archive_path):
    """do_deploy method"""
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


def deploy():
    """ deploy method"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
