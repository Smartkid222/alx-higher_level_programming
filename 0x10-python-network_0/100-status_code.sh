#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response. no pipe
curl -s "$1" -o /dev/null -w '%{http_code}'
