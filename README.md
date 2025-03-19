# Phishing-Detection
# Overview
The Phishing Detection System is a tool designed to detect phishing websites using existing APIs to analyze URLs. Instead of relying on machine learning, the system evaluates website characteristics by querying external APIs and generates a confidence score to classify a URL as either phishing or legitimate.

This system helps users avoid phishing attacks by flagging suspicious websites and providing a risk score based on various indicators.

# Features
1. URL Analysis
The system queries external APIs to analyze URLs for suspicious patterns and characteristics such as domain name anomalies, URL structure, and site behavior.
2. Confidence Score
Based on the results from the APIs, the system generates a confidence score that indicates the likelihood of a website being phishing or legitimate.
A higher score indicates a higher likelihood of the website being phishing.
3. Real-Time Detection
The system provides real-time detection, offering instant results and feedback to the user on whether a website is potentially harmful.
4. API Integration
The system uses well-established external APIs to evaluate URLs, ensuring up-to-date and accurate assessments of websites.

# Technologies Used
Backend: Python

External APIs: Google Safe Browsing, IPQualityScore

Frontend: Flask (for web interface, if applicable)

# Installation
Prerequisites:

Python 3.x

Flask

# Usage
Once the application is running, simply enter a URL in the provided input field to get a confidence score. Based on the score, the system will classify the URL as either a legitimate website or a potential phishing attempt.

# Contributing
Feel free to fork the repository, submit issues, or create pull requests to enhance the system. Contributions are welcome!
