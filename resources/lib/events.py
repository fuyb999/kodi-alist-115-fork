import xbmc
import json

from resources.lib.utils import log


class Monitor(xbmc.Monitor):
    def __init__(self, api, *args, **kwargs):
        xbmc.Monitor.__init__(self)

        self._api = api

    def onNotification(self, sender, method, data):
        log('onNotification')
        log('sender {0}'.format(bool(sender == 'plugin.video.115fork')))

        if (method == 'VideoLibrary.OnUpdate'):
            pass

        if sender == "plugin.video.115fork":
            if method == 'Other.login':
                self._api.login()

    def onSettingsChanged(self):
        log("CHANGED")
