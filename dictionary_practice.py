rolls = ['rock', 'paper', 'scissors']

# This is a static dictionary
d = {'Sam': 7,
     'rolls': rolls,
     'Sarah': 'None',
     'Jeff': -1,
     'done': True}



print(d['Sam'])          # outputs 7
print(d['rolls'])        # outputs ['rock', 'paper', 'scissors']
print(d.get('Sarah'))    # outputs None
print(d.get('Jeff', -1)) # outputs -1
print(d['done'])         # outputs True
