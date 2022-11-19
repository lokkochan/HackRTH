# HackRTH
Hackathon 11/2022 UofC
## Table of Contents
<!-- toc -->
- [Introduction](#introduction)
- [Build Instructions](#build-instructions)
  - [Requirements](#requirements)
  - [Build](#build)
- [Contact](#contact)
- [License](#license)
<!-- tocstop -->

## Introduction
Health ......

## Build Instructions
### Requirements
`python>=3.9`
```shell
pip install -r requirements.txt
```
### Build
```shell
cd hackrth
```
To build the apk, execute
```shell
export DYLD_LIBRARY_PATH="/usr/local/lib/"  # for mac/Linux
briefcase build android -u
```
The built apk will be at `hackrth/android/gradle/HackRTH/app/build/outputs/apk/debug/app-debug.apk`
To run locally, 
```shell
briefcase dev
```
## Contact

## License
