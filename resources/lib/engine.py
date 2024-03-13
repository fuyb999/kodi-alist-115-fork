#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import xbmc
import xbmcgui
import json
import threading

from resources.lib.utils import log

from resources.lib.interface import notify

class Player(xbmc.Player):
    def __init__(self, api):
        xbmc.Player.__init__(self)
        self._api = api
        self._player = xbmc.Player()
        self._playback_lock = threading.Event()

    def onPlayBackStarted(self):
        if self._api.isLoggedIn:
            play_url = self._player.getPlayingFile()
            notify(play_url)
            self._api.play(play_url)

    def onPlayBackStopped(self):
        log("Stop clear")

    def onPlayBackEnded(self):
        log("End clear")
