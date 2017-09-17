#!/bin/bash

ispncon="clients/ispncon/bin/ispncon"

KEY=$(shuf -i 1-50000 -n 1)
VALUE=$(shuf -i 1-50000 -n 1)

retorno=$($ispncon -c hotrod -h 127.1 -p 11222 -C default put $KEY $VALUE)
# retorno=$($ispncon -c hotrod -h 192.168.0.1 -p 11222 -C default put $KEY $VALUE)

if [ "$retorno" != 'STORED' ]; then
    echo "error"
    exit 1
else
    sed -i "/Key/c\    <p>Key: $KEY </p>" model-ok.html
    sed -i "/Value/c\    <p>Value: $VALUE </p>" model-ok.html
fi
