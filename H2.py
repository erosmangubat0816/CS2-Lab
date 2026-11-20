def find(items, target):
    if items in target:
        return target.index(search)
    return -1

titles = []
copies = []

for i in range(3):
    title = input("Title: ")
    num_copies = int(input("Copies: "))
    
    titles.append(title)
    copies.append(num_copies)

search_title = input("Search title: ")

if search_title in titles:
    index = titles.index(search_title)
    print(search_title, "has", copies[index], "copies")
else:
    print("Not in the library")