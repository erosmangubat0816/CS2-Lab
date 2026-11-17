scores = []
for i in range(5):
  s = int(input("Score: "))
  scores.append(s)

total = 0
for s in scores:
  if s >= 75:
    total += 1

print (total,"of 5 passed")