# *Know Your Heart*
# ECE 651 Software Engineering Project

<a id="org6690aa0"></a>

## Overview

-   This project is a web application which uses machine learning to analyze the UCI heart disease dataset and make predictions based on supplied medical data.
-   The website should display the risk factors to the user as well as a probability or confidence score of their health in the coming years. If possible, the lifestyle choices to be made should also be displayed.

# Link for the Website
* IP Address: http://35.196.37.255/
* URL: https://bit.ly/34in0Rq 

# Link for the Gitlab Project Repository
* https://git.uwaterloo.ca/cardiovascular-project-ece651/cardiovascular-predictions

<a id="orgdcf927c"></a>

## Structure

The project (so far) is arranged as follows
.<br/>
+-- app<br/>
| 	+-- app.py<br/>
|	+-- requirements.txt<br/>
|	+-- static<br/>
|	|	+-- 'static content for site'<br/>
|	+-- templates<br/>
|	|	+-- 'html templates for site'<br/>
+-- analysis<br/>
| 	+-- data<br/>
|	|	+-- 'the data files'<br/>
|	+-- documentation<br/>
|	|	+-- 'information on the dataset'<br/>
|	+-- raw_data<br/>
|	|	+-- 'the raw UCI heart disease dataset'<br/>
|	+-- utils<br/>
|	|	+-- 'python scripts for data preparation'<br/>
+-- docker<br/>
|	+-- analysis<br/>
|	+-- app/<br/>
|	|	+-- Dockerfile<br/>
|	+-- database/<br/>
+-  docker-compose.yaml<br/>
+-- kubernetes.yaml<br/>
+-- README.md<br/>


<a id="org9556092"></a>

## How to use

1.  Navigate to the project root
2.  At the command prompt enter \`sudo docker-compose build && sudo docker-compose up\`
3.  Using a web browser, navigate to localhost (default port 80)
