
1. 
    sudo apt-get update
    sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install docker-ce
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    sudo systemctl start docker
2. 
    mkdir /var/www/ 
    mkdir /var/www/restourant_bot/
    cd /var/www/restourant_bot/
    git clone https://github.com/neprostoilya/reustoran_bot.git
    cd restourant_bot/
3. 
    nano .env

    docker compose up -d db api nginx 

    In nginx/default.conf:

        server {
            listen 80;
            server_name kafe-7a-test.tw1.su;

            location / {
                proxy_pass http://api:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }

            location /static/ {
                alias /app/api/static/;
            }

            location ~ /.well-known/acme-challenge/ {
                root /var/www/certbot;
            }
        }
    

    docker compose up -d certbot


    After nginx/default.conf:

        server {
            listen 443 ssl;
            server_name kafe-7a-test.tw1.su;

            ssl_certificate     /etc/letsencrypt/live/kafe-7a-test.tw1.su/fullchain.pem;
            ssl_certificate_key /etc/letsencrypt/live/kafe-7a-test.tw1.su/privkey.pem;
            ssl_trusted_certificate /etc/letsencrypt/live/kafe-7a-test.tw1.su/chain.pem;

            location / {
                proxy_pass http://api:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }

            location /static/ {
                alias /app/api/static/;
            }

            location ~ /.well-known/acme-challenge/ {
                root /var/www/certbot;
            }
        }


    docker compose up -d nginx

