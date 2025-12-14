[app]
title = MonApk
package.name = monapk
package.domain = org.termux
source.include_exts = py,kv
requirements = python3,kivy
entrypoint = main.py
android.permissions = INTERNET
version = 0.1

[buildozer]
log_level = 2
