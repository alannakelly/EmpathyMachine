# Empathy Machine

## Description

A Python program that attempts to simulate the illusion of a counselling robot from a dystopian future.

## Platform

The code is currently compatible with RasPi 2.0

## Requirements

 * OpenCV 3+ for Python.
 * OMXPlayer Python bindings for hardware acellerated mp4 decoding.
 * ALSA Audio for Python

## How it works

The system is modelled as a Finte State Machine, based on the examples given in the book "Programming Gmae AI by Example" by Matt Buckland. There is a basic face recognition system build in OpenCV that takes input from a RasPi camera and recognizes faces.  There is a sound recognizer to recognize "voices". The face recognition system runs in a separate thread. The system launches an instance of OMXPlayer to play the video loop.



