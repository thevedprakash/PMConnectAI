# PMConnectAI

PMConnectAI is a project designed to automate conversations with professionals via Slack, using a custom script that leverages a UI for easy input. This project supports running the script through a Streamlit interface, FastAPI for backend service, Docker for containerization, and deployment on Google Cloud Run and GKE with CI/CD using GitHub Actions and ArgoCD.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Phase I: Streamlit UI](#phase-i-streamlit-ui)
- [Phase II: FastAPI and Docker](#phase-ii-fastapi-and-docker)
- [Phase III: Deployment](#phase-iii-deployment)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.9+
- pip
- Virtual Environment
- Docker
- Google Cloud SDK
- kubectl
- ArgoCD CLI
- Node.js (for some GKE setups)

### Setup Virtual Environment

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/PMConnectAI.git
   cd PMConnectAI
   ```

2. **Create and Activate Virtual Environment**

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running Streamlit UI

1. **Navigate to the `ui` Directory**

   ```sh
   cd ui
   ```

2. **Run Streamlit App**

   ```sh
   streamlit run app.py
   ```

### Running FastAPI App

1. **Run FastAPI**

   ```sh
   uvicorn api.app:app --reload
   ```

2. **Access the FastAPI Documentation**

   Open your browser and navigate to `http://127.0.0.1:8000/docs`.

## Project Structure

```
.
├── README.md
├── api
│   └── app.py
├── data
│   └── dataset.csv
├── k8s
│   ├── Dockerfile
│   ├── cluster
│   ├── deployment.yaml
│   └── service.yaml
├── log.txt
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── calendly.py
│   ├── config.py
│   ├── conversation.py
│   ├── main.py
│   ├── slack_integration.py
│   └── utils.py
├── test
│   ├── bot_test.py
│   ├── calendly_test.py
│   ├── config.py
│   ├── fiass_test.py
│   ├── main_test.py
│   ├── new.py
│   ├── slack_gemini_test.py
│   └── test_gemini_pro.py
└── ui
    └── app.py
```

### Code Arrangement

- **api/**: Contains the FastAPI application code.
- **data/**: Contains the dataset used for the project.
- **k8s/**: Kubernetes deployment files for container orchestration.
- **src/**: Main source code for the project including Slack integration, conversation handling, and utility functions.
- **test/**: Unit tests for various components of the project.
- **ui/**: Streamlit application for inputting email IDs and triggering the conversation script.

## Phase I: Streamlit UI

### Streamlit Setup

The Streamlit application allows users to input a list of email IDs and trigger the conversation script.

**Steps to Run:**

1. Navigate to the `ui` directory.
2. Run the Streamlit application.
3. Enter email IDs and click the "Start Conversations" button.

## Phase II: FastAPI and Docker

### FastAPI Setup

The FastAPI application provides an endpoint to start conversations for a list of email IDs.

**Steps to Run:**

1. Run the FastAPI server using Uvicorn.
2. Access the API documentation at `http://127.0.0.1:8000/docs`.

### Dockerization

Docker is used to containerize the application for consistent deployment.

**Steps to Dockerize:**

1. Build the Docker image.

   ```sh
   docker build -t conversation-app .
   ```

2. Run the Docker container.

   ```sh
   docker run -p 80:80 conversation-app
   ```

## Phase III: Deployment

### Google Cloud Run

Deploy the Dockerized application to Google Cloud Run for serverless deployment.

### GKE Deployment

Deploy the Dockerized application to Google Kubernetes Engine (GKE) for scalable container orchestration.

### CI/CD with GitHub Actions and ArgoCD

Set up CI/CD pipelines using GitHub Actions for continuous integration and ArgoCD for continuous deployment.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any improvements or additions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

### Explanation

1. **Title and Table of Contents**: Provides a clear overview of the project and navigation.
2. **Installation**: Detailed steps to set up the virtual environment and install dependencies.
3. **Usage**: Instructions on running the Streamlit and FastAPI applications.
4. **Project Structure**: Describes the directory structure and explains the purpose of each folder.
5. **Phase Descriptions**: Detailed descriptions of each phase (Streamlit UI, FastAPI and Docker, Deployment).
6. **Contributing**: Guidelines for contributing to the project.
7. **License**: Information about the project's license.

This `README.md` provides comprehensive information for understanding and working with the project, making it easier for new developers to get started.
```
