# data-night
**Welcome to Data Night!**  This is a community event where we explore our neighborhood through the lens of data. The goal is to find, clean up, analyze, and visualize data sets related to our community.  

## Contents

* [The Problem](#the-problem)
* [Setup](#setup)


* [Tools](#tools)

## The Problem

The focus of this Data Night is pedestrian safety - specifically crosswalks.  The City of Newport Bicycle and Pedestrian Advisory Commission (BPAC) has been asked to make recommendations on crosswalk improvements and additions.  We're helping out by combing through publically available data to get a good understanding on what the best options are for the city.  We're also building visualizations to bring out the stories behind the datasets.  

At this Data Night we are going to explore the data we already have, and find new data that we need.  We want to end with nice clean, well-structured data files, and interesting plots, graphs, and maps.

## Setup

This repository has everything you need to get started. [Fork it](https://help.github.com/articles/fork-a-repo/) and clone it to your computer.  Alternatively, you can [download a zip file](https://github.com/NewportDataProject/data-night/archive/master.zip).  

We've set up a few different possible options for working with the data.  You can choose one or more that you're familiar with, or go your own way!

* [Docker](#docker)
* [Conda (Python)](#conda-python)

### Docker

* Install [docker](https://www.docker.com).
* In the command shell, navigate to this folder run the command `docker run`
* Open a browser and go to `http://[CONTAINER_IP]:8888`

### Conda (Python)

* If you don't have it already, install [Anaconda](https://www.anaconda.com) or [miniconda](https://conda.io/miniconda.html).

* Set up the data-night conda environment with the command:

  ```shell
  conda env create -f environment.yml
  ```

* Activate the environment using `activate data-night` (use `source` if you're using bash) and start jupyter with `jupyter notebook`.

* Your browser should open to the jupyter server.  If not, open your browser and go to `http://localhost:8888`.

## Tools



## Data



