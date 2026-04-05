meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }


word = input("cual palabra quieres conocer")
#meme_dict.keys() = ["cringe", "lol"]

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("esa palabra aun no ha sido agregada")

