FROM jupyterhub/jupyterhub:latest

RUN pip install oauthenticator jupyter

RUN conda install -c conda-forge geopandas bokeh folium osmnx

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

VOLUME /srv/jupyterhub

VOLUME /home

EXPOSE 8000
