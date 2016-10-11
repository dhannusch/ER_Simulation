# ER_Simulation
Using python and a QUEUE abstract data structure to simulate an emergency room waiting line.
The program opens a file called ERsim.txt and reads in a list of instructions.
Example of ERsim.txt (must use this formatting):
  "
    add Scott,M. Critical
    add Shrute,D. Serious
    add Halpert,J. Fair
    add Beasley,P. Critical
    add Bernard,A. Serious
    add Malone,K. Fair
    treat next
    treat next
    add Howard,R. Fair
    treat next
    treat next
    treat next
    add Bratton,C. Critical
    add Vance,P. Serious
    treat next
    treat next
    treat next
    add Hudson,S. Critical
    add Kapoor,K. Serious
    add Flenderson,P. Fair
    add Philbin,D. Serious
    add Palmer,M. Critical
    add Martin,A. Serious
    treat Serious
    treat all
    treat next
    exit
  "
  
  Note: I may later implement a writing function, which allows you to add names and their conditions to the txt file and then commands for         more user control.
  
