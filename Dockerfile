# Real men either use Alpine as base
# FROM alpine:latest
# and wastes their time installing all the dependencies
# RUN apk add --no-cache python3-dev \
#     && pip3 install --upgrade pip

# Or just use Python as base. That exists.
FROM python:latest 

# Set the working directory to /app. Gotta keep things clean.
WORKDIR /app

# Copy the server file into the container at /app
COPY hangmanserver.py /app

# Is websockets in the standard library? I don't think so.
RUN pip install websockets

# Expose the port that the server will be listening on. This is for the container's side.
EXPOSE 8765

# Run the server when the container launches.
CMD ["python", "hangmanserver.py", "0.0.0.0", "8765"]

# maybe return some funny strings when the server is launched?
# CMD ["echo", "Hello! I am on Team Chitoge!"]
# Maybe not, unless I specify in the license that the server is not for Onodera fans.

# technically this is a linux machine so you could just... halt the server????
# CMD ["halt"]
# don't do this

# !!! DO NOT NAME THE IMAGE SAYORI !!! 