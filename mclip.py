#! python3
# mclip.py - A multi-clipboard program.

#Dictionary of keyphrase-message pairs
TEXT = {'longtime': """Hey ! What's up? It's been a long time !""",
        'copypasta': """Hey guys. This is my very first copy pasta and I am really nervous about pasting it because if it does not get copy pasta then I will have much embarrassment. I've have thinking about it for a couple of nights now, but here it is!.""",
        'rickroll': """https://www.youtube.com/watch?v=dQw4w9WgXcQ""",
        'eaglegif': """https://media.giphy.com/media/11p1apCPqM7WEw/giphy.gif?cid=ecf05e47ovsq88vo8d5cvp7cw0p6xlf4j4vk16m3ngeqssxn&rid=giphy.gif&ct=g""",
        }


import sys, pyperclip

#Check if a keyphrase has been passed
if len(sys.argv) < 2:
        print('Error : Please enter a keyphrase. \n Usage: mclip [keyphrase] - copy text associated with the keyphrase.')
        sys.exit()

#First command line argument is the key phrase, 'keyphrase' variable used for readability        
keyphrase = sys.argv[1] 

#Check if the keyphrase exists in the Dictionary
if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print('"' + str(TEXT[keyphrase]) + '" has been copied to clipboard.')
#Error message if keyphrase doesn't exist in hte Dictionary
else:
        print('Error : There is no text associated to the "' + keyphrase + '" keyphrase.')
        sys.exit()
