#!/bin/bash
# sending request to url and getting response
curl -sL 0:5000/catch_me -X PUT "You got me!" -H "Origin: 0.0.0.0:5000/catch_me" -d "user_id=98"
