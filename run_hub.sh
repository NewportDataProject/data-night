#!/bin/bash
docker build --tag ndp_hub jupyterhub
docker run --volume=jupyterhub_config:/srv/jupyterhub --volume=jupyterhub_home:/home -p 8000:8000 ndp_hub
