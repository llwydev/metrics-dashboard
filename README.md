# Resource Health Monitoring Flask App

This project is a **Resource Health Checker Dashboard** built using **Flask**, **Prometheus**, and **Grafana**.
It is designed to monitor and visualize the health of various system resources e.g CPU, RAM and Disk Usage.
 
The application is containerized and deployable using **Docker Compose**.

## Features

- **Flask**: Backend API for exposing resource metrics.
- **Prometheus**: Metrics collection and storage.
- **Grafana**: Visualization of metrics with customizable dashboards.
- **Docker Compose**: Multi-container orchestration for easy deployment.

## Prerequisites

- Docker and Docker Compose installed on your system.
- Basic understanding of Flask, Prometheus, and Grafana.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/metrics-dashboard.git
cd metrics-dashboard
```

### Build and Run the Application

1. Build and start the containers:
    ```bash
    docker-compose up --build
    ```

2. Access the services:
    - Flask API: `http://localhost:5000`
    - Prometheus: `http://localhost:9090`
    - Grafana: `http://localhost:3000` (Default login: `admin` / `admin`)

### Stopping the Application

To stop and remove the containers, run:
```bash
docker-compose down
```

## Project Structure

```
metrics-dashboard/
├── app/                # Flask application code
├── docker-compose.yml  # Docker Compose configuration
├── prometheus.yml      # Prometheus configuration
└── README.md           # Project documentation
```

## Configuration

- **Prometheus**: Configure scrape targets in `prometheus/prometheus.yml`.
- **Grafana**: Add or modify dashboards in `grafana/provisioning/dashboards/`.

## Customization

- Extend the Flask app to expose additional metrics.
- Customize Grafana dashboards to suit your monitoring needs.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Docker Compose](https://docs.docker.com/compose/)