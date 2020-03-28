 #generates SSL certfication
 openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
 openssl req -x509 -out localhost.crt -keyout localhost.key \
  -newkey rsa:2048 -nodes -sha256 \
  -subj '/CN=localhost' -extensions EXT -config <( \
   printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")
 # build docker image if any changes are done 
 sudo docker build -t docker-chatcotcovid-api:latest .
 #Launch the application
 sudo docker run -it -p 5000:5000 -v $(pwd):/app  docker-chatcotcovid-api:latest
 #Get container ID and Launch the application
 sudo docker ps
 sudo docker exec -t -i 96f3247ab9cb /bin/bash