#from _typeshed import NoneType
from sly import Lexer
from sly import Parser
import urllib.request
import requests
import sys
import time
import os
import platform
import threading
import subprocess
import traceback
from http.server import HTTPServer, CGIHTTPRequestHandler
from playsound import playsound
import linecache
import re
from tkinter import *
from tkinter import messagebox
import operator

top = None
#top = Tk()
#top.geometry("100x100")

#soundcommand = ""

customvariables = {}
finalvalue = 0


def play_sound(flnm):
	#t = threading.thread(tagret=none)
	#t.daemon = True
	#t.start()
	playsound(flnm)
	#0+0


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'





class BasicLexer(Lexer):
	tokens = { NAME, NUMBER, STRING, PRINT}
	ignore = '\t '
	literals = { '=', '+', '-', '/',
				'*', '(', ')', ',', ';', '#', 'IN'}


	# Define tokens as regular expressions
	# (stored as raw strings)
	NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
	STRING = r'\".*?\"'
	#PRINT = ("(" + input("?:") + ")")
	#print(PRINT)

	# Number token
	@_(r'\d+')
	def NUMBER(self, t):
		
		# convert it into a python integer
		t.value = int(t.value)
		return t

	# Comment token
	@_(r'##.*')
	def COMMENT(self, t):
		pass

	# Newline token(used only for showing
	# errors in new line)
	@_(r'\n+')
	def newline(self, t):
		self.lineno = t.value.count('\n')







class BasicParser(Parser):
	#tokens are passed from lexer to parser
	tokens = BasicLexer.tokens

	precedence = (
		('left', '+', '-'),
		('left', '*', '/'),
		('right', 'UMINUS'),
	)

	def __init__(self):
		self.env = { }

	@_('')
	def statement(self, p):
		pass

		

	
		
	@_('PRINT "("')
	def expr(self, p):
		return p.expr

	
	
		
	@_('var_assign')
	
	def statement(self, p):
		#deeta = p.STRING.replace('"', '')
		#deeta = deeta.replace('\n', ' ').replace('\r', '')
		return p.var_assign

	@_('NAME "=" expr')
	def var_assign(self, p):
		#deeta = str(p.expr).replace('"', '')
		#deeta = deeta.replace('\n', ' ').replace('\r', '')
		#print(deeta)
		return ('var_assign', p.NAME, p.expr)

	@_('NAME "=" STRING')
	def var_assign(self, p):
		###deeta = p.STRING.replace('"', '')
		###deeta = deeta.replace('\n', ' ').replace('\r', '')
		###print(deeta)
		if p.STRING == "\"INP()\"":
			deetalmao = input(">>")
			#print(deetalmao)
			return ('var_assign', p.NAME, deetalmao)
		else:
			#print("LALALALAL")
			return ('var_assign', p.NAME, p.STRING)

	@_('expr')
	def statement(self, p):
		#print(p.expr)
		return (p.expr)

	@_('expr "+" expr')
	def expr(self, p):
		deeta = str(p.expr0).replace('"', '')
		#deeta = deeta.replace('\n', ' ').replace('\r', '')
		#print(deeta)
		return ('add', p.expr0, p.expr1)

	@_('expr "-" expr')
	def expr(self, p):
		return ('sub', p.expr0, p.expr1)

	@_('expr "*" expr')
	def expr(self, p):
		return ('mul', p.expr0, p.expr1)

	@_('expr "/" expr')
	def expr(self, p):
		return ('div', p.expr0, p.expr1)

	@_('"-" expr %prec UMINUS')
	def expr(self, p):
		return p.expr

	@_('NAME')
	def expr(self, p):

		deeta = p.NAME.replace('"', '')
		deeta = deeta.replace('\n', ' ').replace('\r', '')
		#print(deeta)
		#print(vardeeta)
		#direturn 0
		return ('var', p.NAME)
		#stop()

	@_('NUMBER')
	def expr(self, p):
		return ('num', p.NUMBER)





vardeeta = ""


def stop():
    a = "b"

class BasicExecute:
	
	def __init__(self, tree, env):
		self.env = env
		result = self.walkTree(tree)
		if result is not None and isinstance(result, int):
			print(result)
		if isinstance(result, str) and result[0] == '"':
			print(result)

	def walkTree(self, node):

		if isinstance(node, int):
			return node
		if isinstance(node, str):
			
			#print(str(node).replace('"', ''))
			return node

		if node is None:
			return None

		if node[0] == 'program':
			if node[1] == None:
				self.walkTree(node[2])
				
			else:
				
				self.walkTree(node[1])
				self.walkTree(node[2])

		if node[0] == 'num':
			return node[1]

		if node[0] == 'str':
			#print(node[0])
			return node[1]

		if node[0] == 'add':
			return self.walkTree(node[1]) + self.walkTree(node[2])
		elif node[0] == 'sub':
			return self.walkTree(node[1]) - self.walkTree(node[2])
		elif node[0] == 'mul':
			return self.walkTree(node[1]) * self.walkTree(node[2])
		elif node[0] == 'div':
			return self.walkTree(node[1]) / self.walkTree(node[2])

		if node[0] == 'var_assign':
			#print(node)
			self.env[node[1]] = self.walkTree(node[2])
			return node[1]

		if node[0] == 'var':
			try:
				
				vardeeta = (str(self.env[node[1]]).replace('"', ''))
				#print(vardeeta)
				return self.env[node[1]]
			except LookupError:
				print(bcolors.FAIL + "Undefined variable '"+node[1]+"'" + bcolors.ENDC + '\n')
				sys.exit(1)
				return None











if __name__ == '__main__':
	skipline = False
	doLexing = True
	doneFirstParse = False
	Debug = False
	lexer = BasicLexer()
	parser = BasicParser()
	env = {}
	
	if True:
		doLexing = True	
		try:
			try:
				command = sys.argv[1]
			except:
				print("AUSL Programming Language help")
				print("Usage:")
				print(" ./AUSL.bin [program name]")
				#sys.exit(0)
				command = "myprogram.ausl"
				#pass
			file1 = open(command, 'r')
			Lines = file1.readlines()
			#	sys.exit(0)
 
			count = 0
			count2 = 0

			for line in Lines:
				count += 1

				
			# Strips the newline character
			for line in Lines:
				
				text = line.strip()

				

				if doneFirstParse == False:
							count2 += 1;
							file1 = open(command, 'r')
							Lines = file1.readlines()
							doLexing = False
							if text == "end":
										0+0



							if "File.Create(" in text and not "##" in text:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										0+0
										#output = os.system ((text.split("os.do(",1)[1])[:-1])
										#print(output)
									except:
										print("error")
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									sys.exit(1)



							if "File.Write(" in text and not "##" in text:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										0+0
										#output = os.system ((text.split("os.do(",1)[1])[:-1])
										#print(output)
									except:
										print("error")
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									sys.exit(1)

							if "File.Delete(" in text and not "##" in text:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										0+0
										#output = os.system ((text.split("os.do(",1)[1])[:-1])
										#print(output)
									except:
										print("error")
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									sys.exit(1)



							if "pause(" in text and not "##" in text:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										0+0
										#output = os.system ((text.split("os.do(",1)[1])[:-1])
										#print(output)
									except:
										print("error")
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									sys.exit(1)






							
							if "Sound.Play(" in text and not "##" in text:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										0+0
										#output = os.system ((text.split("os.do(",1)[1])[:-1])
										#print(output)
									except:
										print("error")
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									sys.exit(1)




							if "Sound.Play(" in text and not "##" in text:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										0+0
										#output = os.system ((text.split("os.do(",1)[1])[:-1])
										#print(output)
									except:
										print("error")
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									sys.exit(1)




										#sys.exit(0)




							if text == "httpserver.startServer()":
								0+0
								#doLexing = False
								# Make sure the server is created at current directory
								#os.chdir('.')
								# Create server object listening the port 80
								#server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
								# Start the web server
								#server_object.serve_forever()
							
							if "print(" in text and not "##" in text:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										0+0
										#output = os.system ((text.split("os.do(",1)[1])[:-1])
										#print(output)
									except:
										print("error")
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									sys.exit(1)




							
								#print("lol")
								#doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									0+0
									#print ((text.split("print(",1)[1])[:-1])
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									sys.exit(1)

							if "os.do(" in text and not "##" in text:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										0+0
										#output = os.system ((text.split("os.do(",1)[1])[:-1])
										#print(output)
									except:
										print("error")
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									sys.exit(1)


							if "=" in text and not "##" in text:
								#print("lol")
								doLexing = False
								#length = len(text)
								#Get last character of string i.e. char at index position len -1
								#last_char = text[length -1]
								

							



							
							if "download(" in text and not "##" in text:
								#print("lol")
								#doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									
									0+0
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									sys.exit(1)




							if "inp(" in text and not "##" in text:
								
								doLexing = False
								
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":

									0+0
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction!" + bcolors.ENDC)
									sys.exit(1)



							

							if text and doLexing == True:
									if text != "beanslmao" or text != "exit":
																try:
																															tree = parser.parse(lexer.tokenize(text))
																															BasicExecute(tree, env)
																except Exception as ex:
																	
																			template = "\nAn exception of type {0} occurred. Arguments:\n{1!r}\n"
																			message = template.format(type(ex).__name__, ex.args)
																			print (bcolors.FAIL + message + bcolors.ENDC)



							if count2 >= count:
								doLexing = True
								doneFirstParse = True

				


				
					
				if True:

					file1 = open(command, 'r')
					Lines = file1.readlines()
					linenumber = 0
					isinWhile = None

					for line in Lines:

						"""if( "while(" in line.strip()):
									print("in while")
									isinWhile = True

						if(isinWhile and not skipline):
							#print(line.strip())
							if("};" in line.split()):
								print("Not in while")
								isinWhile = False
						else:
							0+0	

						"""


						if(isinWhile):
							#skipline = True
							if(text == "};"):
								#print("no while loop anymore")
								isinWhile = False
							else:
								#doLexing = False
								0+0
						

						if skipline == True:
							skipline = False
							#print("Stop")
							continue
						
						if doneFirstParse == True:
							text = line.strip()
							
							file1 = open(command, 'r')
							Lines = file1.readlines()
							doLexing = True
							linenumber += 1
							if text == "end":
										sys.exit(0)







							if "if(" in text and not "##" in text and not isinWhile:
								doLexing = False
								length = len(text)
								last_char = text[length -1]
								ifstatement = ((text.split("if(",1)[1])[:-1])
								if last_char == ")":									
									data = (((text.split("if(",1)[1])[:-1]))
									data2 = data.split("==")									
									data2 = str(data2[0]).replace(" ", "")
									data3 = data.split("==")									
									data3 = str(data3[1]).replace(" ", "")
									datavar2 = ""
									
									
									if (data2 + " ") in customvariables:
										0+0
										if customvariables[(data2 + " ")] == data3:
											0+0

										else:
											skipline = True
											
										
									else:
										0+0
										
									
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)




							if ":{" in text and not "##" in text:
								doLexing = False

							
							if "};" in text and not "##" in text:
								doLexing = False



							if "while(" in text and not "##" in text:
								isinWhile = True
								#print("While")
								doLexing = False
								
								length = len(text)
								last_char = text[length -1]
								ifstatement = ((text.split("while(",1)[1])[:-1])
								if last_char == ")":									
									data = (((text.split("while(",1)[1])[:-1]))
									data2 = None
									operator = ""
									if("<=" in data):
										data2 = data.split("<=")									
										data2 = str(data2[0]).replace(" ", "")
										data3 = data.split("<=")									
										data3 = str(data3[1]).replace(" ", "")
										operator = "<="

									if(">=" in data):
										data2 = data.split(">=")									
										data2 = str(data2[0]).replace(" ", "")
										data3 = data.split(">=")									
										data3 = str(data3[1]).replace(" ", "")
										operator = ">="

									if("==" in data):
										data2 = data.split("==")									
										data2 = str(data2[0]).replace(" ", "")
										data3 = data.split("==")									
										data3 = str(data3[1]).replace(" ", "")
										operator = "=="

									if("!=" in data):
										data2 = data.split("!=")									
										data2 = str(data2[0]).replace(" ", "")
										data3 = data.split("!=")									
										data3 = str(data3[1]).replace(" ", "")
										operator = "!="



									datavar2 = ""
									

									data = """"""
									result = """"""
									res2 = """"""
									res = """"""
											#data += ""
									with open(command) as myFile:
										#data = myFile.read()
										#print("LoL")
										for li in iter(lambda: myFile.readline().rstrip(), '};'):
        										
												res += (li.lstrip(":{") + "!@")

												#print(li)
												#print(result)
										#result = data.split("};")  # use your \-1 (whatever that means) here
										res2 = str(str((res).split(":{")).replace("!@", "\n")).replace("']","")
										#print(str(str(res).split("while(")[1]).replace(")","",1))
										con2 = 0
										if(con2 == 0):
											con2 += 1
											result = str(str(res2).split("while(")[1]).replace(")", "~", 1).split("~")[1]
									#print(str(result))
									#data2 = result
									#continue

									
									if(operator == "<="):
											#print(str(customvariables[(data2 + " ")]).replace(" ",""))
											while str(customvariables[(data2 + " ")]).replace(" ","") <= data3:
												#time.sleep(1)
												if(True):

													#print(customvariables)
											#print("LoL")
									#		0+0
											#print(result)
													#time.sleep(1)
													for lns in str(result).splitlines():


														if ("+=") in lns and not "##" in lns:
															#print("+=")
															vardata = (((lns.split("=",1)[1])))
															#vardata = ((vardata.replace("+",",")))
															vardata2 = vardata.split(",")
															vardata2 = vardata.replace(" ","")
															varname = lns.split("+=", 1)
															subvarname = varname[0]
															deeta = int(customvariables[varname[0]])
															deeta += (int(vardata2))
															if deeta > int(customvariables[(data2 + " ")]) - 2:
																customvariables[varname[0]] = deeta - 0
																continue
															else:
																customvariables[varname[0]] = deeta
															#print(deeta)
															#print(deeta)



														try:
															#print("running...")
															exec(str(lns))
														except:
															0+0
										
									
									#continue
									if(operator == ">="):
										while (str(customvariables[(data2 + " ")]).replace(" ","")) >= data3:
											if(True):

													#print(customvariables)
											#print("LoL")
									#		0+0
											#print(result)
													#time.sleep(1)
													for lns in str(result).splitlines():


														if ("+=") in lns and not "##" in lns:
															#print("+=")
															vardata = (((lns.split("=",1)[1])))
															#vardata = ((vardata.replace("+",",")))
															vardata2 = vardata.split(",")
															vardata2 = vardata.replace(" ","")
															varname = lns.split("+=", 1)
															subvarname = varname[0]
															deeta = int(customvariables[varname[0]])
															deeta += (int(vardata2))
															if deeta > int(customvariables[(data2 + " ")]) - 2:
																customvariables[varname[0]] = deeta - 0
																continue
															else:
																customvariables[varname[0]] = deeta
															#print(deeta)
															#print(deeta)



														try:
															#print("running...")
															exec(str(lns))
														except:
															0+0
										
									#print(data2)
									if(operator == "=="):
										while str(customvariables[(data2 + " ")]).replace(" ","") == data3:
											if(True):

													#print(customvariables)
											#print("LoL")
									#		0+0
											#print(result)
													#time.sleep(1)
													for lns in str(result).splitlines():


														if ("+=") in lns and not "##" in lns:
															#print("+=")
															vardata = (((lns.split("=",1)[1])))
															#vardata = ((vardata.replace("+",",")))
															vardata2 = vardata.split(",")
															vardata2 = vardata.replace(" ","")
															varname = lns.split("+=", 1)
															subvarname = varname[0]
															deeta = int(customvariables[varname[0]])
															deeta += (int(vardata2))
															if deeta > int(customvariables[(data2 + " ")]) - 2:
																customvariables[varname[0]] = deeta - 0
																continue
															else:
																customvariables[varname[0]] = deeta
															#print(deeta)
															#print(deeta)



														try:
															#print("running...")
															exec(str(lns))
														except:
															0+0
										
									if (data2 + " ") in customvariables:
										#print(data2)
										#print(data3, customvariables[(data2 + " ")])
										#while customvariables[(data2 + " ")] == data3:
											#print("LoL")
										#	0+0
										0+0
										#print("lmao")	
										
									else:
										0+0
										
									
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)





							if "goto(" in text and not "##" in text and not isinWhile:
								doLexing = False
								length = len(text)
								last_char = text[length -1]
								lookup = ((text.split("goto(",1)[1])[:-1])
								#print(lookup)
								linenumber = 0
								if last_char == ")":
									with open(command) as file2:
										for num, linegoto in enumerate(file2):
											if lookup in linegoto:
												linenumber = num
									#print((text.split("goto(",1)[1])[:-1])
									goto_line = linecache.getline(command, linenumber + 1)
									print(goto_line)
									print(linenumber)
									
									#file1.seek((text.split("goto(",1)[1])[:-1])
									
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)



							
							if text == "httpserver.startServer()" and not isinWhile:
								try:
									doLexing = False
									# Make sure the server is created at current directory
									os.chdir('.')
									# Create server object listening the port 80
									server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
									# Start the web server
									server_object.serve_forever()
								except Exception as ex:
																	
									template = ("\nAn exception of type '{0}' occurred at line " + str(linenumber) + ": '" + text + "'. Arguments:\n{1!r}\n")
									message = template.format(type(ex).__name__, ex.args)
									print (bcolors.FAIL + message + bcolors.ENDC)
							if text == "debug" and not isinWhile:
								doLexing = False
								print("DEBUG mode lol")
								
							if "print(\"" in text and not "##" in text and not isinWhile:
								
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									data = (((text.split("print(\"",1)[1])[:-1]))
									datavar = data.split('"')[1::2]
									datavar2 = ""
									for i in datavar:
										datavar2 = i
										datavar2 = datavar2.replace(" ","")
									datavar2 = datavar2.replace("%","")
									
									if (datavar2 + " ") in customvariables:
										data = (((text.split("print(\"",1)[1])[:-1]))
										
										data = data.replace("\"", "")
										data = str(data).replace("%","")
										data = str(data).replace(datavar2,"")
										data = data + (customvariables[(datavar2 + " ")])
										print(data)
									else:
										data = (((text.split("print(\"",1)[1])[:-1]))
										data = data.replace("\"","")
										
										print(data)
									
								else:
								 	print(bcolors.FAIL + "Missing Parentheses or Quote at end of instruction: '" + text + "'" + bcolors.ENDC)

							if "pause(" in text and not "##" in text and not isinWhile:
								doLexing = False
								length = len(text)
								last_char = text[length -1]
								if last_char == ")":
									
									time.sleep(int((text.split("pause(",1)[1])[:-1]))
									
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)

							if "button(" in text and not "##" in text and not isinWhile:
								#print("lol")
								doLexing = False
								txt = text
								length = len(text)
								last_char = text[length -1]
								if last_char == ")":
									pattern = "button(\(.*?)\,"


									substring = re.search(pattern, txt).group(1)
									sub2 = substring.replace("(","")

									pt2 = "(\(.*?)\,"
									txt = text
									substring2 = ",".join(txt.split(",", 2)[:-1])
									
									sub3 = substring2.replace("(","")
									sub3 = sub3.rsplit(",")[1]
									#sub3 =
									#print(sub3)

									top = Tk()
									#print("tkinter lol")
									def helloCallBack():
										print("Hello World")
									#print((((txt.split(",",1)[1])[:-1]).rsplit(","))[1])
									B = Button(top, text = ((((txt.split(",",1)[1])[:-1]).rsplit(","))[1].replace(" ","", 1)), command = helloCallBack)
									txt = text
									x = ((txt.split("button(",1)[1])[:-1])
									y = ((txt.split(",",1)[1])[:-1])
									B.place(x = int(sub2),y = int(sub3))

									#B.pack()
									top.mainloop()
									#time.sleep()
									
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)



							if "File.Delete(" in text and not "##" in text and not isinWhile:
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									
									os.remove((text.split("File.Delete(",1)[1])[:-1])
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)





							if "File.Create(" in text and not "##" in text and not isinWhile:
								
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										open((text.split("File.Create(",1)[1])[:-1], 'w').write("")
									except Exception as ex:
										print("Error: ", ex)
									
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)



							

							if "File.Write(" in text and not "##" in text and not isinWhile:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										start = text. find(",") + len(",")
										end = text.find(")")
										substring = text[start:end]
										#print(substring.split())
										filenm = text.split("File.Write(",1)[1][:-1]
										filenm = filenm.split(",")[0]
										#print(urladdr)
										#r = requests.get(urladdr, allow_redirects=True)
										open(filenm, 'w').write(substring)
										#print ((text.split("download(",1)[1])[:-1])
										#text = ""
									except Exception as ex:
																	
										template = ("\nAn exception of type '{0}' occurred at line " + str(linenumber) + ": '" + text + "'. Arguments:\n{1!r}\n")
										message = template.format(type(ex).__name__, ex.args)
										print (bcolors.FAIL + message + bcolors.ENDC)
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)




							if "os.do(" in text and not "##" in text and not isinWhile:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										output = os.system ((text.split("os.do(",1)[1])[:-1])
										#print((text.split("os.do(",1)[1])[:-1])
									except Exception as ex:
																	
										template = ("\nAn exception of type '{0}' occurred at line " + str(linenumber) + ": '" + text + "'. Arguments:\n{1!r}\n")
										message = template.format(type(ex).__name__, ex.args)
										print (bcolors.FAIL + message + bcolors.ENDC)
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)


							if "=" in text and not "##" in text and not isinWhile:
								
								doLexing = False
								
								varname = text.split("=", 1)
								subvarname = varname[0]
								

								vardata = (((text.split("=",1)[1])))

								if "\"" in vardata:
									customvariables[subvarname] = vardata.replace("\"","")

								else:
									customvariables[subvarname] = vardata


								result = ''
								
								
								if "+" in vardata:
									vardata = (((text.split("=",1)[1])))
									vardata = ((vardata.replace("+",",")))
									vardata2 = vardata.split(",")
									vardata2 = vardata.replace(" ","")
									
									counter = 0
									length = len(customvariables)
									
									
									for x in range(length):
										
										if True:
											if True:  
												0+0
												
												if "," in vardata2:
													
													vardata2 = vardata2.split(',')
													length2 = len(vardata2)
													
													for i in vardata2:
														
														if(not (customvariables.get(i + ' ')) == None):
															vals = customvariables.get(i + ' ').replace(" ", "")

														
														if "\"" in vals:
															vals = vals.replace("\"", "")
															result = result+vals
															customvariables[varname[0]] = result
														else:
															
															nums = []
															#vals = vals.replace("\"", "")
															#for word in result:
															#	if word.isdigit():
															#		nums.append(int(word))
															#		print(word)


															for word in vals:
																if word.isdigit():
																	#nums.append(int(word))
																	finalvalue += int(word)
																	#print(word)

															#print(finalvalue)
															
															customvariables[varname[0]] = finalvalue  
														
														
													
												counter += 1
											

								else:
									vardata = ((text.split("=",1)[1]))
									customvariables[varname[0]] = vardata
								if (str(vardata) + " ") in customvariables:
									0+0
									
							if (text + " ") in customvariables and not isinWhile:
								0+0
								doLexing = False
								print(customvariables[(text + " ")])
								

							if "Sound.Play(" in text and not "##" in text and not isinWhile:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										0+0
										#output = os.system ((text.split("os.do(",1)[1])[:-1])
										t = threading.Thread(target=play_sound((text.split("Sound.Play(",1)[1])[:-1]))
										t.daemon = True
										t.start()
										#playsound((text.split("Sound.Play(",1)[1])[:-1])
										#print(output)
									except Exception as ex:
																	
										template = ("\nAn exception of type '{0}' occurred at line " + str(linenumber) + ": '" + text + "'. Arguments:\n{1!r}\n")
										message = template.format(type(ex).__name__, ex.args)
										print (bcolors.FAIL + message + bcolors.ENDC)
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									#sys.exit(1)
							if "clr" in text and not "##" in text and not isinWhile:
								#print("lol")
								doLexing = False
								if(platform.system() == "Windows"):
																	os.system("cls")
								elif(platform.system() == "Linux"):
																	os.system("clear")
								




							if "os.version" in text and not "##" in text and not isinWhile:
								#print("lol")
								doLexing = False
								try:
									print("OS Version: ", platform.system(), platform.version())
								except Exception as ex:
																	
									template = ("\nAn exception of type '{0}' occurred at line " + str(linenumber) + ": '" + text + "'. Arguments:\n{1!r}\n")
									message = template.format(type(ex).__name__, ex.args)
									print (bcolors.FAIL + message + bcolors.ENDC)
									
								#length = len(text)
								#Get last character of string i.e. char at index position len -1
								#last_char = text[length -1]
								#if last_char == ")":
								#	try:
								#		0+0
										#output = os.system ((text.split("os.do(",1)[1])[:-1])
								#		playsound((text.split("Sound.Play(",1)[1])[:-1])
										#print(output)
								#	except:
								#		print("error")
									#text = ""
								#else:
								#	print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)
									#sys.exit(1)



							

							if "download(" in text and not "##" in text and not isinWhile:
								#print("lol")
								doLexing = False
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":
									try:
										start = text. find(",") + len(",")
										end = text.find(")")
										substring = text[start:end]
										#print(substring.split())
										urladdr = text.split("download(",1)[1][:-1]
										urladdr = urladdr.split(",")[0]
										#print(urladdr)
										r = requests.get(urladdr, allow_redirects=True)
										open(substring, 'wb').write(r.content)
										#file6.close()
										#print ((text.split("download(",1)[1])[:-1])
										#text = ""
									except Exception as ex:
																	
										template = ("\nAn exception of type '{0}' occurred at line " + str(linenumber) + ": '" + text + "'. Arguments:\n{1!r}\n")
										message = template.format(type(ex).__name__, ex.args)
										print (bcolors.FAIL + message + bcolors.ENDC)
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction: '" + text + "'" + bcolors.ENDC)




							if "inp(" in text and not "##" in text and not isinWhile:
								#print("lol")
								doLexing = False
								
								length = len(text)
								#Get last character of string i.e. char at index position len -1
								last_char = text[length -1]
								if last_char == ")":

									#print("wat")
									
									try:
										varname = text.split("=", 1)
										if "inp(" in varname[0]:
											sys.exit(1)
										subvarname = varname[0]
										
									except:
										0+0
									data = input ((text.split("inp(",1)[1])[:-1])
									customvariables[varname[0]] = data
									#text = ""
								else:
									print(bcolors.FAIL + "Missing Parentheses at end of instruction!" + bcolors.ENDC)



							#print(doLexing)

							if text and doLexing == True and not isinWhile:
									if text != "DEBUG" or text != "exit":
																try:
																															tree = parser.parse(lexer.tokenize(text))
																															BasicExecute(tree, env)
																except Exception as ex:
																	
																			template = "\nAn exception of type {0} occurred. Arguments:\n{1!r}\n"
																			message = template.format(type(ex).__name__, ex.args)
																			print (bcolors.FAIL + message + bcolors.ENDC)

				

								
		except EOFError:
			print("error")
		
		
