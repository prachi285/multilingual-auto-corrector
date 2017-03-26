import auto_correct as auto
import sys
import StringIO

# queries to train the model
queries = ['how to handle a 1.5 year old when hitting',
 'how can i avoid getting sick in china',
 'how do male penguins survive without eating for four months',
 'how do i remove candle wax from a polar fleece',
 'how do i find an out of print book',
 'yeh query hai']

# train the model

# supressing the output of training model
stdout = sys.stdout
sys.stdout = StringIO.StringIO()

model = auto.auto_correct(re_train=True,data=queries)

# enabling the output standard output
sys.stdout = stdout

# running the model
model.run()
