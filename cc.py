print("       — WELCOME TO COINCOUNT —")
print()
print("""MMMMMMMMMMMWWMMMMMMMMMMMWWWWWWMMMMMMMMMMMMMMM
MMMMMMMMMMMWWWWNX0OkkkxxxkkOKNWWWWWMWWWWMMMMM
MMMMMMMMWWWXkdooooooooooolllllodkKWWWWMWWMMMM
MMMMMMWWXkolodk0K0000OOOOOkkkxoc:;cxKWWWMMMMM
MMMWWWXxllx0K0000000000OOOOkkkxxxl;,;oKWWWMMM
MMWWNkclOKKKK000kxoooooolllodxxxxdoc;',xXWWMW
MWWXo:kXXKKK0kdoodxkkOOkkxolcccodddo:;,'cKWWW
WWXocOXKXKKOdld0KKKK000000Okxo:;:odol:;;.cKWW
WWx:kXXXXKklo0XXKKKK0000OOOOOxlc;;looc;;,.oNW
WKcoXXXXXOcoKXKKKKK00000OOOkkkdc:;,loc;;,',OW
Wk:kXXXKKdcOXKKKK00000OOOOOkxxdl::,;oc;;,,'xW
Wx:OXXXXKll0XKKK00000OOOOkkkxxdc;:,,lc;;,,.dW
Wk:kXXXKKocOKKK00000OOOOkkkxxdl:;;';l:;,;'.xW
WKcoXXXKXOco0K00000OOOOkkkxddo:;;,,cc;;,;',OW
WWd:OXXXKKkcoO0000OOOkkkxxdoc:;;,,cc:;;;,.oNW
WWXocOXXXKK0ocokOOOkxxddolc::;,,:cc:;;;,'cKWM
WWWXockXXKKKKkollllolllc::;,;:cllc:;:;,'cKWMM
MMWWNkcoOKKK00K0kdolollllllooooc::::;',dXWMMM
MMMMWWKdclk0000000000OOOkxdolc::::;';o0WMMMMM
MMMMMWWWXxolcodxxxxxdooollclcc:;,;cdKWWWMMMMM
MMMMMMMMMWWKkolc:;;;;;;;;;;;::lokKNWWMMMMMMMM
MMMMMMMMMMMMWWWXKOkxxxdxxxkOKNWWMMMMMMMMMMMMM
MMMMMMMMMMMMMMWWWWWWMMMMWWMWWMMMMMMMMMMMMMMMM""")
print()
coins = {
  "1p" : { #the coin
    "maths" : 0.01, #the coin as a decimal
    "bag value" : 1, #the value of an accurate bag of these coins
    "coin weight" : 3.56 #the weight of one coin
  },
  "2p" : {
    "maths" : 0.02,
    "bag value" : 1,
    "coin weight" : 7.12
  },
  "5p" : {
    "maths" : 0.05,
    "bag value" : 5,
    "coin weight" : 2.35
  },
  "10p" : {
    "maths" : 0.1,
    "bag value" : 5,
    "coin weight" : 6.5
  },
  "20p" : {
    "maths" : 0.2,
    "bag value" : 10,
    "coin weight" : 5
  },
  "50p" : {
    "maths" : 0.5,
    "bag value" : 10,
    "coin weight" : 8
  },
  "£1" : {
    "maths" : 1,
    "bag value" : 20,
    "coin weight" : 8.75
  },
  "£2" : {
    "maths" : 2,
    "bag value" : 20,
    "coin weight" : 12
  },
}
volunteers = {
  "volunteer1" : { #the volunteer
    "Name" : "", #their name
    "Bags Done" : 0, #have many of their bags have been entered
    "Bags Correct" : 0, #how many bags they've done correctly
    "Bags Incorrect" : 0, #how many they've done incorrectly
    "Accuracy(%)" : 0 #the percentage of correct bags
  },
  "volunteer2" : {
    "Name" : "",
    "Bags Done" : 0,
    "Bags Correct" : 0,
    "Bags Incorrect" : 0,
    "Accuracy(%)" : 0
  },
  "volunteer3" : {
    "Name" : "",
    "Bags Done" : 0,
    "Bags Correct" : 0,
    "Bags Incorrect" : 0,
    "Accuracy(%)" : 0
  },
  "volunteer4" : {
    "Name" : "",
    "Bags Done" : 0,
    "Bags Correct" : 0,
    "Bags Incorrect" : 0,
    "Accuracy(%)" : 0
  },
  "volunteer5" : {
    "Name" : "",
    "Bags Done" : 0,
    "Bags Correct" : 0,
    "Bags Incorrect" : 0,
    "Accuracy(%)" : 0
  },
  "volunteer6" : {
    "Name" : "",
    "Bags Done" : 0,
    "Bags Correct" : 0,
    "Bags Incorrect" : 0,
    "Accuracy(%)" : 0
  }
}
BagStats = {
  "Total Bags Done" : 0,
  "Total Value(£)" : 0
}
def check_volunteer(volunteer):
  for i in volunteers:
    if volunteers[i]["Name"] == "": #checks if the name key has a value
      volunteers[i]["Name"] = volunteer #adds the volunteer's name to the 'volunteers' dictionary
      currentVolunteer = i
      return True, currentVolunteer, volunteer
    elif volunteers[i]["Name"] == volunteer: #checks if name is already in the dictionary
      currentVolunteer = i
      return True, currentVolunteer, volunteer
    elif i == "volunteer6": #sees if the last slot in the dictionary is full
      print(volunteer,"is not one of our 6 volunteers. They are:")
      for i in volunteers:
        print(volunteers[i]["Name"]) #prints all valid volunteers
      volunteer = input("Please choose again: ") 
      currentVolunteer = 0
      return False, currentVolunteer, volunteer
def input_data():
  currentVolunteer = ""
  global volunteer
  global bagweight
  global coinType
  volunteer = input("Which volunteer is it? ")
  while volunteer.isnumeric() is True:
    print("That's not a name")
    volunteer = input("Please choose again: ")
  correct = False
  while not correct:
    correct, currentVolunteer, volunteer = check_volunteer(volunteer)
    if correct is True:
      break
  bagWeight = float(input("How much does the bag weigh in grams? "))
  coinType = input("What type of coin do you have? ")  
  while True: 
    if coinType not in coins: #checks if coin type is valid
      print(coinType,"is not a valid coin type. The valid coin types are:")
      for i in coins:
        print(i) #prints all valid coin types
      coinType = input("Please choose again: ") #lets the user re-enter the coin type
    else: #breaks loop if coin type is valid
      break
  mathsCoinType = coins[coinType]["maths"] #assigns the decimal value to a variable
  return volunteer, bagWeight, coinType, mathsCoinType, currentVolunteer
def check_correct(mathsCoinType):
  fixExtra = 0
  fixUnder = 0
  coinsInTheoryBag = coins[coinType]["bag value"] / mathsCoinType #calcs how any coins should be in the bag
  theoryBagWeight = coinsInTheoryBag * coins[coinType]["coin weight"] #calcs how much the bag should weigh
  if bagWeight == theoryBagWeight: 
    print("This bag is correct.")
    outcome = "correct"
  elif bagWeight > theoryBagWeight:
    extra = bagWeight - theoryBagWeight
    fixExtra = extra / coins[coinType]["coin weight"]
    print("Remove", round(fixExtra),coinType+"s to get the correct value.")
    outcome = "extra"
  else:
    under = theoryBagWeight - bagWeight
    fixUnder = under / coins[coinType]["coin weight"]
    print("Add", round(fixUnder),coinType+"s to get the correct value.")
    outcome = "under"
  return outcome, fixExtra, fixUnder
def update_stats(currentVolunteer, coinType, outcome, fixExtra, fixUnder):
  BagStats.update({"Total Bags Done" : BagStats["Total Bags Done"]+1})
  moneyInBag = coins[coinType]["bag value"]
  if outcome == "extra":
    moneyInBag += fixExtra
  elif outcome == "under":
    moneyInBag -= fixUnder
  BagStats.update({"Total Value(£)" : round(BagStats["Total Value(£)"]+moneyInBag, 2)})
  volunteers[currentVolunteer]["Bags Done"] += 1
  if outcome == "correct":
    volunteers[currentVolunteer]["Bags Correct"] += 1
  else:
    volunteers[currentVolunteer]["Bags Incorrect"] += 1
  total = volunteers[currentVolunteer]["Bags Done"]
  accuracy = round((volunteers[currentVolunteer]["Bags Correct"] / total) * 100 , 2)
  volunteers[currentVolunteer].update({"Accuracy(%)" : accuracy})
def output_data():
  print("----------------------------------------------------------------------------------------------------------------------------------------")
  print()
  print("            — STATISTICS —")
  print()
  print(BagStats)
  print()
  print("--------------------------------------------------------------------")
  print()
  sortedVols = sorted(volunteers.items(),key=lambda x:x[1]["Accuracy(%)"],reverse=True)
  dictVols = dict(sortedVols)
  for i in dictVols:
    print(dictVols[i])
    print()
  print("----------------------------------------------------------------------------------------------------------------------------------------")
def file_saving():
  with open ("CoinCount.txt", "w") as f:
    f.write("")
  with open ("CoinCount.txt", "a") as file:
    file.write(f"{str(BagStats)}\n")
    for i in volunteers:
      file.write(f"{str(volunteers[i])}\n")
cont = "yes"
while cont == "yes" or cont == "y" or cont == "yeah" or cont == "sure":
  print("           — ENTER A BAG — ")
  print()
  volunteer, bagWeight, coinType, mathsCoinType, currentVolunteer = input_data()
  print()
  outcome, fixExtra, fixUnder = check_correct(mathsCoinType)
  print()
  update_stats(currentVolunteer, coinType, outcome, fixExtra, fixUnder)
  output = input("Display progress? ")
  match output:
    case "yes":
      print()
      output_data()
      print()
    case "y":
      print()
      output_data()
      print()
    case "yeah":
      print()
      output_data()
      print()  
    case "sure":
      print()
      output_data()
      print()
  cont = input("Do you want to add another bag? ")
  print()
  if cont != "y" and cont != "yes" and cont != "yeah" and cont != "sure":
    print("WARNING")
    print()
    msg = "The programme should not be finished until all bags have been"
    msg2 = "checked otherwise data will be wiped!"
    print(msg+msg2)
    sure = input("Still close the programme? ")
    print()
    if sure == "no" or sure == "n" or sure == "nah" or sure  == "nope":
      cont = "yes"
file_saving()
print("   — THANK YOU FOR USING COIN COUNT —")
