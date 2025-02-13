# Loan Approval Prediction

## Overview
This project aims to predict loan approval using machine learning techniques. It provides a comprehensive solution for financial institutions to automate and streamline their loan approval process.

## Demo Video

# Loan Approval Prediction

This repository contains the code and resources for predicting loan approval status using machine learning models.

## Demo Video

[![Watch the video](https://via.placeholder.com/800x450.png?text=Demo+Video)](https://github.com/RohitPawar001/datasets/raw/refs/heads/main/lone_approval_prediction.mp4)
## Features
- Data ingestion and preprocessing
- Machine learning model training and evaluation
- Web application for real-time predictions
- Containerized deployment using Docker

## Tech Stack
- Python
- Jupyter Notebook
- Flask
- Docker

## Project Structure
```
Lone_approval_prediction/
├── .github/workflows/
├── artifacts/data_ingestion/
├── config/
├── research/
├── src/lone_approval_prediction/
├── templates/
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
├── main.py
├── params.yaml
├── requirements.txt
├── schema.yaml
├── setup.py
└── template.py
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/RohitPawar001/Lone_approval_prediction.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the main application:
   ```
   python main.py
   ```
2. Access the web interface at `http://localhost:5000`

## Docker Deployment
1. Build the Docker image:
   ```
   docker build -t loan-approval-prediction .
   ```
2. Run the container:
   ```
   docker run -p 5000:5000 loan-approval-prediction
   ```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact
Rohit Pawar - [GitHub Profile](https://github.com/RohitPawar001)

Project Link: [https://github.com/RohitPawar001/Lone_approval_prediction](https://github.com/RohitPawar001/Lone_approval_prediction)
