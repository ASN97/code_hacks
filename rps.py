{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;\f1\fnil\fcharset0 Menlo-Bold;}
{\colortbl;\red255\green255\blue255;\red238\green252\blue122;\red30\green31\blue41;\red246\green246\blue239;
\red174\green122\blue247;\red252\green93\blue186;}
{\*\expandedcolortbl;;\cssrgb\c94510\c98039\c54902;\cssrgb\c15686\c16471\c21176;\cssrgb\c97255\c97255\c94902;
\cssrgb\c74118\c57647\c97647;\cssrgb\c100000\c47451\c77647;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
""" Mad Libs Generator\cf4 \cb1 \
\cf2 \cb3 ----------------------------------------\cf4 \cb1 \
\cf2 \cb3 """\cf4 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 //Loop back to this point once code finishes\cb1 \
\cb3 loop = \cf5 1\cf4 \cb1 \
\pard\pardeftab720\partightenfactor0

\f1\b \cf6 \cb3 while
\f0\b0 \cf4  (loop < \cf5 10\cf4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 // All the questions that the program asks the user\cb1 \
\cb3  \'a0\'a0\'a0noun = input(\cf2 "Choose a noun: "\cf4 )\cb1 \
\cb3 \'a0\'a0\'a0\'a0p_noun = input(\cf2 "Choose a plural noun: "\cf4 )\cb1 \
\cb3  \'a0\'a0\'a0noun2 = input(\cf2 "Choose a noun: "\cf4 )\cb1 \
\cb3  \'a0\'a0\'a0place = input(\cf2 "Name a place: "\cf4 )\cf2 \cb3 """ Rock Paper Scissors\cf4 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 ----------------------------------------\cf4 \cb1 \
\cf2 \cb3 """\cf4 \cb1 \
\pard\pardeftab720\partightenfactor0

\f1\b \cf6 \cb3 import
\f0\b0 \cf4  random\cb1 \
\cb3 import os\cb1 \
\cb3 import re\cb1 \
\cb3 os.system(\cf2 'cls'\cf4  
\f1\b \cf6 if
\f0\b0 \cf4  os.name==\cf2 'nt'\cf4  
\f1\b \cf6 else
\f0\b0 \cf4  \cf2 'clear'\cf4 )\cb1 \

\f1\b \cf6 \cb3 while
\f0\b0 \cf4  (\cf5 1\cf4  < \cf5 2\cf4 ):\cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  \cf2 "\\n"\cf4 \cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  \cf2 "Rock, Paper, Scissors - Shoot!"\cf4 \cb1 \
\cb3  \'a0\'a0\'a0userChoice = raw_input(\cf2 "Choose your weapon [R]ock], [P]aper, or [S]cissors: "\cf4 )\cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 if
\f0\b0 \cf4  
\f1\b \cf6 not
\f0\b0 \cf4  re.match(\cf2 "[SsRrPp]"\cf4 , userChoice):\cb1 \
\cb3  \'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  \cf2 "Please choose a letter:"\cf4 \cb1 \
\cb3  \'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  \cf2 "[R]ock, [S]cissors or [P]aper."\cf4 \cb1 \
\cb3  \'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f1\b \cf6 continue
\f0\b0 \cf4 \cb1 \
\cb3  \'a0\'a0\'a0// Echo the use\cf2 r's choice\cf4 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3  \'a0\'a0\'a0print "You chose: " + userChoice\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0choices = ['\cf4 R\cf2 ', '\cf4 P\cf2 ', '\cf4 S\cf2 ']\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0opponenetChoice = random.choice(choices)\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0print "I chose: " + opponenetChoice\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0if opponenetChoice == str.upper(userChoice):\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0\'a0\'a0\'a0\'a0print "Tie! "\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0#if opponenetChoice == str("R") and str.upper(userChoice) == "P"\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0elif opponenetChoice == '\cf4 R\cf2 ' and userChoice.upper() == '\cf4 S\cf2 ':\'a0\'a0\'a0\'a0\'a0\'a0\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0\'a0\'a0\'a0\'a0print "Scissors beats rock, I win! "\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0\'a0\'a0\'a0\'a0continue\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0elif opponenetChoice == '\cf4 S\cf2 ' and userChoice.upper() == '\cf4 P\cf2 ':\'a0\'a0\'a0\'a0\'a0\'a0\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0\'a0\'a0\'a0\'a0print "Scissors beats paper! I win! "\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0\'a0\'a0\'a0\'a0continue\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0elif opponenetChoice == '\cf4 P\cf2 ' and userChoice.upper() == '\cf4 R\cf2 ':\'a0\'a0\'a0\'a0\'a0\'a0\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0\'a0\'a0\'a0\'a0print "Paper beat rock, I win! "\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0\'a0\'a0\'a0\'a0continue\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0else:\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf4 \cb1 \
\cf2 \cb3  \'a0\'a0\'a0\'a0\'a0\'a0\'a0print "You win!"\cf4 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3  \'a0\'a0\'a0adjective = input(\cf2 "Choose an adjective (Describing word): "\cf4 )\cb1 \
\cb3  \'a0\'a0\'a0noun3 = input(\cf2 "Choose a noun: "\cf4 )\cb1 \
\cb3 // Displays the story based on the users input\cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  (\cf2 "------------------------------------------"\cf4 )\cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  (\cf2 "Be kind to your"\cf4 ,noun,\cf2 "- footed"\cf4 , p_noun)\cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  (\cf2 "For a duck may be somebody's"\cf4 , noun2,\cf2 ","\cf4 )\cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  (\cf2 "Be kind to your"\cf4 ,p_noun,\cf2 "in"\cf4 ,place)\cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  (\cf2 "Where the weather is always"\cf4 ,adjective,\cf2 "."\cf4 )\cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  ()\cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  (\cf2 "You may think that is this the"\cf4 ,noun3,\cf2 ","\cf4 )\cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  (\cf2 "Well it is."\cf4 )\cb1 \
\cb3  \'a0\'a0\'a0
\f1\b \cf6 print
\f0\b0 \cf4  (\cf2 "------------------------------------------"\cf4 )\cb1 \
\cb3 // Loop back to \cf2 "loop = 1"\cf4 \cb1 \
\cb3 \'a0\'a0\'a0\'a0loop = loop + \cf5 1}