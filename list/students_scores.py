scores = [56, 78, 90, 45, 89, 62, 70, 88, 95, 33, 77, 100, 67]

#Total no of scores in the list.
print(len(scores))

#The highest and the lowest score in the list
print(max(scores))
print(min(scores))

#Calculating the average score(rounded to 2 decimal places.)
avg = (sum(scores) / len(scores))
print(round(avg, 2))

#score >= 60
passed = []
for score in scores :
    if score >= 60 :
        passed.append(score)
print(passed)

#sorting the passed list in descending and ascending order and print it
print(sorted(passed, reverse=True))
print(sorted(passed, reverse=False))

#Replacing the last score in the original score list with 68
scores[-1] = 68
print(scores)

#Remove the lowest score from the original score list
scores.remove(min(scores)) 
print(scores)

#print first five scores
print(scores[0:6])






