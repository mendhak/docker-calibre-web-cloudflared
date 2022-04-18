This is my basic setup for a public facing Calibre Web server, exposed through a Cloudflare Tunnel.  
It's all contained within docker compose, so everything needed to run it is in one place. 

In this example the domain is `mylibrary.example.com` which tunnels to the nginx container which proxies to the calibre web container.  

The nginx container sets the robots.txt and noindex tags.  It also sets proxy headers to tell the calibre-web server to use https URLs, necessary for OAuth logins. 

The calibre-web container points at a `Books/` directory locally, so you'll need to sync your books to it via another mechanism.  I use Google Drive so a sample rclone script `syncbooks.sh.example` is included.


## Pre-setup

Login to Cloudflare first

    docker run -v $PWD/cloudflared:/.cloudflared erisamoe/cloudflared login

This creates a `cloudflared` directory locally with a .pem in it, that's the login credentials needed to manage the tunnel.

List and delete any tunnels named mylibrary, if they exist. 

    docker run -v $PWD/cloudflared:/etc/cloudflared erisamoe/cloudflared tunnel list
    docker run -v $PWD/cloudflared:/etc/cloudflared erisamoe/cloudflared tunnel delete mylibrary


## Setup

That's it, start the containers. 

    docker-compose up -d 

Watch the logs as the initial start takes a few minutes

    docker-compose logs -f

When it's stopped updating, you can browse to https://mylibrary.example.com 
