name: Build Kivy App

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  build-android:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'

    - name: Install system dependencies
      run: |
        sudo apt update
        sudo apt install -y \
          git \
          zip \
          unzip \
          openjdk-17-jdk \
          autoconf \
          libtool \
          pkg-config \
          zlib1g-dev \
          libncurses5-dev \
          libncursesw5-dev \
          libtinfo5 \
          cmake \
          libffi-dev \
          libssl-dev \
          libltdl-dev

    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        pip install buildozer cython virtualenv

    - name: Cache buildozer directory
      uses: actions/cache@v3
      with:
        path: ~/.buildozer
        key: ${{ runner.os }}-buildozer-${{ hashFiles('buildozer.spec') }}
        restore-keys: |
          ${{ runner.os }}-buildozer-

    - name: Build with buildozer
      run: |
        buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: counter-app-apk
        path: bin/*.apk