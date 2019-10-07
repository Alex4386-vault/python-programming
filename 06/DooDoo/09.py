# count occuring values

pureImagination = "Come with me and you'll be In a world of pure imagination Take a look and you'll see Into your imagination"
pureImaginationContinuation = "We'll begin with a spin Traveling in the world of my creation What we'll see will defy explanation If you want to view paradise Simply look around and view it"

pureImaginationWords = pureImagination.split(' ')
pureImaginationContinuationWords = pureImaginationContinuation.split(' ')

print(pureImaginationWords + pureImaginationContinuationWords)

thePureImaginationWords = pureImaginationWords + pureImaginationContinuationWords

print(thePureImaginationWords.count("and"))
