#!/usr/bin/env bash
curl -I -s $1 | grep "Content-Length" | cut -d " " -f 2
