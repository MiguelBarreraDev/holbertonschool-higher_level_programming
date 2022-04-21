#!/bin/bash
# Correction of "0. cURL body size"
curl -sI $1 | grep "Content-Length" | cut -d " " -f 2
