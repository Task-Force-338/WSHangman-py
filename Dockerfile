# Real men either use Alpine as base
# FROM alpine:latest
# and wastes their time installing all the dependencies
# RUN apk add --no-cache python3-dev \
#     && pip3 install --upgrade pip

# Or just use Python as base. That exists.
FROM python:latest 
# you can specify the version of Python you want to use, but for the sake of simplicity, I'll just use the latest version.

# Set the working directory to /app. Gotta keep things clean.
WORKDIR /app

# Copy the server file into the container at /app
COPY hangmanserver.py /app

# Is websockets in the standard library? I don't think so.
RUN pip install websockets

# Expose the port that the server will be listening on. This is for the container's side.
EXPOSE 8765

# Run the server when the container launches.
# CMD differs from RUN in that it is run when the container is launched, not when the image is built.
# CMD is also overwritten by the command line arguments when the container is launched.
# So if you want to run the server with different arguments, you can do so by changing the CMD arguments below.
CMD ["python", "hangmanserver.py", "0.0.0.0", "8765"]

# maybe return some funny strings when the server is launched?
# CMD ["echo", "Hello! I am on Team Chitoge!"]
# Maybe not, unless I specify in the license that the server is not for Onodera fans.

# technically this is a linux machine so you could just... halt the server????
# CMD ["halt"]
# don't do this

# !!! DO NOT NAME THE IMAGE SAYORI !!! 