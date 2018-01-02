FROM jupyterhub/jupyterhub:latest

RUN pip install oauthenticator jupyter

RUN apt-get update && apt-get install -y gdal-bin imagemagick

RUN conda install -c conda-forge geopandas bokeh folium osmnx

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

VOLUME /srv/jupyterhub

VOLUME /home

EXPOSE 8000
