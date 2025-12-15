[app]
title = MonApk
package.name = monapk
package.domain = org.termux
source.include_exts = py,kv
requirements = python3,kivy
entrypoint = main.py
orientation = portrait
fullscreen = 0
version = 0.1
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.api = 33
android.ndk = 25b
android.sdk = 33
android.minapi = 21
