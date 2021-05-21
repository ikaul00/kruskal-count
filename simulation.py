import random
NO_OF_CARDS = 52
Deck =[]
Ctr_victim = 0 #the counter of the victim
Ctr_mag = 0 #the counter of the magician
match = 0
Run_count = 0
#initialising the deck for the spelled out card variation
#words = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 4, 5, 4]
#Deck = [words[i%13] for i in range (NO_OF_CARDS)]
#initialising the deck for the original trick with face cards as 5
Deck =[(i % 13) + 1 for i in range (NO_OF_CARDS)]
for i in range (NO_OF_CARDS):
  if ((i % 13) + 1) > 10:
    Deck[i] = 5
#takes the given deck and its size as parameters and returns the shuffled deck
def shuffle_deck(Deck, i):
  while i > 0:
    j = (random.randint (0, 1000000)) % i
    temp = Deck[i]
    Deck[i] = Deck[j]
    Deck[j] = temp
    i = i - 1
return Deck

for k in range (1000000):
  shuffle_deck(Deck, NO_OF_CARDS-1)

  Ctr_victim = random.randint (0, 1000000) % 10
  while Ctr_victim + Deck[Ctr_victim] < NO_OF_CARDS:
    Ctr_victim = Ctr_victim + Deck[Ctr_victim]
  #the case where the magician chooses a random number
  Ctr_mag = random.randint (0, 1000000) % 10
  #the case where the magician chooses the first card
  #Ctr_mag = 0
  while Ctr_mag + Deck[Ctr_mag] < NO_OF_CARDS:
    Ctr_mag = Ctr_mag + Deck[Ctr_mag]

  if Ctr_mag == Ctr_victim:
    match = match + 1
  Run_count = Run_count + 1
print (100 *(match / Run_count))
