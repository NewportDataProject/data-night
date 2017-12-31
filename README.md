# data-night
**Welcome to Data Night!**  This is a community event where we explore our neighborhood through the lens of data. The goal is to find, clean up, analyze, and visualize data sets related to our community.  

## Contents

* [The Problem](#the-problem)
* [Tools](#tools)
* [Setup](#setup)

## The Problem

The focus of this Data Night is pedestrian safety - specifically crosswalks.  The City of Newport Bicycle and Pedestrian Advisory Commission (BPAC) has been asked to make recommendations on crosswalk improvements and additions.  We're helping out by combing through publically available data to get a good understanding on what the best options are for the city.  We're also building visualizations to bring out the stories behind the datasets.  

At this Data Night we are going to explore the data we already have and find new data that we need.  We want to end with nice clean, well-structured data files and interesting plots, graphs, and maps.

## Tools

Data night is all about exploring the data, so you should use whatever tools you are comfortable with (or want to get better at).
Here are a few technologies to help get you started:
* [Google](https://www.google.com) - Yes, Google (or [bing](https://www.bing.com)). Really, any search engine. There is a lot of data already out there to find, so search away!.
* [Fusion Tables](https://support.google.com/fusiontables#topic=1652595) - A free google tool for finding, building, sharing, and analyzing datasets.
* [Google Sheets](https://support.google.com/docs?docs_site_home#topic=2811806) - The free online spreadsheet you probably already know. Use it to build and share basic structured datasets.
* [Tableau](https://public.tableau.com/en-us/s/) - A data visualization software package that has a limited free tier.
* [Jupyter Notebooks](http://jupyter.org/index.html) with [Python](https://www.python.org/) - Jupyter is a browser-based development environment for python.  Run code and display data and graphics from your browser. There are some pre-built notebooks in this repo to kickstart your analysis.

### Python Packages
These are some python libraries that may come in handy at data night.  They're installed in the conda environment and on the Jupyter notebook server.
* [Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html) - The favorite data processing library. Read and write data files; sort, slice, and access data elements; analyze and visualize data. Pandas is also used as a base for a number of more specialized packages.
* [GeoPandas](http://geopandas.org/) - An extension of Pandas that works with geospatial data.
* [Requests](http://docs.python-requests.org/en/master/) - *"HTTP for Humans"* - A package for accessing data via the web, like apis.

## Data




## Setup

This repository has everything you need to get started. [Fork it](https://help.github.com/articles/fork-a-repo/) and clone it to your computer.  Alternatively, you can [download a zip file](https://github.com/NewportDataProject/data-night/archive/master.zip).  

We've set up a few different possible options for working with the data.  You can choose one or more that you're familiar with, or go your own way!

* [Docker](#docker)
* [Conda (Python)](#conda-python)

The base enviornment supported will be:
- Ubuntu 16.04 (Linux)
- Developers tools like `curl`, `vim`, and `git`
- Python 3
- Jupyter

> See something missing, please open an issue or PR and make a request!

### Docker
Docker is a tool for creating / deploying reproducible and consistent environments called "containers".  The idea behind creating a container is that the
environment / runtime can be scripted and thus rebuilt the same way easily over and over again.  

For the sake of Data Night, the intent is provide a unified and consistent development environment for anyone to use so as to provide all the tools that are considered most useful in one place.


#### Installation
1. Install [docker](https://www.docker.com).
1. In the command shell, navigate to this folder run the command `docker run`
1. Open a browser and go to `http://[CONTAINER_IP]:8888`

#### Usage
After you've built an image (see above steps), you can connect to it and use it like any other Linux CLI



### Conda (Python)
**Note: Currently this is only supported for Windows.**

1. If you don't have it already, install [Anaconda](https://www.anaconda.com) or [miniconda](https://conda.io/miniconda.html).
1. Set up the data-night conda environment with the command:

  ```shell
  conda env create -f environment.yml
  ```
3. Activate the environment using `activate data-night` (use `source` if you're using bash) and start jupyter with `jupyter notebook`.
4. Your browser should open to the jupyter server.  If not, open your browser and go to `http://localhost:8888`.
