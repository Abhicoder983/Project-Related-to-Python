import random
# this function is for checking your pin number
def check():
	global a19
	a19 = input('ENTER YOUR PIN NUMBER')
	con.execute('select PIN from bank')
	a22=tuple(con.fetchall())

	# this is the loop
	for a20 in a22:
		if a19 in a20:
			con.execute("select NAME ,ACCOUNT_NO from bank where PIN='%s'"%(a19,))
			a21= con.fetchall()
			for i in a21:
				print('YOUR NAME & ACCOUNT NO. ',i)
			
				
			print('              *******************a.CASH DEPOSITE***************************')
			print('              ********************b.BALANCE CHECKING*************************')
			print('              ********************c.TRANSFER MONEY****************')
			print('              ********************d.CASH WITHDRAWL***************************')
			print('              ********************e.DELETE ACCOUNT***********-****************')
			print("              ********************f.FOR CANCELLING THE TRANSACTION")
			choice=input('ENTER YOUR CHOICE')
			a=choice.lower()
			if a=='a':
			  	a14=input('DO YOU WANT TO DEPOSITE YOUR CASH  Y/N :-')
			  	a14=a14.lower()
			  	if a14=="y":
			  		cashd()
			  	else:
			  		check()
								
			elif a=="b":
				a15=input('DO YOU WANT TO CHECK YOUR BALANCE Y/N :-')
				a15=a15.lower()
				if a15=="y":
					checkb()
				else:
					check()
			elif a=="c":
				a16=input('DO YOU WANT TO TRANSFER YOUR CASH  TO ANOTHER ACCOUNT Y/N :-')
				a16=a16.lower()
				if a16=="y":
					trans()
				else:
					check()
			elif a=="d":
				a16b=input('DO YOU WANT TO WITHDRAWL YOUR CASH Y/N :-')
				a16b=a16b.lower()
				if a16b=="y":
					cashw()
				else:
					check()
			elif a=='e':
				df=input('DO YOU WANT TO DELETE YOUR ACCOUNT')
				df=df.lower()
				if df=='y':
					dele()
				else:
					check()
			elif a=='f':
				a16a=input('DO YOU WANT TO CANCEL TRANSACTION Y/N :-')
				a16a=a16a.lower()
				if a16a=="y":
					bank()
				else:
					check()
			else:
				check()
	else:

		print(' YOUR PIN NUMBER IS WORNG PLEASE ENTER CORRECT PIN NUMBER')
# calling the function check for the pin number which is given by the user
		check()
		# defining the function checkb for 
def checkb():
			q="select BALANCE from bank where PIN='%s'"%(a19,)
			con.execute(q)
			wq=con.fetchall()
			for iq in wq:
				print('**********YOUR BALANCE IS************',iq) 
			bank()
	# this function delete is for deleting the bank account 
def dele():
	con.execute("delete from bank where PIN='%s'"%(a19))
	db.commit()
	
	print('*******************YOUR ACCOIUNT HAS BEEN DELETED IN THIS BANK***************')
	# calling the function bank 
	bank()
	# defining the fuction for withdrawing cash
def cashw():
	a18=int(input('HOW MUCH MONEY DO YOU WANT TO WITHDRAWL MONEY :-'))
	con.execute("select BALANCE from bank where PIN='%s' "%(a19,))
	b7=con.fetchall()
	# this loop condition
	for i7 in b7:
		for w7 in i7:
			wcb=w7-a18
			print('*****YOUR INTIAL AMOUNT IS',i7,'********')
			print('*****YOUR WITHDRAWLAMOUNT IS',a18,'*******')
			print('*****YOUR FINAL AMOUNT IS', wcb,'*********')
	que="update bank set BALANCE=%s where PIN = '%s' "%(wcb,a19)
	con.execute(que)
	db.commit()
	bank()
	# this function is for transaction of cash from one account to the other account 
def trans():
			a18p=int(input('HOW MUCH MONEY DO YOU WANT TO WITHDRAWL MONEY :-'))
			a19s=input('ENTER THE PIN NUMBER OF THE ACCOUNT WHERE YOU WANT TO TRANSFER YOUR MONEY')
			
			
			
			con.execute('select PIN from bank')
			q2=con.fetchall()
			for abc in q2:
					if a19s in abc:
						nb=1
			if nb==1:
				con.execute("select BALANCE from bank where PIN='%s' "%(a19,))
				b7p=con.fetchall()
				for i7p in b7p:
					for w7p in i7p:
						wcbp=w7p-a18p
						print('*****YOUR INTIAL AMOUNT IS',i7p,'********')
						print('*****YOUR TRANSFER MONEY IS',a18p,'*******')
						print('*****YOUR FINAL AMOUNT IS', wcbp,'*********')
				quep="update bank set BALANCE=%s where PIN = '%s' "%(wcbp,a19)
				con.execute(quep)
				db.commit()
				con.execute("select BALANCE from bank where PIN='%s'"%(a19s,))
				wa=con.fetchall()
				con.execute("select NAME from bank where PIN='%s'"%(a19s,))
				wz=con.fetchall()
				for rf in wz:
					print("ACCOUNT NAME WHERE YOU WANT TO TRANSFER MONEY ",rf)
				for wr in wa:
					for wt in wr:
						ts=wt+a18p
				con.execute("update bank set BALANCE=%s where PIN = '%s'"%(ts,a19s))		
				print("*********YOUR MONEY HAS BEEN TRANSFER BY THIS ATM MACHINE ********")
				
				bank()
			else:
				print("**********PLEASE WRITE CORRECT PIN NUMBER OF THE ACCOUNT WHERE YOU WANT  TO TRANSFERING THE MONEY********************")
				trans()

					
			
			
			
		
			
		
			
			# this function is used for depositing the cash to your account
	
def cashd():
	a18=int(input('HOW MUCH MONEY DO YOU WANT TO DEPOSITE :-'))
	con.execute("select BALANCE from bank where PIN='%s' "%(a19,))
	b7=con.fetchall()
	for i7 in b7:
		for w7 in i7:
			wcb=a18+w7
			print('*****YOUR INTIAL AMOUNT IS',i7,'********')
			print('*****YOUR DEPOSITE AMOUNT IS',a18,'*******')
			print('*****YOUR FINAL AMOUNT IS', wcb,'*********')
	que="update bank set BALANCE=%s where PIN = '%s' "%(wcb,a19)
	con.execute(que)
	db.commit()
	# calling the function bank 
	bank()
	
	
	
	#opening the bank account 
def open():
	per=input('do you want to open your account y/n')
	per=per.lower()
	if per=='y':
		try:
			a6=input('ENTER YOUR NAME')
			a7=int(input('ENTER YOUR MOBLIE NUMBER'))
			a8=input("ENTER YOUR DOMINATE'S NAME ")
			a9=input('ENTER YOUR F.NAME')
			a10=input('ENTER YOUR ADDRESS')
			a13=5
		except:
			print('******************PLEASE ENTER ALL YOUR NECESSARY INFORMATION*************************')
			open()
		a7=str(a7)
		
		con.execute('select PIN from bank')
		
		sx=tuple(con.fetchall())
		# creating the bank account number
		def acc():
			fg=1
			while fg==1:
				ep=str(random.randint(111111111111,999999999999))
				for i in ep:
					if ep not in i:
						return ep
						fg=2
						break
		n=1
		while n==1:
			az= str(random.randint(1111,9999))
			for wx in sx:
				if az not in wx:
					qw=acc()
					tg=az
					n=2
					
					break
		
		que="insert into bank values('%s','%s','%s','%s','%s','%s','%s','%s')"%(tg,a6,qw,a7,a9,a8,a10,a13)
		con.execute(que)
		db.commit()
		print('            **************************&&&NOTE:-YOUR ACCOUNT HAS CREATED IN THIS BANK&&**************************')
		print('             **************************&&&nNOTE:-PLEASE REMEMBER THSI PIN NUMBER ,ACCOUNT NUMBER WHENEVER YOU WANT TO DO ANY TRANSACTION*****************************ACCOUNT NUMBER IS ',qw,'AND PIN NUMBER IS',az)
		print('THANKS TO MAKING YOUR ACCOUNT IN THIS BANK')
		bank()		
	else:
		bank()	
	# defing the function bank
def bank():
			try:
				con.execute('create database abhi_bank ')
				con.execute('use abhi_bank')
				con.execute('create table bank(PIN varchar(23) , NAME varchar(16) NOT NULL,ACCOUNT_NO varchar(19) primary key NOT NULL,MOBLIE_NUM varchar(13) NOT NULL,F_NAME varchar(20) NOT NULL, DOMINATE varchar(20) NOT NULL,ADDRESS varchar(30) NOT NULL, BALANCE int(30) NOT NULL)' )
				www()
			except:
				def www():
					con.execute('use abhi_bank')
					print('***************WELCOME TO THE ABHISHEK AND SHIYA BANK********************')
					print("             ********************a.OPENING ACCOUNT***************************")
					print("              ********************b.FOR ANY TRANSCATION********************")
					print("              ********************c.FOR EXISTING******************")
			
			   
					
					choice=input('ENTER YOUR CHOICE')
					a=choice.lower()
					if a=='a':
						open()
					elif a=='b':
						mn=input('DO YOU WANT ANY TRANSACTION Y/N')
						mn=mn.lower()
						if mn=="y":
							check()
						else:
							bank()			            
					
					
					elif a=='c':
					            we=1
					            while we==1:
					            	ab=input('DO YOU WANT TO OPEN THIS ATM MACHINE PRESS Y/N')
					            	a1=ab.lower()
					            	if a1=='y':
					            		
					            		bank()
					            		
					            		
					            			
					            	else:
										print('****************ENTER CORRECT PASSWORD*****************')
					            		we=1	            
					else:
						print('***********************PLEASE PRESS COPRRECT KEY*******************')
						www()   
					# calling the function www
				www()                                              
# this is for checking that mysql is connect or not
def ab():	
	a=input ("enter your localhost")
	b=input("enter your root")
	c=input("enter your password")
	try:
		import mysql.connector
		yj= mysql.connector.connect(host=a, user=b,passwd=c)
		return yj		
	except:
			print(" your password, localhost&root is wrong, please enter your correct password")
			ab()
db=ab()

if db.is_connected:
	con=db.cursor()
	# calling the functio of bank for futher processing 
	bank()
else:
	ab()


			


			