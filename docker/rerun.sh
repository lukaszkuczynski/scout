ARGS=$1
docker run --rm -p 5000:5000 -it $ARGS --name scout luk/rpi-scout
