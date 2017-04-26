docker rm -f scout
docker run -p 5000:5000 -it --name scout luk/rpiscout
