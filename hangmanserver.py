import asyncio
import random
import websockets
import json
import sys

wordlist = [{"word": "apple", "hint": "A red fruit which is good for health", "second_hint": "A company which makes phones"},
            {"word": "banana", "hint": "A yellow fruit which monkeys like", "second_hint": "Inferno's Mid to B"},
            {"word": "orange", "hint": "A fruit which is orange in color", "second_hint": "Obviously not tangarine"},
            {"word": "sedan", "hint": "A word to call cars with 4 doors", "second_hint": "A car body type"},
            {"word": "honda", "hint": "A car brand or a Street Fighter character", "second_hint": "A car brand which makes Civic and Accord"},
            {"word": "hawaii", "hint": "A state in the US", "second_hint": "A state which is a group of islands"},
            {"word": "kiryu", "hint": "A character from Like a Dragon (Formerly known in the west as Yakuza) series", "second_hint": "The Dragon of Dojima"},
            {"word": "python", "hint": "A programming language", "second_hint": "A type of snake"},
            {"word": "websocket", "hint": "A protocol for web communication", "second_hint": "The URI starts with ws://"},
            {"word": "uefi", "hint": "A firmware interface", "second_hint": "A replacement for BIOS"},
            {"word": "cinnamon", "hint": "A spice and a desktop environment", "second_hint": "A spice which is brown in color"},
            {"word": "almaty", "hint": "A city in Kazakhstan" , "second_hint": "A city which is the former capital of Kazakhstan"},
            {"word": "almalinux", "hint": "A linux distribution which is a replacement for CentOS", "second_hint": "Another is Rocky Linux"},
            {"word": "shoothouse", "hint": "A map in Call of Duty: Modern Warfare", "second_hint": "It's not Shipment"},
            {"word": "inferno", "hint": "A map in Counter-Strike: Global Offensive", "second_hint": "A map which is set in Italy"},
            {"word": "nishikiyama", "hint": "A character from Like a Dragon (Formerly known in the west as Yakuza) series}", "second_hint": "Kiryu's sworn brother"},
            {"word": "globemaster", "hint": "A cargo plane", "second_hint": "C-17"},
            {"word": "dotonbori", "hint": "A place in Osaka, Japan", "second_hint": "Glico Man"},
            {"word": "omgkawaiiangel", "hint": "The main character of Needy Streamer Overload", "second_hint": "Shorthand name is KAngel"},
            {"word": "modbus", "hint": "An industrial communication protocol", "second_hint": "A protocol which is used in SCADA"},
            {"word": "manchester", "hint": "A port city in England", "second_hint": "Hosts 2 Premier League clubs"},
            {"word": "senjougahara", "hint": "A character from Bakemonogatari", "second_hint": "Araragi's girlfriend"},
            {"word": "v", "hint": "A playable character in Cyberpunk 2077", "second_hint": "Come on... it's obvious"},
            {"word": "spring", "hint": "A season, a framework, and a water source", "second_hint": "A mechanical part which is used to store energy"},
            {"word": "judgment", "hint": "A spinoff of Like a Dragon (Formerly known in the west as Yakuza) series starring Takuya Kimura", "second_hint": "The Japanese release is named 'Judge Eyes'"},
            {"word": "reimu", "hint": "A character from Touhou Project", "second_hint": "The Hakurei Shrine Maiden"},
            {"word": "hockenheim", "hint": "A city in Germany, famous for its racetrack", "second_hint": "A city which hosts the German Grand Prix"},
            {"word": "saarbrucken", "hint": "A city in Germany near the border of France", "second_hint": "A city which is the capital of Saarland"},
            {"word": "svelte", "hint": "A javascript framework", "second_hint": "A javascript framework which compiles to vanilla JavaScript"},
            {"word": "pripyat", "hint": "A city in Ukraine, near the Chernobyl Nuclear Power Plant", "second_hint": "S.T.A.L.K.E.R. fans will know that you can only get the Gauss Rifle here"},
            {"word": "clarkson", "hint": "A former Top Gear presenter", "second_hint": "The oldest of the bunch"},
            {"word": "hammond", "hint": "Wrecking Ball's pilot name in Overwatch", "second_hint": "Shares the same name with a former Top Gear presenter"},
            {"word": "durian", "hint": "A fruit which is spiky and smells bad", "second_hint": "A fruit which is banned on the Singapore MRT"},
            {"word": "sakura", "hint": "A tree which is pink in color. The answer is in Japanese", "second_hint": "Not the same as the answer above, but it's the same tree"},
            {"word": "hokkaido", "hint": "A prefecture in Japan", "second_hint": "The northernmost prefecture in Japan"},
            {"word": "okinawa", "hint": "A prefecture in Japan, referred to as an 'US aircraft carrier'", "second_hint": "The southernmost prefecture in Japan"},
            {"word": "weiss", "hint": "A character from RWBY", "second_hint": "The white one"},
            {"word": "tachanka", "hint": "A horse drawn carriage with a machine gun, but you may know him as a Rainbow Six Siege operator", "second_hint": "The Lord"},
            {"word": "vozrozhdeniya", "hint": "An island in the Aral Sea, which was used for biological weapon testing. Very popular among Warzone players.", "second_hint": "MY NAME IS VIKTOR REZNOV AND I WILL HAVE MY REVENGE!"},
            {"word": "majima", "hint": "A character from Like a Dragon (Formerly known in the west as Yakuza) series", "second_hint": "The Mad Dog of Shimano"},
            {"word": "verdansk", "hint": "A fictional city in Call of Duty: Warzone", "second_hint": "The first Warzone map"},
            {"word": "yanov", "hint": "A train station in the vicinity of Pripyat", "second_hint": "A train station which is the main hub in S.T.A.L.K.E.R.: Call of Pripyat"},
            {"word": "prolog", "hint": "A programming language", "second_hint": "A logic programming language, to be exact"},
            {"word": "systemd", "hint": "An init", "second_hint": "A system and service manager which is used in most Linux distributions"},
            {"word": "kde", "hint": "A desktop environment", "second_hint": "The default DE for openSUSE"},
            {"word": "sarthe", "hint": "A department in France", "second_hint": "Hosts the 24 Hours of Le Mans"},
            {"word": "leclerc", "hint": "A French F1 driver", "second_hint": "The current Ferrari driver"},
            {"word": "dunkerque", "hint": "A city in France", "second_hint": "Brits, historians and World of Warships players will know this as Dunkirk"},
            {"word": "dover", "hint": "A city in England", "second_hint": "Eric Johnson's instrumental song is called Cliffs of what?"},
            {"word": "price", "hint": "A character from Call of Duty: Modern Warfare", "second_hint": "Captain"},
            {"word": "soap", "hint": "A bar of glycerin", "second_hint": "Also a character from Call of Duty: Modern Warfare"},
            {"word": "brimstone", "hint": "An archaic term for sulfur", "second_hint": "A character from Valorant"},
            {"word": "jett", "hint": "A character from Valorant", "second_hint": "Unsurprisingly, she cannot revive you, Omen."},
            {"word": "karen", "hint": "One of the Araragi sisters from Monogatari series", "second_hint": "The one who had her teeth brushed by Araragi"},
            {"word": "pipimi", "hint": "A character from Pop Team Epic", "second_hint": "The taller one"},
            {"word": "popuko", "hint": "A character from Pop Team Epic", "second_hint": "The shorter one"},
            {"word": "pass", "hint": "The suffixes for this word are word, phrase, code", "second_hint": "What you would type if you couldn't think of a constructor in Python"},
            {"word": "jarate", "hint": "An item in Team Fortress 2", "second_hint": "Which is a jar of urine"},
            {"word": "goodsprings", "hint": "A town in the outskirts of Las Vegas", "second_hint": "The starting town in Fallout: New Vegas"},
            {"word": "fenway", "hint": "A park in Boston", "second_hint": "The home of the Boston Red Sox"},
            {"word": "tea", "hint": "A drink which is popular in the UK", "second_hint": "What did they drop into the Boston Harbor?"},
            {"word": "glasgow", "hint": "A city in Scotland", "second_hint": "The largest one too"},
            {"word": "ullapool", "hint": "A town in Scotland", "second_hint": "Demoman's hometown"},
            {"word": "wales", "hint": "A country in the UK", "second_hint": "The one with the dragon"},
            #{"word": "llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch", "hint": "A town in Wales", "second_hint": "The longest town name in Europe"}, #i am sorry
            {"word": "alert", "hint": "A type of message box", "second_hint": "Northernmost permanently inhabited place in the world"},
            {"word": "alaska", "hint": "A state in the US", "second_hint": "One of the worst Russian Empire's screwups in history"},
            {"word": "siberia", "hint": "A region in Russia", "second_hint": "Which boasts nothing but snow and gulags"},
            {"word": "gulag", "hint": "A prison in Soviet Russia", "second_hint": "When you gets killed in Warzone, you will be sent here"},
            {"word": "eve", "hint": "A game about spaceships", "second_hint": "Which somehow holds the record of the most costly battle in gaming history at $300,000"},
            {"word": "stalker", "hint": "A game about scavenging in the Chernobyl Exclusion Zone", "second_hint": "The first game is called Shadow of Chernobyl"},
            {"word": "ryuji", "hint": "A character from Like a Dragon (Formerly known in the west as Yakuza) series", "second_hint": "The Dragon of Kansai. But no don't call him that"},
            {"word": "kabukicho", "hint": "A district in Tokyo", "second_hint": "Which is the main inspiration for Kamurocho"},
            {"word": "shimokitazawa", "hint": "A district in Tokyo", "second_hint": "Which is the setting of Bocchi The Rock!"},
            {"word": "akiyama", "hint": "A character from Like a Dragon (Formerly known in the west as Yakuza) series", "second_hint": "The Lifeline of Kamurocho"},
            {"word": "akiyama", "hint": "A character from K-On!", "second_hint": "The bassist"},
            {"word": "akiyama", "hint": "A character from Girls und Panzer", "second_hint": "The loader"},
            {"word": "quake", "hint": "A game about shooting monsters", "second_hint": "Kickstarted the whole Speedrunning scene"},
            {"word": "doom", "hint": "A game about shooting demons", "second_hint": "The father of all FPS games"},
            {"word": "postal", "hint": "A game about shooting people", "second_hint": "The second game never tells you to go postal. It's all your doing."},
            {"word": "morrowind", "hint": "A The Elder Scrolls game", "second_hint": "The hardest one."},
            {"word": "oblivion", "hint": "A The Elder Scrolls game", "second_hint": "The one with Patrick Stewart"},
            {"word": "skyrim", "hint": "A The Elder Scrolls game", "second_hint": "The one that Todd Howard managed to port to everything"},
            {"word": "biohazard", "hint": "The Japanese name of a game about shooting zombies", "second_hint": "The fourth installment got ported to everything. Last port is the port to iPhone 15"},
            {"word": "talinn", "hint" : "A city in the Baltic region", "second_hint": "The capital of Estonia"},
            {"word": "belgrade", "hint": "A city in one of the ex-Yugoslavian countries", "second_hint": "The capital of Serbia"},
            {"word": "kosovo", "hint": "A country in the Balkans", "second_hint": "Not officially recognized by Serbia"},
            {"word": "slovenia", "hint": "A country in the Balkans", "second_hint": "The only Balkan country which is in the EU"},
            {"word": "cern", "hint": "A research organization in Switzerland", "second_hint": "Famous works include: World Wide Web, the Large Hadron Collider, and the discovery of the Higgs Boson"},
            {"word": "tarkov", "hint": "The setting of Escape from Tarkov", "second_hint": "The first hint is obvious."},
            {"word": "erangel", "hint": "A map from a Battle Royale game", "second_hint": "THE OG map"},
            {"word": "nodered", "hint": "A programming tool", "second_hint": "Low-code for automation"},
            {"word": "skadovsk", "hint": "A ship in S.T.A.L.K.E.R.: Call of Pripyat", "second_hint": "The first place you will visit in the game"},
            {"word": "cupra", "hint": "A car brand", "second_hint": "A performance brand of SEAT"},
            {"word": "senna", "hint": "A McLaren F1 (Formula 1, not the F1 model) driver", "second_hint": "Also the name of a McLaren model"},
            {"word": "montecarlo", "hint": "A circuit in Monaco", "second_hint": "Also the algorithm for random number generation"},
            {"word": "monaco", "hint": "A country in Europe", "second_hint": "The second smallest country in the world"},
            {"word": "saejima", "hint": "A character from Like a Dragon (Formerly known in the west as Yakuza) series", "second_hint": "The Tiger of Tojo Clan"},
            {"word": "makoto", "hint": "A common unisex name in Japan", "second_hint": "Used as the name for a character in Persona 5, Persona 3, Yakuza 0, Street Fighter. Also famous for beign the name of a filmmaker who made Kimi no Na wa"},
            {"word": "maimai", "hint": "A rhythm game", "second_hint": "Often mistaken for a washing machine"},
            {"word": "arma", "hint": "A simulation game", "second_hint": "That does not simulate vehicles, but rather military operations"},
            {"word": "sombra", "hint": "A character from Overwatch", "second_hint": "Spanish for shadow"},
            {"word": "lithium", "hint": "An element that explodes in water", "second_hint": "Used in batteries"},
            {"word": "unreal", "hint": "A game", "second_hint": "Always mistaken for a game engine with the same name"},
            {"word": "taiko", "hint": "A rhythm game", "second_hint": "The one with the drum"},
            {"word": "drummania", "hint": "A rhythm game", "second_hint": "That's not Taiko no Tatsujin. Also it's much, much harder than whatever Whiplash has"},
            {"word": "java", "hint": "An island in Indonesia", "second_hint": "Also a programming language"},
            {"word": "go", "hint": "A verb", "second_hint": "Also a programming language"},
            {"word": "rust", "hint": "A programming language", "second_hint": "Also the famous 1v1 map from Call of Duty: Modern Warfare 2"},
            {"word": "kashiwagi", "hint": "A character from Like a Dragon (Formerly known in the west as Yakuza) series", "second_hint": "Got a huge scar on his face"},
            {"word": "groza", "hint": "An assault rifle in the Russian military", "second_hint": "Chambered in 9x39mm. Also obsolete because the AK-74M still works."},
            {"word": "gyoza", "hint": "A Japanese dumpling", "second_hint": "Can be eaten steamed or fried, but who eats steamed anyway?"},
            {"word": "pylance", "hint": "A language server for Python", "second_hint": "One of the most based language servers out there"},
            {"word": "kashima", "hint": "A character from Kantai Collection", "second_hint": "The first ship you will get in the game"},
            {"word": "shimakaze", "hint": "A destroyer in the Imperial Japanese Navy", "second_hint": "The fanart of it is.... well... You know what I mean. The ship which is referred to as male."},
            {"word": "maven", "hint": "A build tool", "second_hint": "Alternatives includes Gradle and Ant"},
            {"word": "hijacked", "hint": "A map in Call of Duty: Black Ops 2", "second_hint": "The one with the yacht"},
            {"word": "nuketown", "hint": "A map in Call of Duty: Black Ops", "second_hint": "Looks like that scene from Indiana Jones and the Kingdom of the Crystal Skull"},
            {"word": "tensor", "hint": "A data structure", "second_hint": "3D arrays"},
            {"word": "subaru", "hint": "A car brand", "second_hint": "Or a name of a Vtuber"},
            {"word": "yui", "hint": "A character from K-On!", "second_hint": "The lead guitarist"},
            {"word": "mio", "hint": "A character from K-On!", "second_hint": "The bassist"},
            {"word": "azusa", "hint": "A character from K-On!", "second_hint": "The rhythm guitarist"},
            {"word": "ritsu", "hint": "A character from K-On!", "second_hint": "The drummer"},
            {"word": "tsumugi", "hint": "A character from K-On!", "second_hint": "The keyboardist"},
            {"word": "vorkuta", "hint": "A city in Russia", "second_hint": "1. Secure the keys. 2. Ascend from darkness. 3. Rain fire. 4. Unleash the horde. 5. Skewer the winged beast. 6. Wield a fist of iron. 7. Raise hell. 8. Freedom."},
            {"word": "oarai", "hint": "A town in Ibaraki, Japan", "second_hint": "The setting of Girls Und Panzer"},
            {"word": "r", "hint": "A programming language", "second_hint": "The one which is used for data science"},
            {"word": "julia", "hint": "A programming language", "second_hint": "The one which is used for data science"},
            {"word": "marrakesh", "hint": "A city in Morocco", "second_hint": "The setting of Hitman 2016's third episode"},
            {"word": "vermont", "hint": "A state in the US", "second_hint": "Whittleton Creek is set here"},
            {"word": "melbourne", "hint": "A city in Australia", "second_hint": "Hosts a race in the F1 calendar"},
            {"word": "jakarta", "hint": "A capital city in Indonesia", "second_hint": "Also the name for Eclipse's Java EE Implementation"},
            {"word": "urzikstan", "hint": "A fictional country in Call of Duty: Modern Warfare", "second_hint": "The one which is invaded by Russia"},
]

#or.. you know... make a class like a normal person. this is the backend after all
from dataclasses import dataclass

#god bless dataclasses
@dataclass
class HangmanWord:
    word: str
    hint: str
    sechint: str

classwordlist = [HangmanWord(x["word"], x["hint"], x["second_hint"]) for x in wordlist]
#or just use json. websocket talks in json anyway

class HangmanGame:
    def __init__(self) -> None:
        self.word = ""
        self.hint = ""
        self.guessed = []
        self.lives = 6
        self.gameover = False
        self.second_hint = ""
        self.is_second_hint = False
    
    def start(self):
        random_word = random.choice(wordlist)
        self.word = random_word["word"]
        self.hint = random_word["hint"]
        self.second_hint = random_word["second_hint"]

    def guess(self, letter):
        if letter in self.guessed:
            return 
        self.guessed.append(letter)
        if letter not in self.word:
            self.lives -= 1
        if self.lives == 0:
            self.gameover = True
        if all(letter in self.guessed for letter in self.word):
            self.gameover = True


async def hangman(websocket, path):
    print("A challenger approaches")
    game = HangmanGame()
    game.start()

    #send the details about the correct answer first. the client can deal with the presentation later.
    await websocket.send(json.dumps({"type": "start", "word": game.word, "hint": game.hint}))

    async for event in websocket:
        if game.gameover:
            if game.lives == 0:
                await websocket.send(json.dumps({"type": "gameover", "message": "You lost!"}))
                break
            else:
                await websocket.send(json.dumps({"type": "gameover", "message": "You won!"}))
                break
        data = json.loads(event)
        game.guess(data["letter"].lower())

        if game.lives == 3 and not game.is_second_hint:
            game.is_second_hint = True
            await websocket.send(json.dumps({"type": "guess", "guessed": game.guessed, "lives": game.lives, "word": game.word, "gameover": game.gameover, "second_hint": game.second_hint}))
        else:
            await websocket.send(json.dumps({"type": "guess", "guessed": game.guessed, "lives": game.lives, "word": game.word, "gameover": game.gameover}))

        if game.gameover:
            if game.lives == 0:
                await websocket.send(json.dumps({"type": "gameover", "win": False, "word": game.word}))
                break
            else:
                await websocket.send(json.dumps({"type": "gameover", "win": True}))
                break

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python hangmanserver.py <ip address> <port>")
        exit(1)

    address = sys.argv[1]
    port = sys.argv[2]

    start_server = websockets.serve(hangman, address, port)
    print("Server started")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()