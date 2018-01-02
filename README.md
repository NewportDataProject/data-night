# data-night
**Welcome to Data Night!**  This is a community event where we explore our neighborhood through the lens of data. The goal is to find, clean up, analyze, and visualize data sets related to our community.  

## Contents

* [The Problem](#the-problem)
* [Setup](#setup)
* [Data](#data)

## The Problem

The focus of this Data Night is pedestrian safety - specifically crosswalks.  The City of Newport Bicycle and Pedestrian Advisory Commission (BPAC) has been asked to make recommendations on crosswalk improvements and additions.  We're helping out by combing through publically available data to get a good understanding on what the best options are for the city.  We're also building visualizations to bring out the stories behind the datasets.  

At this Data Night we are going to explore the data we already have and find new data that we need.  We want to end with nice clean, well-structured data files and interesting plots, graphs, and maps. [This notebook](http://www.newportdataproject.org/data-night/intro-to-data.html) walks through the general process of what we are trying to accomplish.

## Setup

This repository has pretty much everything you need to get started. [Fork it](https://help.github.com/articles/fork-a-repo/) and clone it to your computer.  Alternatively, you can [download a zip file](https://github.com/NewportDataProject/data-night/archive/master.zip). 

**There are a few ways to contribute at Data Night:**  

- If you're more comfortable with researching on the web and using google tools, check out the [data mining team](http://www.newportdataproject.org/data-night/data-mining.html).  
- If you know or want to practice python, keep reading below for a few options.  
- If you've already got your own data science workflow, grab some [datasets](#data) and have fun.

### Python in Jupyter

[Jupyter](http://jupyter.org/index.html) is a browser-based development environment for [Python](https://www.python.org/).  Run code and display data and graphics from your browser. There are some pre-built notebooks in the `/workspace` directory to kick-start your analysis.

#### Jupyter Hub

If you just want to skip the setup and start coding, we have a jupyter hub running for Data Night at [http://jupyter.newportdatproject.org](http://jupyter.newportdataproject.org).

1. Log in with your github credentials ([sign up here](https://github.com/join) if you don't have them)
2. Upload one of the example `*.ipynb` notebooks from the `/workspace` directory or start a fresh one
3. When you're done, make sure you download your notebooks, because the server will be shutdown after the event

#### Docker

[Docker](https://www.docker.com) is a tool for creating / deploying reproducible and consistent environments called "containers".  The idea behind creating a container is that the environment / runtime can be scripted and thus rebuilt the same way easily over and over again.  

For the sake of Data Night, the intent of using Docker is provide a unified and consistent environment for anyone to get all the tools that are considered most useful in one place with minimal overhead installing them all manually.

##### Starting the Container

1. [Install Docker](https://www.docker.com/community-edition).
2. In the command shell, navigate to the root of this repository
3. Run `docker-compose up -d`  (First time running this may a take a little time)
4. Navigate to [`localhost:8889`](http://localhost:8889) in your browser

#### Anaconda (Python)

Anaconda is a distribution of python focused on data science.  It provides a very good package manager `conda` and manages isolated virtual environments so you can run multiple versions of python on your machine for different projects. These instructions will get you up and running with the base packages needed for the examples.

1. If you don't have it already, install [Anaconda](https://www.anaconda.com) or [miniconda](https://conda.io/miniconda.html).

2. Set up the data-night conda environment with the command:

   ```shell
   $ conda create -n data-night python=3.6
   $ activate data-night  # if you're using bash, use source activate here
   $ conda install -c conda-forge geopandas bokeh folium osmnx geopy
   ```

3. Open your console in this directory, activate the environment using `activate data-night` (use `source` if you're using bash) and start jupyter with `jupyter notebook`.

4. Your browser should open to the jupyter server.  If not, copy and paste the link (with the token) from your console.  (it should be something like `127.0.0.1:8888/?token=####)

### Python Packages
These are some python libraries that may come in handy at Data Night.  They're installed in the docker image and on the Jupyter notebook server.
* [Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html) - The favorite data processing library. Read and write data files; sort, slice, and access data elements; analyze and visualize data. Pandas is also used as a base for a number of more specialized packages.
* [GeoPandas](http://geopandas.org/) - An extension of Pandas that works with geospatial data.
* [osmnx](http://geoffboeing.com/2016/11/osmnx-python-street-networks/) - A tool for analyzing and visualizing street networks, pulling from [OpenStreetMap](https://www.openstreetmap.org) data and using standard python network analysis libararies.
* [Folium](https://folium.readthedocs.io/en/latest/) and [Bokeh](https://bokeh.pydata.org/en/latest/) - Two visualization libraries that work well in juyter notebooks. Folium is an interface to build interactive maps, and Bokeh builds interactive charts, including maps.

## Data

There are public datasets available all over the internet.  Here are a couple places to start looking:

* The [Sidewalk Map](https://github.com/newportdataportal/sidewalk-map)
* [Results from the 2014 BPAC Survey on Pedestrian Safety](https://github.com/NewportDataPortal/newport-crosswalk-survey-2014)
* [This list of public datasets](https://github.com/newportdataproject/data/wiki/Data-Portals) compiled by Newport Data Project
* The Newport Data Project [data portal](http://portal.newportdataproject.org) - a collection of datasets in github repositories, so they can be downloaded or accessed via an api