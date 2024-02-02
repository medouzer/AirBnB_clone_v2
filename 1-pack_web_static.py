#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import local
from datetime import datetime
import os


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
