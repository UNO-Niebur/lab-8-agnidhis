#ProcessData.py
#Name: Nidhi Agarwal
#Date: 03/26/2026
#Assignment: reading  & writing in the file

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    id = data[3]
    major = data[6]
    year = data[5]
    

    studentID = makeID(first, last, id)
    output = last + "," + first + "," + id + "\n"

    majorYear = makeMajorYear(major, year)
    
    output = last + "," + first + "," + studentID + "," + majorYear + "\n"

      
    outFile.write(output)
  


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

  
def makeID(firstname, lastname, idnum):
  idlen= len(idnum)

  while len(lastname) < 5:
    lastname = lastname + "X" 

  id = firstname[0] + lastname + idnum[idlen -3:]

  return id  


def makeMajorYear(major, year):

    majorCode = major[:3].upper()

    # Convert year to abbreviation
    if year == "Freshman":
        yearCode = "FR"
    elif year == "Sophomore":
        yearCode = "SO"
    elif year == "Junior":
        yearCode = "JR"
    elif year == "Senior":
        yearCode = "SR"
    else:
        yearCode = "NA"   # if something unexpected is entered

    result = majorCode + "-" + yearCode

    return result
    

if __name__ == '__main__':
  main()
