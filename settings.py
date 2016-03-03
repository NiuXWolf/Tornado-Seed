"""Project settings"""

import platform
import os

#root_dir = ''

if platform.node() == "FELINX":  # FELINX is the hosting server name.
    debug = False
else:
    debug = True

loglevel = "INFO"  # for celeryd
port = 8888


sitename = "DSE Status"
domain = "api.tr.me"
home_url = "http://%s/d3" % domain
login_url = "http://%s/login" % home_url
app_url_prefix = "/d3/v1"
email_from = "%s <noreply@%s>" % (sitename, domain)
admins = ("Felinx <felinx.lee@gmail.com>",)
send_error_email = True
cookie_secret = "d1d87395-8272-4749-b2f2-dcabd3903a1c"
xsrf_cookies = False


mysql = {"host": "localhost",
         "port": "3306",
         "database": "d3status",
         "user": "felinx",
         "password": "felinx"
         }

smtp = {"host": "localhost",
        "user": "",
        "password": "",
        "duration": 30,
        "tls": False
        }
