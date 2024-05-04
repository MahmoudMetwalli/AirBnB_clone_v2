#!/usr/bin/python3
"""To deploy file on the server"""
from os.path import exists
from fabric.operations import put, run, env
env.hosts = ["54.173.91.227", "3.85.1.149"]


def do_deploy(archive_path):
    """To deploy file on the server"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm -f /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -sf {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False
