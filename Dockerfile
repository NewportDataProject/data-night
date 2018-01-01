FROM continuumio/anaconda3:5.0.1
RUN conda create -n datanight python=3.6
RUN bash -c "source activate datanight  && conda install -c conda-forge geopandas bokeh folium osmnx"