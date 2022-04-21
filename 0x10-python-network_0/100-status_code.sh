#!/bin/bash
# Displays only the status code of the response
curl -s $1 -w "%{http_code}" -o /dev/null
