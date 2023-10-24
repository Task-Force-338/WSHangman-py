# WSHangman-py
An Operating System project that forces us to write a hangman game that uses ~~websockets~~ just TCP sockets. This one is Python.

I know. I screwed up by writing it to use Websockets and `asyncio`. I'm not fixing it. For non-websocket, see the Java version.

# Pre-requisites
- You have to **be a human being**. Unless you are going to write a `pyautogui` script to play the game for you. In that case, go ahead. I'm not stopping you.
    - You also need a basic understanding on English vocabulary. If you don't know what a word means, you can always look it up on Google.
    - (Optional) Implement a Neuro-sama-like Vtuber AI to play the game for you.
    - (Optional) You also should have basic knowledge on:
      - Programming
      - Ryu Ga Gotoku Series
      - Call of Duty
      - Planes
      - Counter-Strike
      - Industrial Communication Protocols
      - ~~How to write a good README~~
      - Gepgraphy of Japan
      - Racing
      - S.T.A.L.K.E.R.
      - Cold War History
      - Linux
      - Valorant
      - TF2
      - British Empire
      - K-On!
      - Balkan Geography
      - Geopolitics of Ex-Soviet States
      - Cars
      - Japanese Arcade Games
      - Food
      - Yuri (the genre, not the Russian name)
      - Yuri (the Russian name, not the genre)
- You'll need **any computing device** that can run Python 3.6 or higher. I'm using an Acer Nitro, but I have confirmed that it also works with a guest under an ESXi host and a Raspberry Pi 4. If you're feeling fancy you can also run it on a EC2 instance. Just make sure that you shut it down when you're done.
- You'll need **Python 3.6 or higher**. I'm using whatever version of Python that comes with Rocky Linux 9.
- You'll need **the `websockets` module**. Install it with `pip3 install websockets`.
- You'll need **Docker or Podman** if you want to **run the server in a container.** You'll also need to build the image first. The ability to build images comes with every copy of Docker Engine and Podman.

# Usage

### Server
Run the Server (preferrably raw, but Docker is cooler so you might want to do that.)
Or use Podman, because Docker's business decision is why Podman exists in the first place. You have to build the image first, though.

```bash
# Raw
$ python3 hangmanserver.py <address> <port>

# Docker
$ docker build -t wshangman-py .
# please do not name the image Sayori, please.
$ docker run -p 8765:8765 wshangman-py

# Podman
# You know that Podman is a drop-in replacement for Docker, right?
$ podman build -t wshangman-py .
$ podman run -p 8765:8765 wshangman-py
```
### Client

Run the Client. The game will loop forever until you ragequit.
Don't worry. I'll make it so that you can quit the game without ragequitting. Check issue #1.

```bash
$ python3 client.py

# Why would you want to run the client in a container?
```

Regarding on how to play the game, I'll let you figure it out yourself. I'm not going to spoonfeed you.

## Regarding Docker Compose
Why would you even need Docker Compose for this? It's a single container. You can just run it with Docker or Podman.

# Report Bugs
cope.

# License
Licensed under ~~WTFPL. This shit isn't worth it bros.~~ BSD 3-Clause License.

![](https://steamuserimages-a.akamaihd.net/ugc/965345547598415674/CD26A9222173195870AEA9AD6887C9CA3EEEC546/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false)
