#!/bin/sh -x

awk -F: '{cmd="echo " $1;  system(cmd)}' test
