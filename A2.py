scores = []
for i in range(5):
  s = int(input("What's your score?: "))
  scores.append(s)

total = 0
for s in scores:
  total = total + s
print ("Total: ", total)

average = total / len(scores)
print ("Average: ", average)