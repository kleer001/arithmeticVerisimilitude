# arithmeticVerisimilitude
explore combinatorial arithmetic in the context of arbitrary ranges of base ten digits

It all started with the childhood urban superstition of making a wish on 11:11.

I read the ":" as an "=" and off I went. 

EXAMPLES:

18:22:48 Mon Feb 12  ~/ 

576 > python arithmeticVerisimilitude_1.py 13200 13400 7 4 4

13256 , 4 ,['1+3=2*5-6', '1*3=2-5+6', '13=2+5+6', '13-2=5+6'] ,

18:24:10 Mon Feb 12  ~/ 

577 > python arithmeticVerisimilitude_1.py 13200 13400 2 4 4

13256 , 4 ,['1+3=2*5-6', '1*3=2-5+6', '13=2+5+6', '13-2=5+6'] ,

13282 , 4 ,['1+3+2=8-2', '1=3+2-8/2', '1-3=2-8/2', '1*3*2=8-2'] ,

13296 , 4 ,['1=3/2/9*6', '1*3/2=9/6', '1*3=2*9/6', '13+2=9+6'] ,

13318 , 4 ,['1=3*3-1*8', '1=3*3/1-8', '1*3*3=1+8', '1=3*3*1-8'] ,

13342 , 4 ,['1+3/3=4-2', '1+3/3=4/2', '1*3+3=4+2', '1=3*3-4*2'] ,

13346 , 4 ,['1+3*3=4+6', '1=3-3*4/6', '13=3+4+6', '13-3=4+6'] ,



USAGE: arithmeticVerisimilitude_1.py [-h] minimum maximum step showMin showMax

Find and display the arithmetic versimilitude of a number. Using the basic
operators +,-,/,* and one = inbetween the numerals, how many correct equations
can be created?

positional arguments:
  minimum     the starting number
  maximum     the ending number
  step        each step to take
  showMin     minimum number of right answers to show -1 is all
  showMax     maximum number of right answers to show -1 is all

optional arguments:
  -h, --help  show this help message and exit
