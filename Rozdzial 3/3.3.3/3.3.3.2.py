def odczytPlikuJson():
    f = open('plik.json')

    data = json.load(f)

    for key,value in data.items():
        print(key,value)

    print(data)
    # Closing file
    f.close()