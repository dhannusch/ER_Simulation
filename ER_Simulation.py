#  File: ER_Simulation.py
#  Description: simulates an Emergency Room order of attending
#  Name: Dennis Hannusch

#  Date Created: 10/7/16
#  Date Last Modified: 10/7/16

class Queue (object):

    def __init__(self):
        self.items = []
        

    def enqueue(self,item):
        self.items.append(item)


    def dequeue(self):
        return self.items.pop(0)


    def isEmpty(self):
        return self.items == []


    def size(self):
        return len(self.items) 


    def peek(self):
        return self.items[0]

    def __str__(self):
        return( str(list(reversed(self.items))) )

def displayQueues(Critical,Serious,Fair):

    print("Queues are:")
    print("Critical:", Critical)
    print("Serious:", Serious)
    print("Fair:", Fair)
    print()
    
def main():

    ER = open("ERsim.txt","r")

    Critical = Queue()
    Serious = Queue()
    Fair = Queue()

    for line in ER:
        line = line.strip()
        line = line.split(" ")

        if line[0] == "add":
            
            if line[2] == "Critical":
                print("Add patient", line[1], "to Critical queue")
                Critical.enqueue(line[1])
                displayQueues(Critical,Serious,Fair)

            elif line[2] == "Serious":
                print("Add patient", line[1], "to Serious queue")
                Serious.enqueue(line[1])
                displayQueues(Critical,Serious,Fair)

            elif line[2] == "Fair":
                print("Add patient", line[1], "to Fair queue")
                Fair.enqueue(line[1])
                displayQueues(Critical,Serious,Fair)

        elif line[0] == "treat":

            if line[1] == "next":

                if not Critical.isEmpty():
                    print("Treating", Critical.peek(),"from Critical queue")
                    Critical.dequeue()
                    displayQueues(Critical,Serious,Fair)
                elif not Serious.isEmpty():
                    print("Treating", Serious.peek(),"from Serious queue")
                    Serious.dequeue()
                    displayQueues(Critical,Serious,Fair)
                elif not Fair.isEmpty():
                    print("Treating", Fair.peek(),"from Fair queue")
                    Fair.dequeue()
                    displayQueues(Critical,Serious,Fair)
                else:
                    print("No patients in queues")

            elif line[1] == "Critical":

                if not Critical.isEmpty():
                    print("Treating", Critical.peek(),"from Critical queue")
                    Critical.dequeue()
                    displayQueues(Critical,Serious,Fair)

                else:
                    print("No patients in Critical queue")

            elif line[1] == "Serious":

                if not Serious.isEmpty():
                    print("Treating", Serious.peek(),"from Serious queue")
                    Serious.dequeue()
                    displayQueues(Critical,Serious,Fair)

                else:
                    print("No patients in Serious queue")

            elif line[1] == "Fair":

                if not Fair.isEmpty():
                    print("Treating", Fair.peek(),"from Fair queue")
                    Fair.dequeue()
                    displayQueues(Critical,Serious,Fair)

                else:
                    print("No patients in Fair queue")


            elif line[1] == "all":

                while( not Critical.isEmpty() or not Serious.isEmpty() or not Fair.isEmpty() ):

                    if not Critical.isEmpty():
                        print("Treating", Critical.peek(),"from Critical queue")
                        Critical.dequeue()
                        displayQueues(Critical,Serious,Fair)
                    elif not Serious.isEmpty():
                        print("Treating", Serious.peek(),"from Serious queue")
                        Serious.dequeue()
                        displayQueues(Critical,Serious,Fair)
                    elif not Fair.isEmpty():
                        print("Treating", Fair.peek(),"from Fair queue")
                        Fair.dequeue()
                        displayQueues(Critical,Serious,Fair)

        else:
            print("Exit")
            break

    ER.close()

main()
