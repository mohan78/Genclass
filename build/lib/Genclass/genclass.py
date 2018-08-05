class Class_generator:

	def __init__(self,filename):
		filename = filename+'.py'
		self.filename = filename

	def GenerateClass(self,title,fields,str_method='No',str_names=None,in_fields=None):
		content = self.ReadCode()
		code = self.ClassConstruct(title,fields,str_method,str_names,in_fields)
		code = content + '\n' + code
		f = open(self.filename,'w')
		f.write(code)
		f.close()

	def ReadCode(self):
		try:
			f = open(self.filename,'r')
			content = f.read()
			return content
			f.close()
		except FileNotFoundError:
			f = open(self.filename,'w')
			f.write('')
			content = f.read()
			return content
			f.close()

	def ClassConstruct(self,title,fields,str_method,str_names,in_fields):
		header = """
class {}:
		""".format(title)
		arguments = ""
		for i in fields:
			arguments = arguments + ',' + i
		if in_fields is not None:
			init = '\t'+'def __init__(self'+in_fields+arguments+'):'
		else:
			init = '\t'+'def __init__(self'+arguments+'):'
		body = ""
		for i in fields:
			statement = '\t'*2+"self."+i+'='+i
			body = body + '\n' + statement
		if str_method == 'No':
			return(header+'\n'+init+'\n'+body)
		else:
			string1 = header+'\n'+init+'\n'+body+'\n'*2
			string2 = '\t'+'def __str__(self):'+'\n'
			name = 'self.'+str_names[0]
			if len(str_names) > 1:
				for i in range(1,len(str_names)):
					temp = '" "+'+'self.'+ str_names[i] 
					name = name+'+'+temp
			string3 = '\t'*2+'return '+ name
			string = string1 + string2 + string3
			return string

	def InheritClass(self,parent,child,fields,str_method='No',str_names=None):
		args = self.tell_params(parent)
		body = self.ClassConstruct(child,fields,str_method,str_names,','+args)
		parent_def = '\t'*2 + parent.__name__+'.__init__(self,'+args+')'
		code = body + '\n' + parent_def
		content = self.ReadCode()
		code = content + '\n' + code
		f = open(self.filename,'w')
		f.write(code)
		f.close()

	def tell_params(self,parent):
		import inspect
		parent_args = inspect.getargspec(parent.__init__)
		args = parent_args[0][1]
		for i in range(2,len(parent_args[0])):
			text = parent_args[0][i]
			args = args + ',' + text
		return args

