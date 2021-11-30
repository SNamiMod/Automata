# in this code we check if a string is acceptable in Automatas A & B 
# 
# Nov. 2021
# Seyed Nami Modarressi

# Todo :
#  1 ) input String and machines ==> Done
#  2 ) write accept function
#  3 ) use function for A and B and String 
#  4 ) add an example
import numpy as np

alphabet = []
automata_A = []
automata_A_size = 0
automata_A_finals = []
automata_B = []
automata_B_size = 0
automata_B_finals = []
input_String = ""

alphabet = input("\n\nEnter alphabet with ',' (exp. :  a,b,c  or  0,1) :")
alphabet = alphabet.split(",")
input_String = input("\nEnter string :")
in_alphabet_flag = 0
for i in input_String:
    for j in alphabet:
        if i == j:
            in_alphabet_flag = 1
            break
    if in_alphabet_flag == 1:
        break
if in_alphabet_flag == 0:
    print("\nInvalid string . Enter string with given alphabet")
else:
    # String is OK
    # now we get machine A
    automata_A_size = int(input("\nEnter number of nodes(states) for first machine :"))
    automata_A = input("\nEnter transition table for first machine (from [0,0] to [size,size] with ',' like alphabet) :")
    automata_A = automata_A.split(",")
    temp = np.reshape(automata_A , (automata_A_size,len(alphabet)))
    automata_A = temp
    print("\nFirst Machine : \n")
    print("       ",end="")
    for i in alphabet:
        print(i , end="  ")
    print("\n",end="")
    print("------"*len(alphabet))
    for i in range(0 , automata_A_size):
        print("Q",end="")
        print(i,end="")
        print(" |   ",end="")
        for j in range(0 , len(alphabet)):
            print(automata_A[i][j] , end="  ")
        print("\n")
    automata_A_finals = input("\nEnter 'Goal' nodes for first machine(without 'P' - with ',' like alphabet) :")
    automata_A_finals = automata_A_finals.split(",")
    # now we get machine B
    automata_B_size = int(input("\nEnter number of nodes(states) for second machine :"))
    automata_B = input("\nEnter transition table for first machine (from [0,0] to [size,size] with ',' like alphabet) :")
    automata_B = automata_B.split(",")
    temp = np.reshape(automata_B , (automata_B_size,len(alphabet)))
    automata_B = temp
    print("\nSecond Machine : \n")
    print("       ",end="")
    for i in alphabet:
        print(i , end="  ")
    print("\n",end="")
    print("------"*len(alphabet))
    for i in range(0 , automata_B_size):
        print("P",end="")
        print(i,end="")
        print(" |   ",end="")
        for j in range(0 , len(alphabet)):
            print(automata_B[i][j] , end="  ")
        print("\n")
    automata_B_finals = input("\nEnter 'Goal' nodes for second machine(without 'P' - with ',' like alphabet) :")
    automata_B_finals = automata_B_finals.split(",")
    
