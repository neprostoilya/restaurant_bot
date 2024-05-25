#  Restouran Bot

Restoran Bot is a comprehensive dining app designed to enhance your restaurant experience. 
It offers seamless food ordering, table reservations, and pick-up options, all within a user-friendly interface. 
With Restoran Bot, enjoy real-time menu browsing, quick reservations, and hassle-free orders, making your dining experience smoother than ever.


Link bot in telegram: https://t.me/Cafe_7a_bot

#  Setup And Start 

1. Download Docker and Docker Compose

```
    sudo apt-get update
    sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install docker-ce
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    sudo systemctl start docker
```


2. Create main folder and clone reposetory

```
    mkdir /var/www/ 
    mkdir /var/www/restourant_bot/
    cd /var/www/restourant_bot/
    git clone https://github.com/neprostoilya/reustoran_bot.git
    cd restourant_bot/
```

3. Setup in .env file


```
    SECRET_KEY=django_secret_key
    
    DEBUG=1 or 0 
    
    TOKEN_BOT_1=token_for_restouran_bot
    
    TOKEN_BOT_2=token_for_manager_bot
    
    NAME=db_postgres
    USER=postgres
    PASSWORD=password_postgres
    HOST=db
    PORT=5432
    
    CLICK=your_ssh_code_for_click
    
    POSTGRES_DB=db_postgres
    POSTGRES_USER=user_postgres
    POSTGRES_PASSWORD=
    
    PAYME=your_ssh_code_for_payme
```

   
4. Setup In nginx/default.conf:

```
    server {
        listen 80;
        server_name your_domain;
    
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
    
```

5. Start docker compose

```
    docker compose up -d db api nginx
    docker compose up -d certbot
```

6. Before 'Succesful Let's Encrypt', you have to change config In nginx/default.conf: 

```
    server {
        listen 443 ssl;
        server_name your_domain;

        ssl_certificate     /etc/letsencrypt/live/your_domain/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/your_domain/privkey.pem;
        ssl_trusted_certificate /etc/letsencrypt/live/your_domain/chain.pem;

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
```

7. Before 'Succesful Let's Encrypt', you have to change config In nginx/default.conf: 

```
    docker compose up -d nginx
    docker compose up -d bot
```

..end 
