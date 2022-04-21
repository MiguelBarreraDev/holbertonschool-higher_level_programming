#!/bin/bash
# 3. cURL only methods
curl -sI $1 | grep "Allow" | cut -d " " -f 2-
