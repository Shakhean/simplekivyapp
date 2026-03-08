[app]

# (str) Title of your application
title = Counter App

# (str) Package name
package.name = counterapp

# (str) Package domain (reverse domain style)
package.domain = org.test

# (str) Source code folder
source.dir = .

# (list) Source files to include (important for GitHub Actions)
source.include_exts = py,png,jpg,kv,atlas,ttf,txt

# (str) Main Python file
source.main = main.py

# (str) Version number
version = 0.1

# (list) Application requirements - ADDED crucial dependencies
requirements = python3,kivy==2.1.0,setuptools,hostpython3,openssl,requests

# (str) Orientation
orientation = portrait

# (int) Fullscreen mode (0 = no, 1 = yes)
fullscreen = 0

# (str) Icon of the app (optional)
icon.filename = %(source.dir)s/icon.png

# (list) Permissions your app needs (optional)
android.permissions = INTERNET

# --- Android-specific options ---
# (int) Android API level to use
android.api = 31

# (int) Minimum API level
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 24

# (str) Android NDK version to use
android.ndk = 23b

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) Android package name (modify to be unique)
android.package_name = org.test.counterapp

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) If True, then don't try to copy Python to the device
android.copy_python = True

# (bool) If True, then ignore the Java version error
android.ignore_java_version = True

# (str) Android entry point (default is 'org.kivy.android.PythonActivity')
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme (default is '@android:style/Theme.NoTitleBar')
android.apptheme = "@android:style/Theme.Material.Light"

# (list) Java files to add to the build (optional)
# android.add_src =

# (str) Extra Java dependencies (optional)
# android.gradle_dependencies =

# (bool) Add gradle dependencies reported by builds
android.gradle_repositories = []

# --- Buildozer settings ---
# (int) Log level (0-2)
log_level = 2

# (str) Directory for builds
build_dir = ./.buildozer

# (str) Directory for binaries
bin_dir = ./bin

# (str) Architecture to build (when not building for all)
android.arch = armeabi-v7a