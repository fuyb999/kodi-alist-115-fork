#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
NOT LICENSED YET
Creator: David Davó <david@ddavo.me>
'''

import sys
import xbmc
import xbmcvfs

from resources.lib.utils import log
from resources.lib.utils import system_lock
from resources.lib.interface import notify
from resources.lib import engine
# from resources.lib import api_simkl
from resources.lib import api_alist
from resources.lib import events

if __name__ == "__main__":
    system_lock("Alist115ForkRun", 5)
    log("dir = " + str(xbmcvfs.translatePath("special://home")))
    log("Python Version = " + str(sys.version))
    log("args = " + str(sys.argv))

    notify("welcome")

    # api = api_simkl.Simkl()
    api = api_alist.Alist()
    monitor = events.Monitor(api=api)
    player = engine.Player(api=api)

    while not monitor.abortRequested():
        if monitor.waitForAbort(90):
            break

sys.exit(0)
