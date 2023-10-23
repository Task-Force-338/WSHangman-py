# WSHangman-py
An Operating System project that forces us to write a hangman game that uses websockets. This one is Python.

# Usage
Run the Server (preferrably raw, but Docker is cooler so you might want to do that.)
Or use Podman, because Docker's business decision is why Podman exists in the first place. You have to build the image first, though.

```bash
# Raw
$ python3 hangmanserver.py

# Docker
$ docker build -t wshangman-py .
# please do not name the image Sayori, please.
$ docker run -p 8765:8765 wshangman-py

# Podman
# You know that Podman is a drop-in replacement for Docker, right?
$ podman build -t wshangman-py .
$ podman run -p 8765:8765 wshangman-py
```

Run the Client. The game will loop forever until you ragequit.
Don't worry. I'll make it so that you can quit the game without ragequitting. Check issue #1.

```bash
$ python3 client.py

# Why would you want to run the client in a container?
```

## Regarding Docker Compose
Why would you even need Docker Compose for this? It's a single container. You can just run it with Docker or Podman.

# Report Bugs
cope.

# License
Licensed under ~~WTFPL. This shit isn't worth it bros.~~ BSD 3-Clause License.

![](https://steamuserimages-a.akamaihd.net/ugc/965345547598415674/CD26A9222173195870AEA9AD6887C9CA3EEEC546/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false)
