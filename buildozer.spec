[app]
title = My Python App
package.name = mypythonapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 1.0.0
requirements = python3,kivy==2.1.0,android
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True

# Configuration Android
[android]
api = 33
minapi = 21
ndk = 25b
android.ndk_path = 
android.sdk_path = 
p4a.branch = develop
p4a.source_dir = 
android.arch = armeabi-v7a

# Permissions Android (ajuste selon tes besoins)
android.permissions = INTERNET
