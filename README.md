# Docker Network Demo - Flask Apps

A simple demonstration of two Flask applications communicating over a custom Docker network.

## Features
- Two Flask microservices (`app1` and `app2`)
- Custom bridge network for inter-container communication
- `app2` calls `app1` using service name (`app1:5001`)
- Interactive form on App2 that sends data to App1

## Project Structure
```text
├── docker-compose.yml
├── app1/
│   ├── Dockerfile
│   └── app.py
├── app2/
│   ├── Dockerfile
│   └── app.py
└── README.md
```

## How to Run

```bash
docker-compose up --build -d
```

Open your browser and navigate to: `http://localhost:5002`

## What You'll See
1. **App2 shows a form**
2. **Enter your name → Submit**
3. **App2 calls App1 over the Docker network and displays the response**

## Useful Commands

```bash
docker-compose down              # Stop containers
docker-compose up --build -d     # Rebuild and start
docker-compose logs -f           # View logs
docker ps                        # Check running containers
```
