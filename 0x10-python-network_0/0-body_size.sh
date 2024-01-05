#!/bin/bash
#takes in a URL, sends a request to that URL isplays the size of the body of re
curl -s "$1" | wc -c
