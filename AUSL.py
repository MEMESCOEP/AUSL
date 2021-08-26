from sly import Lexer
from sly import Parser
import urllib.request
import requests
import sys
import time
import os
from http.server import HTTPServer, CGIHTTPRequestHandler




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
	tokens = { NAME, NUMBER, STRING, PRINT, INP }
	ignore = '\t '
	literals = { '=', '+', '-', '/',
				'*', '(', ')', ',', ';', '#'}


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

	@_('INP "("')
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
		#return 0
		return ('var', deeta)
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
				print(vardeeta)
				return self.env[node[1]]
			except LookupError:
				print("Undefined variable '"+node[1]+"'")
				return 0











if __name__ == '__main__':
	doLexing = True
	lexer = BasicLexer()
	parser = BasicParser()
	#print('GFG Language')
	env = {}
	
	if True:
		doLexing = True	
		try:
			try:
				filename = sys.argv[1]
			except:
				print("AUSL Programming Language help")
				print("Usage:")
				print(" ./AUSL.bin [program name]")
				#sys.exit(0)
				filename = "myprogram.ausl"
				#pass
			file1 = open(filename, 'r')
			Lines = file1.readlines()
 
			count = 0
			# Strips the newline character
			for line in Lines:
				
				doLexing = True
				#print(doLexing, "\n\n")
				count += 1
				#print("Line{}: {}".format(count, line.strip()))
				text = line.strip()
				#input('AUSL > ')
				if text == "end":
								sys.exit(0)




				if text == "httpserver.startServer()":
					doLexing = False
					# Make sure the server is created at current directory
					os.chdir('.')
					# Create server object listening the port 80
					server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
					# Start the web server
					server_object.serve_forever()
				if text == "beanslmao":
					print("BEANS wtfffffff")
					#break
				if "print(" in text and not "##" in text:
					#print("lol")
					doLexing = False
					length = len(text)
					#Get last character of string i.e. char at index position len -1
					last_char = text[length -1]
					if last_char == ")":
						
						print ((text.split("print(",1)[1])[:-1])
						#text = ""
					else:
						print("Missing Parentheses at end of instruction!")




				if "download(" in text and not "##" in text:
					#print("lol")
					doLexing = False
					length = len(text)
					#Get last character of string i.e. char at index position len -1
					last_char = text[length -1]
					if last_char == ")":
						start = text. find(",") + len(",")
						end = text.find(")")
						substring = text[start:end]
						#print(substring.split())
						urladdr = text.split("download(",1)[1][:-1]
						urladdr = urladdr.split(",")[0]
						#print(urladdr)
						r = requests.get(urladdr, allow_redirects=True)
						open(substring, 'wb').write(r.content)
						#print ((text.split("download(",1)[1])[:-1])
						#text = ""
					else:
						print("Missing Parentheses at end of instruction!")




				if "inp(" in text and not "##" in text:
					#print("lol")
					doLexing = False
					
					length = len(text)
					#Get last character of string i.e. char at index position len -1
					last_char = text[length -1]
					if last_char == ")":

						#print("wat")
						data = input ((text.split("inp(",1)[1])[:-1])
						def var_assign(self, p):
							return ('var_assign', "A", data)
						#text = ""
					else:
						print("Missing Parentheses at end of instruction!")



				#print(doLexing)

				if text and doLexing == True:
						if text != "beanslmao" or text != "exit":
													try:
																												tree = parser.parse(lexer.tokenize(text))
																												BasicExecute(tree, env)
													except Exception as ex:
														
																template = "\nAn exception of type {0} occurred. Arguments:\n{1!r}\n"
																message = template.format(type(ex).__name__, ex.args)
																print (bcolors.FAIL + message + bcolors.ENDC)


				

		except EOFError:
			print("error")
		
		

class httpserver():
	
		# Make sure the server is created at current directory
		os.chdir('.')
		# Create server object listening the port 80
		server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
		# Start the web server
		server_object.serve_forever()

