FROM jupyterhub/jupyterhub:latest

RUN pip install oauthenticator jupyter

RUN apt-get update && apt-get install -y gcc libspatialindex-dev libjpeg-dev gdal-bin imagemagick

RUN pip install geopandas bokeh folium osmnx fiona rtree

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

VOLUME /srv/jupyterhub

VOLUME /home

EXPOSE 8000
