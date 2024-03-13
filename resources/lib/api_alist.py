#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

import http.client

from resources.lib.interface import notify
from resources.lib.utils import get_str
from resources.lib.utils import get_setting
from resources.lib.utils import set_setting


class Alist:
    def __init__(self):
        self.userSettings = {
            "user": {
                "name": "unknown"
            }
        }
        self.isLoggedIn = False
        self.loginInProgress = False

        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
        # set_setting('token', '')
        token = get_setting('token')
        if token:
            self.headers["authorization"] = token
            return
        self.login()

    def login(self):
        if self.loginInProgress:
            return
        self.loginInProgress = True

        if not self.isLoggedIn:
            data = {
                "username": get_setting("username"),
                "password": get_setting("password")
            }
            rdic = self._http("/auth", headers=self.headers, body=data)

            if isinstance(rdic, dict) and rdic["code"] == 200:
                token = rdic["data"]
                self.headers["authorization"] = token
                set_setting('token', token)
                if len(token) == 0:
                    notify("Alist login successfully.")
                else:
                    notify("Alist login fail.")
        else:
            self.loginInProgress = False

    def play(self, url):
        data = {
            "path": url
        }
        rdic = self._http("/play", headers=self.headers, body=data)
        if isinstance(rdic, dict) and rdic["code"] == 200:
            notify(rdic["data"])
        else:
            notify(rdic["message"])

    def _http(self, url, headers={}, body={}, is_json=True, method='POST'):
        try:
            con = http.client.HTTPConnection(get_setting("address"), 5243)
            form_data = None
            if len(body) > 0:
                form_data = '&'.join([f'{key}={value}' for key, value in body.items()])
            con.request(method, url, headers=headers, body=form_data)
            r = con.getresponse()
            data = json.loads(r.read().decode("utf-8"))
            if r.status == 401 or data["code"] == 401:
                self.isLoggedIn = False
                set_setting('token', '')
                notify(get_str(32031))
                return False
            return data if is_json else r
        except Exception as e:
            notify("http err: " + str(e))
            return None

