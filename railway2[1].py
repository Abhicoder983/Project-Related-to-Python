# this section is for connection of mysql table to python
def www():
	try:
		a=input('enter your host')
		b=input('enter your password')
		c=input('enter your root')
		import mysql.connector
		yj=mysql.connector.connect(host=a,user=c,password=b)
		return yj 
	except:
		
			print('your password,username,host is worng')
			www()
			
	# calling the function www
db=www()
# defining the cursor
cur=db.cursor()







# defining the function which is used for udate the booed ticket

def update():
	def bv():
		print('a.kerala express')
		print('b.shatabdi express')
		print('c.back to menu')
		o=input('ENTER YOUR TRAIN')
		g=o.lower()
		return g
	# calling the function bv
	uc=bv()
	
	
	
	
	
	if uc=='a':
		cur.execute('select Sno from kerala')
		for i in cur:
			print(' Sno. is ',i)
		a=int(input('ENTER YOUR SNO. NUMBER AS 1/2/3/4...'))
		zc=int(input('ENTER YOUR NEW SNO.'))
		b=input('ENTER YOUR NEW NAME')
		c=int(input('ENTER YOUR NEW PHONE NO.'))
		d=input('ENTER YOUR NEW  CLASS')
		e=int(input('ENTER YOUR NO. OF PASEENGER'))
		f=input('ENTER YOUR NEW LOCATION')
		g=input('ENTER YOUR NEW DESTINATION')
		rp=60*e
		query="update kerala set Sno=%s,Name='%s',phoneno=%s,class='%s',passenger=%s,yourlocation='%s',destination='%s',Rs=%s where Sno=%s"%(zc,b,c,d,e,f,g,rp,a)
		cur.execute(query)
		db.commit()
		print('                     *********√your ticket is updated********')
		     
		     
		     
		     
		     
		     
		     
		     
		     
		     
		     
		     
		     
	elif uc=='b':
		cur.execute('select Sno from shatabdi')
		for i in cur:
			print('SNO. IS ',i)
		ap=int(input('ENTER YOUR SNO. NUMBER AS 1/2/3...'))
		zc=int(input('ENTER YOUR NEW SNO.'))
		bp=input('ENTER YOUR NEW NAME')
						
		cp=int(input('ENTER YOUR NEW PHONE NO.'))
		dp=input('ENTER YOUR NEW CLASS')
		ep=int(input('ENTER YOUR NEW NO. OF PASEENGER'))
		fp=input('ENTER YOUR NEW LOCATION')
		gp=input('ENTER YOUR NEW DESTINATION')
		rj=67*ep
		querys="update shatabdi set Sno=%s, Name='%s',phoneno=%s,class='%s',passenger=%s,yourlocation='%s',destination='%s',Rs=%s where Sno=%s"%(zc,bp,cp,dp,ep,fp,gp,rj,ap)
		cur.execute(querys)
		db.commit()
		print('        **********√your ticket is updated**********')
	elif uc=='c':
		railway()
	else:
		print('*********PLEASE ENTER CORRECT CHOICE*********')
		bv()
		
		
		
		
		
		
		
		
		
		
	
		

# defining the function for cancelling the ticket

def cancel():
	
	
	y=input('did you want to agree to cancel Y/N')
	j=y.lower()
	if j=='y':
	#   taking the data of user to cancel the ticket
	  print('a. CANCEL TICKET FOR KERALA')
	  print('b.CANCEL TICKET FOR SHATABDI')
	  print('c.back to the menu')
	  n=input('ENTER YOUR TRAIN')
	  qp=n.lower()
	#   for checking the ticket
	  if qp=='a':
	  	cur.execute('select Sno from kerala')
	  	for i in cur:
	  		print(i)
	  	f=int(input('ENTER YOUR SNO FOR DELELTE AS 1/2/3/4...'))
	  	cur.execute('delete from kerala where sno=%s'%f)
	  	db.commit()
	  	print('              ******your kerala train ticket is cancel now*******')
	  	
	  if qp=='b':
	  	cur.execute('select Sno from shatabdi')
	  	for i in cur:
	  		print(i)
	  	f=int(input('ENTER YOUR SNO FOR DELELTE AS 1/2/3/4...'))
	  	cur.execute('delete from shatabdi where sno=%s'%f)
	  	db.commit()
	  	print('              ******your shatabdi train ticket is cancel now*******')
	  if qp=='c':
	  		railway()
	else:
		print('            ********ok your ticket is not cancel*******')
		# after the cancelling the ticket then call the railway function
		railway()
		
		
		
		
		
		
		


# this function for checking the train for booking 

def rails():
	print("a.FOR CHECKING KERALA EXPRESS")
	print("b.FOR CHECKING SHATABDI EXPRESS")
	print('c.for back to menu')
	w=input('enter your choice')
	if w=='a':
		cur.execute('select Sno from kerala')
		for i in cur:
			print('your Sno. is',i)
			
		d=input('ENTER YOUR SNO. as 1/2/3/4...')
		cur.execute('select*from kerala where Sno=%s'%(d,))
		for i in cur:
			print(i)
		rails()
	elif w=='b':
		cur.execute('select Sno from shatabdi')
		
		for i in cur:
			print('your Sno. is',i)
			
		q=input('ENTER YOUR SNO. as1/2/3/4....')
		cur.execute('select*from shatabdi where Sno=%s'%(q,))
		for i in cur:
			print(i)
		rails()
	elif w=='c':
		railway()
	
	
	else:
		print('please enter your choice')
		rails()
		# this function for giving the searched train 
def rail(FR,des):
			
			def traink():
				
				print('Searching for the train...')
				print('*****no. of train are available****')
				
				print('     **a.Kerala Express**')
				print('     **b.Shatabdi Express**')
				print('      **c.back for menu')
				ch=input('enter your choice')
				return ch
				
				
				
				
				
				
				
				
				
				
			
			chs=traink()
			if chs=='a':
				try:
					a=int(input('ENTER SNO. NUMBER'))
					b=input('ENTER YOUR NAME')
					c=int(input('ENTER YOUR PHONE NO.'))
					d=input('ENTER YOUR CLASS')
					e=int(input('ENTER YOUR NO. OF PASEENGER'))
					i=60*e
					query="insert into kerala values(%s,'%s',%s,'%s',%s,'%s','%s',%s)"%(a,b,c,d,e,FR,des,i)
					cur.execute(query)
					print('                 *****√  your booking is successfull')
					db.commit()
					traink()
				except:
					print('********PLEASE ENTER YOUR CORRECT INFORMATION********')
					traink()
				
				

			
			
			elif chs=='b':
				try:
					a=int(input('ENTER SNO. NUMBER'))
					b=input('ENTER YOUR NAME')
					c=int(input('ENTER YOUR PHONE NO.'))
					d=input('ENTER YOUR CLASS')
					e=int(input('ENTER YOUR NO. OF PASEENGER'))
					l=67*e
					query="insert into shatabdi values(%s,'%s',%s,'%s',%s,'%s','%s',%s)"%(a,b,c,d,e,FR,des,l)
					cur.execute(query)
					print('                *****√  your booking is successfull')
					db.commit()
					traink()
				except:
					print('******PLEASE ENTER YOUR CORRECT INFORMATION******')
					traink()
				
			
			
			elif chs=='c':
				# calling the railway funcion
				railway()
			else:
				print()
				traink()
				
				
				
				
			
				
				
				
	
try:
	cur.execute('create database railway')
	cur.execute('use railway')
	q="create table kerala(Sno integer primary key,Name varchar(15) NOT NULL,phoneno integer NOT NULL,class varchar(25) NOT NULL,passenger integer NOT NULL,yourlocation varchar(12) NOT NULL,destination varchar(12) NOT NULL,Rs integer)"
	cur.execute(q)
	p="create table shatabdi(Sno integer primary key,Name varchar(15) NOT NULL,phoneno integer NOT NULL,class varchar(25) NOT NULL,passenger integer NOT NULL,yourlocation varchar(12) NOT NULL,destination varchar(12) NOT NULL,Rs integer)"
	cur.execute(p)
	railway()
except:
	cur.execute('use railway')
	# for defining the railway function for taking the data 
	def railway():
		print('*******WELCOME TO THE TRAIN RESERVATION*******')
		print('         ***********menu************')
		print('             *******a.BOOKING FOR THE TRAIN*******')
		print('             *******b.CHECKING THE TRAIN*******')
		print('             *******c.CANCEL FOR TICKET*******')
		print('             *******d.FOR UPDATE YOUR TICKET*******')
		print('             *******e.EXIST*******')

		choice=input('ENTER YOUR CHOICE')
		choices=choice.lower()
		if choices=='a':
			u=input('will you want booking a ticket Y/N')
			k=u.lower()
			if k=='y':
				FR=input('ENTER YOUR PLACE')
				des=input('ENTER YOUR DESTINATION')
				rail(FR,des)
		if choices=='b':
			rails()
		if choices=='c':
			cancel()
		if choices=='d':
			x=input('did you want update your ticket Y/N')
			m=x.lower()
			if m=='y':
				update()
				
				
				
				
				
			
		# this is for existing from railway file
		if choices=='e':
			print('existing...')
			def xc():
				wc=input('did you to open Y/N')
				sc=wc.lower()
				if sc=='y':
					railway()
				elif sc=='n':
					xc()
				else:
					print('*****PLEASE ENTER CORRECT CHOICE FROM Y/N*****')
					xc()
			xc()
			
		
		else:
			print('***********PLEASE ENTER YOUR CORRECT CHOICE*************')
			
			railway()
		
			
	# calling the function railway for restart
	railway()

			
	

	
	
		
		

		
		


