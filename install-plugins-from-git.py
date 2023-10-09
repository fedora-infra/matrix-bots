#!/usr/bin/env python3

import os
import shutil
from argparse import ArgumentParser
from contextlib import contextmanager
from pathlib import Path
from urllib.parse import urlparse
from subprocess import run
from tempfile import TemporaryDirectory


def run_cmd(cmd):
    return run(cmd, check=True, text=True)


@contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(previous_dir)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-b", "--branch", help="Branch to checkout")
    parser.add_argument("-o", "--output", help="Maubot's plugin directory")
    parser.add_argument("git_url", nargs="+", help="Git URL to checkout")
    return parser.parse_args()


def install_plugin(git_url, branch, output):
    cmd = ["git", "clone", "--depth", "1", "--single-branch", git_url]
    if branch:
        cmd[2:2] = ["-b", branch]
    run_cmd(cmd)
    clone_dir = Path(urlparse(git_url).path).stem
    with pushd(clone_dir):
        os.mkdir("build")
        run(["mbc", "build", "-o", "build"])
        for plugin in Path("build").glob("*.mbp"):
            shutil.move(plugin, output)


if __name__ == "__main__":
    args = parse_args()
    with TemporaryDirectory() as tmpdirname:
        with pushd(tmpdirname):
            for git_url in args.git_url:
                install_plugin(git_url, args.branch, args.output)
