#!/usr/bin/env python3
#Guessing Game
#KBowen

def getChoice():
  validator = False
  while not validator:
    try:
      c = int(input("Select Game Type: 1=Hot/Cold, 2=High/Low, 0=Quit: ")
      if c < 0 or c > 2:
        print("Illegal value:  Please select 0, 1, or 2.
        validator = False
      else:
      	validator = True
			except ValueError:
      	print("Illegal Value, please enter 1, 2, or 0.")
      	validator = False
	return c



def main():

  print("Welcome to the Guessing game!")
  choice = getChoice()
  
	while choice!=0:
							
	

#launch program based on env pariable name
if __name__ == "__main__":
    main()
