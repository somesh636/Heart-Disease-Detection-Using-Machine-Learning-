# *Know Your Heart*
# ECE 651 Software Engineering Project


<a id="org6690aa0"></a>

## Overview

-   This project is a web application which uses machine learning to analyze the UCI heart disease dataset and make predictions based on supplied medical data.
-   The website should display the risk factors to the user as well as a probability or confidence score of their health in the coming years. If possible, the lifestyle choices to be made should also be displayed.


<a id="orgdcf927c"></a>

## Structure

The project (so far) is arranged as follows
.|.
.|app|
..|app.py|
..|requirements<sub>flask.txt</sub>|
..|static|
...|<static content for site>|
..|templates|
...|<html templates for site>|
.|analysis|
..|data|
..|documentation|
...|<information on the dataset>|
..|raw<sub>data</sub>|
...|<the raw UCI heart disease dataset>|
..|utils|
...|<python scripts for data preparation>|
.|docker|
..|analysis|
..|app|
...|Dockerfile|
..|database|
.|kubernetes.yaml|
.|README.md|

.
+-- app
| 	+-- app.py
|	+-- requirements<sub>flask.txt</sub>
|	+-- static
|	|	+-- 'static content for site'
|	+-- templates
|	|	+-- 'html templates for site'
+-- analysis
| 	+-- data
|	|	+-- 'the data files'
|	+-- documentation
|	|	+-- 'information on the dataset'
|	+-- raw<sub>data</sub>
|	|	+-- 'the raw UCI heart disease dataset'
|	+-- utils
|	|	+-- 'python scripts for data preparation'
+-- docker
|	+-- analysis
|	+-- app
|	|	+-- Dockerfile
|	+-- database
+-- kubernetes.yaml
+-- README.md


<a id="org9556092"></a>

## How to use

1.  Navigate to the project root
2.  At the command prompt enter \`flask run\`
3.  Using a web browser, navigate to localhost:5000 (or 127.0.0.1:5000)

To run the Website make the backend you Working Directory and execute the following command 
$ flask run
ctrl+click on the http://127.0.0.1:5000/ to run and Press CTRL+C to quit 
