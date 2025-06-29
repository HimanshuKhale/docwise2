[app]
title = Docwise App
package.name = docwiseapp
package.domain = org.codex

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
include_patterns = assets/*

version = 0.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,plyer,certifi,idna,chardet,urllib3

orientation = portrait

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = armeabi-v7a

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
