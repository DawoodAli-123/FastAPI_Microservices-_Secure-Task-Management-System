#full image (large size ~900MB+), Not optimized for microservices. Us slim or alpine
#apk add --no-cache build-base isted apt-get, In Alpine, build-base is similar to Debian’s build-essential.  
FROM python:3.11-slim

#Creates a folder inside container, All commands run inside this directory.
WORKDIR /app

#Prevents .pyc file creation, Ensures real-time logs (important in Kubernetes)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#Refresh the list of available software packages from Debian/Ubuntu repositories.
#Automatically answer "yes" to prompts.
#It gives your container the ability to compile C/C++ code.
#Recursively and forcefully delete directory and everything inside it, without asking any questions.
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists*

#If your code changes but requirements don’t, Docker won’t reinstall dependencies.
COPY requirements.txt .
#Prevents pip cache, Reduces image size
RUN pip install --no-cache-dir -r requirements.txt

#Copies entire auth-service into container.
COPY . .

#Auth service runs on: http://localhost:8001
#In microservices: auth → 8001, task → 8002, gateway → 8000
EXPOSE 8001

#CMD tells Docker: “When the container starts, run this command.”
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--workers", "2"]
