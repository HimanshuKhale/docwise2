[app]
title = Docwise App
package.name = docwiseapp
package.domain = org.codex

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
include_patterns = assets/*

version = 0.1

# Only include packages you've already preinstalled from wheels.
requirements = python3,kivy,kivymd,requests,plyer,certifi,idna,chardet,urllib3,pyjnius,kivy_garden,docutils,pygments

orientation = portrait

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = armeabi-v7a

# Local custom recipes
p4a.local_recipes = ./recipes
extra_pip_args = --no-index --find-links=./wheels

# Optional prebuilt wheels (used to avoid PyPI entirely)
p4a.whl_dir = ./wheels

android.allow_backup = 1
android.logcat_filters = *:S python:D
android.enable_androidx = 1

# Avoid runtime crashes from missing multidex support
android.gradle_dependencies = com.android.support:multidex:1.0.3

[buildozer]
log_level = 2
warn_on_root = 1
