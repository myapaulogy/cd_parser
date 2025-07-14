import constructor
import parser
import json

import test

string = """
hello=83830;
hel_lo = 83831    ;
h_el_lo = 83832;
 (0, 0)  0.8
( 0, 1 ) 0
( 1, 0       ) 0.83
(1, 1) 20.8
"""

p = parser.Parser(string)
x = p.parse()
d = constructor.Constructor(x)
y = d.to_csv()

'''
for i in x['body']['coordinates']:
    print(i[2])
'''

#print(json.dumps(x))
print(y)
'''
for (string, expected) in test.tests:
    actual = p.parse(string)
    if json.dumps(actual) != json.dumps(expected):
        raise ArithmeticError(f'failed: {string}')


'''
