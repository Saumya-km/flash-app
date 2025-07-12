# Base image (OS)

FROM python:3.9

# Working directory

WORKDIR flash-app/

# Copy src code to container

COPY . .

# Run the upgrade commands

RUN pip install --upgrade pip

# Run the build commands

RUN pip install -r requirements.txt

# expose port 5000

EXPOSE 5000

CMD ["python","app.py"]
