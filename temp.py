import requests

apikey = "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"

word = input("Enter your word:")

res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

print("status code:",res.status_code)

if res.status_code ==200:
    meanings = res.json()[0]["meanings"]
    for meaning in meanings:
        defn = meaning['definitions']
        for d in defn:
         print(d['definition'])

else:
    print("word not found in dictionary")