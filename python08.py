# ============================================================
#
# Student Name (as it appears on cuLearn): Yiming He
# Student ID (9 digits in angle brackets): <101090748>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

'''
This is the build function that let users to build their chessboard.each row should under the requirement of length function.  

@params		none
@return		store store the build. 
'''

def build():
	store, l=[],[]
	for i in range(1,9):
		while True:
			l=[]
			print("please type the", i,"row of your chessboard.Ex,----X---",end="")
			a=input(": ")
			for j in a:
				l.append(j)
			if length(l):
				store.append(l)
				break
			else:
				print("Invalid type.")
	return store

'''
This is the length function that check the chessboard is 8X8. and check the letters that users typed should meet the requirement. 

@params		l	each row of chessboardthat users want to build.
@return		i	return the answer after check the letters that users typed.
'''

def length(l):
	i=True
	if len(l)!=8:
		return False
	for j in l:
		if not j in ['-','K','Q','B','N','R','P','k','q','b','n','r','p']:
			i=False
	return i

'''
This is the structure function to modify the whole chessboard. 

@params		store	use the stored information for structure function.
@return		NONE	
'''


def structure(store):
	num=0
	print(" 1 2 3 4 5 6 7 8 ")
	for i in store:
		num+=1
		print(num,end="")
		for j in i:
			print(j,end=" ")
		print("")
'''
This is the move function that let users to move pieces. The pieces they want move should be current pieces. if they input any empty place or out of the chessboard range, they need retype their move. if one side's piece move on other side's piece place, it will be replaced. 

@params		store	use the stored information 
@return		store	store the new chessboard after move
'''

def move(store):
	while True:
		a=int(input("which row of piece you want move:"))
		b=int(input("which column of piece you want move:"))
		if 1<=a<=8 and 1<=b<=8 and store[a-1][b-1]!='-':
			break
		else:
			print("sorry, it is invalid, please try again.")
	i=store[a-1][b-1]
	store[a-1][b-1]=('-')
	while True:
		c=int(input("Which row you want move to:"))
		d=int(input("which column you want move to:"))
		if 1<=c<=8 and 1<=d<=8:
			break
		else:
			print("sorry, invalid move, please try again:")
	store[c-1][d-1]=i
	return store

'''
This is the score function that check to scores of White side and black side. "Q,q" is 10 scores,"K,k" is 0 score, "B,b" is 3 scores, "N,n is 3.5 scores, "R,r" is 5 scores, "P,p" is 1 scores. 

@params		store	use the stored information 
@return		Whitescore	the scores of White is sum of all lowercases letters' scores.
		Blackscore	the scores of Black is sum of all uppercases letters' scores
'''

def score(store):
	Whitescore=0
	Blackscore=0
	for i in store:
		for j in i:
			if j=="Q":
				Blackscore+=10
			elif j=="q":
				Whitescore+=10
			elif j=="B":
				Blackscore+=3
			elif j=="b":
				Whitescore+=3
			elif j=="N":
				Blackscore+=3.5
			elif j=="n":
				Whitescore+=3.5
			elif j=="R":
				Blackscore+=5
			elif j=="r":
				Whitescore+=5
			elif j=="P":
				Blackscore+=1
			elif j=="p":
				Whitescore+=1
	return Whitescore,Blackscore

'''
This is the main function to program chessboard. There is a list of menu show to users. Users can play chessboard by choice option from menu. The chessboard they made will display to users after every steps.

@params		NONE	 
@return		NONE	
'''


def main():
	a=input("Hello, do you need instructions?(yes/no)").upper()
	if a=="YES":
		print('''==================================instructions==================================
Welcome to my chessboard game! Firstly, you can build your chessboard and play it. The structure of chessboard is by "-","k","q","b","n","r","p","K","Q","B","N","R","P","K". "-" represent empty space, lowercase letters are white pieces and uppercase letters are black pieces. After building your own chessboard, you can move both side pieces, and each sides pieces can eat each other if they moved to other sides. The basic chessboard with all empty is like:\n--------\n--------\n--------\n--------\n--------\n--------\n--------\n--------\nyou can place pieces everywhere step by step. You can also have other requires at the list of main menu, such as the numbers of each side's pieces left,which side is winner and quit. ''')
	b=build()
	structure(b)
	while True:
		print("==========MAIN MENU==========")
		print("1,Instructions")
		print("2,Scores.")
		print("3,Who is winner?")
		print("4,Play chessboard.")
		print("5,Quit")
		c=input("Make your choose:")
		if c=="1":
			print('''==================================instructions==================================
Welcome to my chessboard game! Firstly, you can build your chessboard and play it. The structure of chessboard is by "-","k","q","b","n","r","p","K","Q","B","N","R","P","K". "-" represent empty space, lowercase letters are white pieces and uppercase letters are black pieces. After building your own chessboard, you can move both side pieces, and each sides pieces can eat each other if they moved to other sides. The basic chessboard with all empty is like:\n--------\n--------\n--------\n--------\n--------\n--------\n--------\n--------\nyou can place pieces everywhere step by step. You can also have other requires at the list of main menu, such as the numbers of each side's pieces left,which side is winner and quit. ''')
			print("This is your chessboard:")
			structure(b)
		elif c=="2":
			(Whitescore,Blackscore)=score(b)
			print("\n\tThe White score is:", Whitescore)
			print("\n\tThe Black score is:", Blackscore)
			print("This is your chessboard:")
			structure(b)
		elif c=="3":
			print("\n\tThe White score is:", Whitescore)
			print("\n\tThe Black score is:", Blackscore)
			if Blackscore>Whitescore:
				print("\n\tBlack side is winner.")
			elif Blackscore<Whitescore:
				print("\n\tWhite side is winner.")
			else:
				print("Draw.")
			print("This is your chessboard:")
			structure(b)
		elif c=="4":
			b=move(b)
			structure(b)
		elif c=="5":
			quit()
main()
