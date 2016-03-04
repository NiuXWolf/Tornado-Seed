"""Project settings"""

import platform
import os

#root_dir = ''

if platform.node() == "TR":  # FELINX is the hosting server name.
    debug = False
else:
    debug = True

loglevel = "INFO"  # for celeryd
port = 8888


sitename = "DSE Status"
domain = "trdse.com"
home_url = "http://%s/d3" % domain
#login_url = "http://%s/login" % home_url
app_url_prefix = "/dse/v1"
email_from = "%s <noreply@%s>" % (sitename, domain)
admins = ("Y.Yu@thomsonreuters.com",)
send_error_email = True
cookie_secret = "d2d87395-8272-4749-b2f2-dcabd3903a1d"
xsrf_cookies = False


mysql = {"host": "localhost",
         "port": "3306",
         "database": "d3status",
         "user": "felinx",
         "password": "felinx"
         }

smtp = {"host": "smtp.qq.com",
        "port":"25",
        "user": "786381191@qq.com",
        "password": "xxx",
        "duration": 30,
        "tls": False
        }
