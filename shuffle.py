import random
 
def randomhallo(woord):
    randomised = ''.join(random.sample(woord, len(woord)))
    return randomised
 
print(randomhallo("peer"))
print(randomhallo("appel"))
print(randomhallo("banaan"))
