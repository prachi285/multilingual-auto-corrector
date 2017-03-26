import auto_correct as auto
import sys
import StringIO

# queries to train the model
queries = ['how to handle a 1.5 year old when hitting',
 'how can i avoid getting sick in china',
 'how do male penguins survive without eating for four months',
 'how do i remove candle wax from a polar fleece',
 'how do i find an out of print book',
 'yeh query hai',
 'Aap Kaise Hain',
'I am Fine Main theek Hoon',
'We’ll meet again',
 'See you latter Phir Milenge',
'What’s your name? Aap ka naam kya hai',
'My Name is <name> Mera Naam <name> Hai',
'I am Going Main Ja Raha Hoon, Main Ja Rahi Hoon',
'Where are you going? Aap kahan ja rahe ho?',
'Where are we going? Hum kahan ja rahe hain?',
'How is your family? Aapka parivaar kaisa hai?''
'Nice to meet you Aapse mil kar khushi hu']

# train the model

# supressing the output of training model
stdout = sys.stdout
sys.stdout = StringIO.StringIO()

model = auto.auto_correct(re_train=True,data=queries)

# enabling the output standard output
sys.stdout = stdout

# running the model
model.run()
