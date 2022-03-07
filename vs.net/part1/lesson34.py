my_dict = {'bumfuzzle': 'confuse; perplex; fluster',
'cattywampus':'askew, awry, kitty-corner',
'taradiddle':'a fib or pretentious nonsense',
'billingsgate':'coarsely abusive language',
'snickersnee':'a large knife',
'widdershins':'in a left-handed or contrary direction; counterclockwise',
'collywobbles':'pain in the abdomen and expecially in the stomach; a bellyache',
'dipthong':'two vowel sounds joined in one syllable to form one speech sound, e.g. the sounds of \"ou\" in out and of \"oy\" in boy'}

print(my_dict.keys())

word = input('\nWhich of the words above would you like to know the definition of?')
if word in my_dict.keys():
    print(my_dict[word])
else:
    print('That didn\'t match any of the words in the dictionary.')