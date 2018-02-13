#!/usr/bin/python
# -*- coding: ascii -*-

import re
import itertools
import argparse

# aka math-truth
# in the number "11384" how many ways are there to insert simple arithmetic operators
# and an equals sign and get a true equation? 
# 1=1%384 for an easy example or 1*1+3=8-4 and so on... 

#interface: 
# from=100,to=200,step=1,
# -1=all, 0=with none, 1 & 1 = with only, 4 & 10 = between 4 & 10 inclusive
# showMin=-1, showMax=-1
#

def formatCleaner(partialEquation): #because eval gets messed up on leading zeros & for float
	numberlist = re.split('[^0-9]',partialEquation)
	oplist = re.split('[0-9]+',partialEquation)
	oplist.append("")
	filteredEquation = ""
	for i, digits in enumerate(numberlist):
		if bool(re.search('0+[1-9]',digits)): #does it need to be cleaned, any zeros and #
			replace = digits.lstrip("0") #clean it
		else: 
			replace = digits #leave it
		numberlist[i] = replace+".0" #put it back fixed and float
	cleanedList = [a for b in zip(oplist,numberlist) for a in b]
	cleanedFormat = ''.join(cleanedList)
	return cleanedFormat

def testEquation(EquationString):

	leftHand = formatCleaner(EquationString.split("=")[0])
	rightHand = formatCleaner(EquationString.split("=")[1])	
	veracity = 0
	try: 
		veracity = 1 if eval(leftHand)==eval(rightHand) else 0
	except ZeroDivisionError:
		veracity = 0
	except SyntaxError:
		print "*!Sntx!Err!*" + EquationString
	returnList = [str(veracity),EquationString]
	return returnList


def searchPath(minimum=4100, maximum=4300, step=1, showMin=-1, showMax=-1): #add in base? default base 10

	if(showMax==-1): showMax=6969696969696969 #how to infinity

	for i in range(minimum,maximum,step):
		totalTruth = ['']
		thisNumbersTruths = []
		thisNumberTruthCount = 0
		digits = len(str(i))
		operators = ['+','-','/','*',''] #add exponentiation "**"?!
		#operators = ['+','-','%',''] #add exponentiation "**""
		opplaces = digits - 2 #inside and leave room for "="
		oplist = list(itertools.product(operators,repeat=opplaces)) #heavy duty
		for applyOps in oplist: #each operator combination
			for opcombo in range(opplaces): #insert '='
				newOpList = list(applyOps)				
				newOpList.insert(opcombo,'=')
				newOpList.append('') #now it's the same length as number digits
				numbersString = str(i)
				equationString = ''
				equationResult = ''
				for n, char in enumerate(numbersString): #put 'em together
					equationString += char + newOpList[n]
				equationResult = testEquation(equationString)
				#thisNumbersTruths += equationResult[0]
				if equationResult[0]=="1":
					thisNumbersTruths.append(equationString)	
					thisNumberTruthCount += 1
		#count the holes
		if((thisNumberTruthCount>=showMin)and(thisNumberTruthCount<=showMax)): 			
			print i,
			print ",",
			print thisNumberTruthCount, 
			print ","+str(thisNumbersTruths),
			print ","

def main(minimum=92500,maximum=93100,step=1,showMin=4,showMax=4):

	searchPath(minimum,maximum,step,showMin,showMax)

default = "Find and display the arithmetic versimilitude of a number. \
Using the basic operators +,-,/,* and one = inbetween the numerals, how many correct equations can be created?"

parser = argparse.ArgumentParser(description=default)

parser.add_argument("minimum", type=int, help="the starting number")
parser.add_argument("maximum", type=int, help="the ending number")
parser.add_argument("step", type=int, help="each step to take")
parser.add_argument("showMin", type=int, help="minimum number of right answers to show -1 is all")
parser.add_argument("showMax", type=int, help="maximum number of right answers to show -1 is all")

args = parser.parse_args()

main(args.minimum,args.maximum,args.step,args.showMin,args.showMax)













