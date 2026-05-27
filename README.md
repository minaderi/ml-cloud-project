# Cloud-Based Machine Learning Traffic Prediction System

## Project Description
This project is a cloud-based machine learning application developed using Python, Flask, Scikit-learn, and AWS S3.

The system predicts traffic density based on temperature and humidity values.

## Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- AWS S3

## Features
- Traffic density prediction
- REST API service
- Machine learning model training
- Cloud storage integration with AWS S3

## Example API Request

POST /predict

Example JSON:

{
  "temperature": 32,
  "humidity": 78
}

## Example Response

{
  "prediction": "high"
}