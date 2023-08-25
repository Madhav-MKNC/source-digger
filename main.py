#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import system as cmd
import sys

USAGE = """
USAGE:
$ `python main.py URL_TO_THE_REPO`
$ `python main.py PATH_TO_THE_DIR`

EXAMPLES:
$ `python main.py https://github.com/Madhav-MKNC/source-digger.git`
$ `python main.py https://github.com/Madhav-MKNC/source-digger`
$ `python main.py /home/madhav/projects/source-digger/`
$ `python main.py D:/Projects/source-digger/`

NOTE:
* `PATH_TO_THE_DIR` should be an absolute path, relative paths might not work if not set correctly
* For `URL_TO_THE_REPO` only this format works in currect version: `https://github.com/USERNAME/REPO.git`
"""

BANNER = """[Github: Madhav-MKNC/source-digger]
###################################
##    WE DIG YOUR SOURCE CODE    ##
###################################
"""

regex= "((http|git|ssh|http(s)|file|\/?)|(git@[\w\.]+))(:(\/\/)?)([\w\.@\:/\-~]+)(\.git)(\/)?"
try:
    pass
except:
    pass

