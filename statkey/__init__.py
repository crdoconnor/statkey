#!/usr/bin/env python
from __future__ import print_function
import os, sys, subprocess

DIFF_CUTOFF = 80

def print_output(output):
    """If status command output anything, then print it. Then quit."""
    if output != "":
        sys.stdout.write(output + "\n")
    sys.exit()

def mercurial_status(use_color):
    """Run hg status command and output."""
    color_appendage = ["--color", "always",] if use_color == True else []
    output = ""
    hg_diff = subprocess.check_output(["hg", "diff",] + color_appendage)
    if len(hg_diff.split('\n')) < DIFF_CUTOFF:
        output = hg_diff
    if output != "":
        output = output + u"==========\n"
    output = output + subprocess.check_output(["hg", "status",] + color_appendage).strip()
    print_output(output)

def git_status():
    """Run git status command and output."""
    output = ""
    git_diff = subprocess.check_output(["git", "diff"])
    if len(git_diff.split('\n')) < DIFF_CUTOFF:
        output = git_diff
    output = output +  subprocess.check_output(["git", "status"]).strip()
    print_output(output)

def run():
    """The main command that does everything."""
    checkdirectory = os.getcwd()

    while checkdirectory != '/':
        hgdir = "{0}{1}.hg".format(checkdirectory, os.sep)
        if os.path.exists(hgdir):
            use_color = False
            if os.path.exists("{0}{1}hgrc".format(hgdir, os.sep)):
                with open("{0}{1}.hg{1}hgrc".format(checkdirectory, os.sep), 'r') as hgrc_handle:
                    if "color =" in hgrc_handle.read():
                        use_color = True
            mercurial_status(use_color)
        elif os.path.exists("{0}{1}.git".format(checkdirectory, os.sep)):
            git_status()
        else:
            checkdirectory = os.path.abspath(os.path.join(checkdirectory, os.pardir))

    sys.stderr.write("No repo under this directory.\n")
