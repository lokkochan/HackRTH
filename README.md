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
Let the users do some exercise tasks, so that can gain some points, which can redeem in some shops
Go to [This website](http://101.132.227.6:3554) (My server) to see the demo for shops. 

## Build Instructions
### Requirements
`python>=3.9`
```shell
pip install -r requirements.txt
```
To install the android environment, it's necessory to create an app and you can be deleted afterwards: 
```shell
briefcase new
briefcase create android
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
The 3 contributors
## License
