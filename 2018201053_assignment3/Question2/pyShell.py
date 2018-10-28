#!/usr/bin/env python
from __future__ import print_function
from os import listdir
from os.path import isfile, join
import re
import os

while True:
	x=raw_input(">>>")
	if x=="ls":
		for f in listdir("."):
			print(f, end=' ')
		print()  #done

	if re.match("cd *",x): 
		x=x[3:]
		try:
			os.chdir(x)
			for f in listdir("."):
				print(f, end=' ')
			print() 
		except:
			print("No such directory exists!")  #done

	if x=="pwd":
		print(os.getcwd()) #done

	if re.match("touch *",x): 
		x=x[6:]
		files=x.split() #if more than one file is put in touch
		for f in files:
			f=open(f,'a')
			f.close()   #done
		
	if re.match("head *",x):
		x=x[5:]

		if x[0]=="-":
			y=x[1]
			z=x[3:]
			try:
				isfile(z)
				f=open(z)
				for i in range(int(y)):
					line=f.next()
					line.strip()
					print(line, end='')
				f.close()
			except:
				print("give valid file name!")
		else:
			try:
				isfile(x)
				size=0
				f=open(x)
				for i in f: #calculate size of file
					size=size+1
				f.close()
				if size>=10:
					f=open(x)
					for i in range(10):
						line=f.next()
						line.strip()
						print(line, end='')
					f.close()
				else:
					f=open(x)
					for i in range(size):
						line=f.next()
						line.strip()
						print(line, end='')
					f.close()
			except:
				print("give valid file name!")  #done
			

	if re.match("tail *",x):
		x=x[5:]
		if x[0]=="-":
			y=x[1] #tail -2 then y=2
			z=x[3:]
			try:
				isfile(z)
				size=0
				f=open(z)
				for i in f: #calculate size of file
					size=size+1
				f.close()
				y=size-int(y)
				l=[]
				for i in range(int(y),size+1,1): #froming list of line no.s to be printed
					l.append(i)
				f=open(z)
				i=0
				for line in f:
					if i in l:
						print(line, end='')
						i+=1
					else:
						i+=1
				f.close()
				print()
			except:
				print("This file does not exist!")
		else:
			try:
				isfile(x)
				size=0
				f=open(x)
				for i in f: #calculate size of file
					size=size+1
				f.close()
				if size>=10:
					y=size-10
					l=[]
					for i in range(int(y),size+1,1): #froming list of line no.s to be printed
						l.append(i)
					f=open(x)
					i=0
					for line in f:
						if i in l:
							print(line, end='')
							i+=1
						else:
							i+=1
					f.close()
					print()
				else:
					f=open(x)
					for i in range(size):
						line=f.next()
						line.strip()
						print(line, end='')
					f.close()
			except:
				print("This file does not exist!")  #done
			
	if re.match("tr *",x): #unimplemented do it later
		x=x[3:]
		string=x.split()

	if re.match("grep *",x):
		x=x[5:]
		st=x.split(" ",1)
		s=st[0].strip('\'')
		# print(s)
		string=[s,st[1]]
		# print(string)
		try:
			isfile(string[1])
			f=open(string[1])
			for line in f:
				if re.search(string[0],line):
					print(line, end="")
				else:
					pass
			f.close()
		except:
			print(string[0])
			print(string[1])
			print("Enter valid file name")

