[app]
title = Docwise App
package.name = docwiseapp
package.domain = org.codex

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
include_patterns = assets/*

version = 0.1
requirements = python3,kivy,materialyoucolor,exceptiongroup,asyncgui,asynckivy,requests,plyer,certifi,idna,chardet,urllib3,https://github.com/kivymd/KivyMD/archive/master.zip

#presplash.filename = %(source.dir)s/Splash.png
#icon.filename = %(source.dir)s/Icon.png

orientation = portrait

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
osx.kivy_version = 2.3.0
android.accept_sdk_license = True
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a

# Let Buildozer auto-manage SDK/NDK/platform tools
android.sdk = 
android.ndk_path = 

# Enable AndroidX to avoid support lib errors
android.enable_androidx = 1
android.allow_backup = 1
android.logcat_filters = *:S python:D

# Prevent crashes due to missing dependencies
android.gradle_dependencies = com.android.support:multidex:1.0.3

[buildozer]
log_level = 2
warn_on_root = 1
