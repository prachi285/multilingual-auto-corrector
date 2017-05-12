import auto_correct as auto
import sys
import StringIO

# queries to train the model
queries = ['aap kaise hain', 'hum badhiya hain']

# load English data set to training model
with open('english_clean.txt') as engf:
	line = [next(engf) for x in xrange(50)]
	queries.extend(line)
engf.close()

# load Hinglish data set to training model
with open('hinglish_clean.txt') as hingf:
	line = [next(hingf) for x in xrange(50)]
	queries.extend(line)
hingf.close()

# train the model

# supressing the output of training model
stdout = sys.stdout
sys.stdout = StringIO.StringIO()

model = auto.auto_correct(re_train=True,data=queries)

# enabling the output standard output
sys.stdout = stdout

# running the model
model.run()
