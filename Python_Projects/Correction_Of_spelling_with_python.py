from textblob import TextBlob

incorrect = ['Machne', 'Learnineg']
correct = []
for i in incorrect:
    correct.append(TextBlob(i))

for i in correct:
    print(i.correct())

