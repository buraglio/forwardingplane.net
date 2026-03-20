---
title: Linkwarden with docker compose and nginx proxy manager
date: 2026-03-12
author: Nick Buraglio
layout: post
categories:
    - configuration
    - linux
    - docker
tags:
    - networking
    - docker
    - linux
---


[Linkwarden(https://github.com/linkwarden/linkwarden) is a tool for better managing bookmarks. If you're nything like me, you keep 1000 browser tabs open across a series of profiles, with full intention of revisiting them later, and then never do. A colleague shpoed me linkwarden and I was interested straight away. I did have a few hangups, however: 

- I don't want to rely on a cloud service if I don't have to
- I prefer to control my own content
- I am not a big fan of docker, which is required for self hosting

I got over the docker hangup since it wasn't really an option to do any other way and got straight to it. Very quickly I ran into the near-universal issues I have with docker:

- poor understanding or lack of attention of networking by the developers (this needs to run over IPv6 for me to use it)
- spotty documentation for running this securely via a SSL enabled web service

As I have done with other services that require docker, I went to nginx proxy manager. This container is a nice front end for proxying services via SSL / NGINX, and is far easier to wrestle than something like Traefik. 

After much fighting of the docker compose file I ended up with this, which works. 

```
services:
  postgres:
    image: postgres:16-alpine
    env_file: .env
    restart: always
    volumes:
      - ./pgdata:/var/lib/postgresql/data
    networks:
      - linkwarden-network
  linkwarden:
    env_file: .env
    environment:
      - DATABASE_URL=postgresql://postgres:${POSTGRES_PASSWORD}@postgres:5432/postgres
    restart: always
    # build: . # uncomment to build from source
    image: ghcr.io/linkwarden/linkwarden:latest # comment to build from source
    ports:
      - 3000:3000
    volumes:
      - ./data:/data/data
    depends_on:
      - postgres
      - meilisearch
    networks:
      - linkwarden-network
  meilisearch:
    image: getmeili/meilisearch:v1.12.8
    restart: always
    env_file:
      - .env
    networks:
      - linkwarden-network
    volumes:
      - ./meili_data:/meili_data
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: npm
    ports:
      - "81:81"    # Admin interface
      - "80:80"    # HTTP
      - "443:443"  # HTTPS
    volumes:
      - ./npm/data:/data
      - ./npm/letsencrypt:/etc/letsencrypt
    networks:
      - linkwarden-network
networks:
  linkwarden-network:
    driver: bridge
    enable_ipv6: true
```

This configuration will work with NPM front ending the https pieces, and will also work behind cloudflare. You'll need to find the address of the container to put into the NPM proxy manager. This can be found with the following command:

`sudo docker inspect <container ID> | grep IP`

The output should look similar to 

```
buraglio@dockhost1:/opt/linkwarden$ sudo docker inspect af8e7a6c4edd | grep IP
                "RSS_SUBSCRIPTION_LIMIT_PER_USER=",
                "PIPEDRIVE_CUSTOM_NAME=",
                "NEXT_PUBLIC_PIPEDRIVE_ENABLED=",
                "PIPEDRIVE_CLIENT_ID=",
                "PIPEDRIVE_CLIENT_SECRET=",
                    "IPAMConfig": null,
                    "IPAddress": "172.19.0.4",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "fd64:b2a0:6eac:1::1",
                    "GlobalIPv6Address": "fd64:b2a0:6eac:1::4",
                    "GlobalIPv6PrefixLen": 64,
```

for anyone who would rather not deal with this amount of complexity, linkwarden has a [very reasonable hosted option](https://linkwarden.app/).
