#Q3
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")

#Q4
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")

if(len(original) > 0):
  print original
else:
  print 'empty'

#Q5
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")

if(len(original) > 0 and original.isalpha()):
  print original
else:
  print 'empty'


#Q6
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print original
  word = original.lower()
  first = word[0]
else:
  print 'empty'


#Q9
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print original
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
else:
  print 'empty'


#Q10
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print original
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
  print 'empty'


#Q11
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  #print original
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
  print 'empty'