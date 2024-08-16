# Skin Cancer Detection Demo (Flask Web Application)

## Overview
This repository contains a Flask web application designed for the early and accurate detection of skin cancer. The application utilizes a deep learning model to classify skin lesions, helping healthcare providers and patients identify potential cases of skin cancer quickly and efficiently. Early detection is crucial in treating skin cancer, particularly melanoma, which can be deadly if not caught early.

## Problem Statement
Skin cancer is one of the most common and rapidly increasing forms of cancer worldwide. Traditional methods of diagnosis, such as visual inspections, can be subjective and may lead to misdiagnosis. This application addresses the need for a reliable, accessible, and non-invasive tool to assist in the early detection of skin cancer, ultimately improving patient outcomes.

## Benefits of the Application
Early Detection: Assists in identifying skin cancer at an early stage, increasing the chances of successful treatment.
Accessibility: Provides an easy-to-use interface accessible to both healthcare providers and patients.
Efficiency: Reduces the burden on dermatologists by offering an AI-powered second opinion.
Scalability: Deployable across various environments, making it accessible globally.

## Repository Structure
app.py: The main Python file that contains the Flask application. This file sets up the routes, handles image uploads, and performs predictions using the pre-trained model.

Dockerfile: Contains instructions to build a Docker image for the application. It specifies the environment, installs necessary dependencies, and sets up the application to run in a containerized environment.

requirements.txt: Lists all the Python libraries and dependencies required to run the application, including Flask, torch, transformers, and Pillow.

templates/: Contains HTML files that define the front-end of the application.

home.html: The landing page of the application where users can upload images.
index.html: A template for displaying results or interacting with the prediction feature.
static/: Stores static assets such as CSS, images, and JavaScript files used in the front-end.

style.css: The stylesheet for styling the web pages.
images/: Contains images used in the application, such as logos and sample images.
.dockerignore: Specifies files and directories that should be ignored when creating the Docker image, reducing the size of the image by excluding unnecessary files.

.gitignore: Lists files and directories that should be ignored by Git, such as environment files and compiled code.


