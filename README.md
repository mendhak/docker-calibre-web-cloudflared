This is my setup for a public facing [Calibre Web](https://github.com/janeczku/calibre-web) server, exposed through a [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/) hosted on a Raspberry Pi.  
It's all contained within docker compose, so everything needed to run it is in one place. 

## About

In this example the domain is `mylibrary.example.com` which is a Cloudflare tunnel pointing at the nginx container which proxies to the calibre-web container.  

The nginx container sets the robots.txt and noindex tags.  It also sets proxy headers to tell the calibre-web server to use https URLs, necessary for OAuth logins. 

The calibre-web container points at a `Books/` directory locally, so you'll need to sync your Calibre library to it via another mechanism.  I use Google Drive so a sample rclone script `syncbooks.sh.example` is included.


## Setup

Login to Cloudflare first

    docker run -v $PWD/cloudflared:/.cloudflared erisamoe/cloudflared login

This creates a `cloudflared` directory locally with a .pem in it, that's the login credentials needed to manage the tunnel.

Edit the `docker-compose.yml` file to point it at a domain that you manage on Cloudflare, instead of `mylibrary.example.com`.  

Then, start the containers. 

    docker-compose up -d 

Watch the logs as the initial start takes a few minutes

    docker-compose logs -f

When it's stopped updating, you can browse to https://mylibrary.example.com 


## Troubleshooting 

If this is a new setup reusing an existing tunnel, you'll need to clear it out first.  List and delete any tunnels named mylibrary, if they exist.

    docker run -v $PWD/cloudflared:/etc/cloudflared erisamoe/cloudflared tunnel list
    docker run -v $PWD/cloudflared:/etc/cloudflared erisamoe/cloudflared tunnel delete mylibrary

Then follow the setup instructions
