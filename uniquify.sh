#!/bin/bash

cut -d '	' -f 1 $1 | sort | uniq | sort
