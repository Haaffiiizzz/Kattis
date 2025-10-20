text = input().split(" ")
store = {}

for word in text:
    if store.get(word, False):
        print("no")
        quit()
    else:
        store[word] = True

print("yes")

