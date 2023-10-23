import websockets
import asyncio
import json

async def play():
    async for websocket in websockets.connect("ws://localhost:8765"): #connect to the server. localhost for testing. for presentation, we'll put the server in the remote server
        print("Hangman")
        print("Lives: 6")

        #wait for the server to send the word and the hint
        event = await websocket.recv()
        data = json.loads(event)

        print("The word has {} letters".format(len(data["word"])))
        print("Hint: {}".format(data["hint"]))

        while True:
            print("Guess a letter: ")
            letter = input()
            if len(letter) != 1:
                print("Please enter a single letter")
                continue
            await websocket.send(json.dumps({"letter": letter}))
            event = await websocket.recv()
            data = json.loads(event)
            if data["type"] == "guess":
                print("Word: {}".format("".join(letter if letter in data["guessed"] else "_" for letter in data["word"])))
                print("Guessed: {}".format(data["guessed"]))
                print("Lives: {}".format(data["lives"]))
            #check if second hint is in the data
            if "second_hint" in data:
                print("Second hint: {}".format(data["second_hint"]))
            if data["gameover"]:
                event = await websocket.recv()
                data = json.loads(event)
                if data["type"] == "gameover":
                    if data["win"]:
                        print("You win!")
                    else:
                        print("You lose!")
                        print("The word was {}".format(data["word"]))
                    break

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(play())