# Ticket Intent Extractor
### [Final output for Accenture Technology's Project X program]

---
## Authors
#### Marielle Louise Cruz
* https://github.com/marielleloui
* https://linkedin.com/in/marielle-louise-cruz

#### Zhong Xien Yeoh
* https://linkedin.com/in/zhong-xien-yeoh-137141173

## About the Project
This application was developed as a way to extract information from support tickets,
categorise ticket data into clusters with the use of Machine Learning models, create sorted CSV outputs,
and visualise data in a more meaningful way

## Features
### Front-End:
* A minimalist User Interface
* Accepts CSV files
* Sends CSV files from Front-End to Back-End for processing  
(Via an XHR request from Javascript to Flask)
* Displays an ML scatter plot diagram
* Allows user to download a sorted CSV output

### Back-End:
* Accepts POST requests
* Saves output to local drive
* Unsupervised Machine Learning

## 5-Step Machine Learning Process
* Reading input data
* TF-IDF Model
* Filtering
* Clustering using K-Means
* Data Visualisation

## Technology Stack
* HTML
* CSS
* JavaScript
* Flask
* Python (+ scikit.learn)
* Splunk *
* Docker *

#### The original version of this application was run with Splunk and Docker
