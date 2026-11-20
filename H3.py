def count(items, target):
    total = 0
    for item in items:
        if item == target:
            total += 1
    return total

votes = []
while votes != "done":
    vote = input("Vote (done to stop): ")
    if vote == "done":
        break
    votes.append(vote)

candidate = input("Candidate: ")
vote_count = count(votes, candidate)
print(candidate, "got", vote_count, "vote(s)")