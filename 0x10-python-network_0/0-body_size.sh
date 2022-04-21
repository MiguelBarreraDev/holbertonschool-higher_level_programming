#!/usr/bin/env bash
#!/usr/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
curl -I -s $1 | grep "Content-Length" | cut -d " " -f 2
