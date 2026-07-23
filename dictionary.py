import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return f"No definition found for '{word}'."

    data = response.json()
    meanings = data[0]["meanings"]

    result = f"\n📖 {word.upper()}\n"
    for meaning in meanings:
        part_of_speech = meaning["partOfSpeech"]
        result += f"\n({part_of_speech})\n"
        for i, definition in enumerate(meaning["definitions"][:2], 1):
            result += f"  {i}. {definition['definition']}\n"

    return result


if __name__ == "__main__":
    word = input("Enter a word: ")
    print(get_definition(word))