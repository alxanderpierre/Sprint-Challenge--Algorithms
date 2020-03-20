'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  #def the function with the word parameter
  counter = 0
  # here im setting the counter to zero so it can do a += later and
  # add the number of th words.
  return th_counter(word,counter)
  # here i am returning the below function.
def th_counter(word,counter):
  # me def the th_counter function that i used above
  # i will be using recursion in this function
  if word[:2] == 'th':
    counter += 1
# counting the times th appears in the string
# since i cant do a for loop im going to use rec to loop thru every two unit to count
  if word[2:] == '':
    return counter
  return th_counter(word[1:],counter)
  # revusrive is done here instead of the for loop tht would of been
  # so much easier and not taken me an hour and a half to figure out :)
