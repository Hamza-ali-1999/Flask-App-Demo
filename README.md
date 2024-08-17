# **Skin Cancer Lesion Detection Project**

## **Overview**

Skin cancer is one of the most prevalent forms of cancer globally, affecting millions each year. Early detection is crucial for effective treatment, as delayed diagnosis can lead to severe consequences. This project aims to develop an accurate, accessible, and easy-to-use skin cancer detection system using machine learning, particularly focusing on image classification to assist in early detection and diagnosis.

## **Problem Statement**

- **Global Impact**: Skin cancer is the most common cancer worldwide.
- **Need for Early Detection**: Early diagnosis significantly improves treatment outcomes.
- **Challenge in Diagnosis**: The visual nature of skin cancer makes it difficult to diagnose accurately, with high variability in appearance.
- **Objective**: Develop a machine learning model that classifies skin lesions as benign or malignant, providing an accessible tool for both patients and healthcare professionals.

## **Project Significance**

An accurate skin cancer detection system can:
- **Reduce Treatment Costs**: Early diagnosis can lead to early intervention, reducing overall treatment costs.
- **Increase Accessibility**: Providing patients with a tool for frequent self-checks can lead to earlier detection.
- **Improve Patient Outcomes**: Quick and accurate diagnosis can set patient priority and improve treatment processes.

## **Methodology**

### **Model Development**

- **Past Projects**: 
  - Participated in a Kaggle competition for skin cancer binary classification.
  - Experimented with YOLO v5 for skin lesion object detection, though this was not integrated into the final deployment due to viability concerns.

- **Model Benchmarking**:
  - Initially trained models like EfficientNet and DenseNet, focusing on loss function metrics to compare performance against publicly available benchmarks.
  - Conducted manual evaluation of model predictions to ensure reliability, particularly in distinguishing between malignant and benign cases.

- **Model Update**:
  - For the final deployment, the trained model was replaced with a pre-trained Vision Transformer model from Hugging Face. This decision was made to enhance the accuracy and reliability of the predictions.

### **Machine Learning Canvas**

- **Prediction Task**: A classification task on skin lesion images with possible outcomes being benign or malignant.
- **Value Proposition**: The end-users, primarily healthcare professionals and patients, benefit from an accessible and accurate diagnosis tool.
- **Data Collection & Sources**: Initial training data was sourced from public datasets (e.g., ISIC). Continuous updates would rely on new patient data, if accessible.
- **Model Deployment**: The model is deployed using Docker and Google Cloud Platform (GCP), ensuring scalability and accessibility.
- **Challenges**: Faced issues with library conflicts, front-end design, and managing the Docker image size.

## **Model Deployment**

### **Dockerization**

- Created a Dockerfile to containerize the Flask application.
- Built the Docker image and pushed it to Docker Hub for easy deployment across different environments.

### **Google Cloud Platform (GCP) Setup**

- Initialized a cloud project on GCP and enabled necessary APIs.
- Deployed the Docker image using Google Cloud Run, which offers a serverless deployment option.
- Manually tested the deployment to ensure the application runs as expected.

### **Challenges Faced**

- **Library Conflicts**: Encountered issues with conflicting library versions, which required careful management during deployment.
- **Front-End Development**: Designing an intuitive and user-friendly interface was a challenge, given the technical nature of the project.
- **Docker Image Optimization**: The initial Docker image was too large due to the inclusion of the model file; in future iterations, external model loading will be considered.
- **Model Update**: Replaced the initially trained model with a Vision Transformer from Hugging Face for more accurate and robust predictions.

## **Demonstration & Future Work**

The deployed application can be accessed online, allowing users to upload images of skin lesions for analysis. The application provides predictions along with a confidence score, guiding users in seeking further medical advice.

### **Demo Link**: [Skin Cancer Detector](https://scdwebdeployment-kivpee72oq-uc.a.run.app/)

### **Future Enhancements**

- **Ensemble Models**: Integrating additional patient data, such as blood tests, could enhance the accuracy of the system through ensemble modeling.
- **System Integration**: Working towards integration with healthcare systems for real-time patient data access and better prediction accuracy.
- **Optimization**: Refining the Docker image and improving the application's responsiveness to handle higher traffic and larger datasets.


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


