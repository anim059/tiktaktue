#tiktaktue game

broad=["-","-","-"
       ,"-","-","-"
       ,"-","-","-"]

game_is_over=True
currentplayer="X"
winner=None
def displaybroad():
  print(broad[0]+"|"+broad[1]+"|"+broad[2])
  print(broad[3]+"|"+broad[4]+"|"+broad[5])
  print(broad[6]+"|"+broad[7]+"|"+broad[8])


def playgame():
  displaybroad()
  while game_is_over:
    handleturn(currentplayer)
    
    check_for_winner() 
    check_for_tie()
    flip_player()

  if winner=='X'or winner=='O':
     print(winner +'wins')
  else:
     print('game tie')
        


def handleturn(player):
  print("now turn player "+player)
  position=input("enter a position between 1-9:")
  valid=False
  while not valid:
   while position not in ['1','2','3','4','5','6','7','8','9']:
     print("plz enter between (1-9)")
     if broad[position-1]=="-":
        position=input("enter a position between 1-9:") 

   position=int(position)-1
   if broad[position]=='-':
     valid=True
   else:
     print('cant')  
 
  broad[position]=player
  displaybroad()

def check_for_tie():
  global game_is_over
  if "-" not in broad:
    game_is_over=False  
  return
def check_for_winner():
  global winner
  rowwinnwe=checkrow()
  coloumwinner=checkcoloum()
  diagonalwinner=checkdaigolan()

  if rowwinnwe:
    winner=rowwinnwe
  elif coloumwinner:
    winner=coloumwinner
  elif diagonalwinner:
    winner=diagonalwinner    
  return

def checkrow():
  global game_is_over
  row1=broad[0]==broad[1]==broad[2]!="-"
  row2=broad[3]==broad[4]==broad[5]!="-"
  row3=broad[6]==broad[7]==broad[8]!="-"
  
  if row1 or row2 or row3:
    game_is_over=False
    if row1:
      return broad[0]
    elif row2:
      return broad[3]  
    elif row3:
      return broad[6]  
  return

def checkcoloum():
  global game_is_over
  coloum1=broad[0]==broad[3]==broad[6]!="-"
  coloum2=broad[1]==broad[4]==broad[7]!="-"
  coloum3=broad[2]==broad[5]==broad[8]!="-"
  
  if coloum1 or coloum2 or coloum3:
    game_is_over=False
    if coloum1:
      return broad[0]
    elif coloum2:
      return broad[1]  
    elif coloum3:
      return broad[2]  
  return

def checkdaigolan():
  global game_is_over
  dia1=broad[0]==broad[4]==broad[8]!="-"
  dia2=broad[2]==broad[4]==broad[6]!="-"

  
  if dia1 or dia2:
    game_is_over=False
    if dia1:
      return broad[0]
    elif dia2:
      return broad[2]   
  return

def flip_player():
  global currentplayer
  if currentplayer=="X":
    currentplayer="O"
  else:
    currentplayer="X"  
  return  

playgame()

