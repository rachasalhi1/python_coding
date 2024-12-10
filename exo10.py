word = input("type in a word ")
i=1
is_palindrom=True
l=len(word)
if word[i] != word[l-1] :
  is_palindrom=False
  print(word[l-1])
else :
  while word[i] == word[l-1] :
    if word[i] != word[l-1] :
     is_palindrom=False
     break
    else:
     i=i+1
     l=l-1

if is_palindrom == True :
  print("yes, it's palindrom")
else: 
  print("NO, it's not palindrom")