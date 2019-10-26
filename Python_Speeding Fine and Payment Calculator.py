#Speeding Fine
#Jan. 16th, 2018
#This program calculates a fine for speeding
#50 fee plus $5 for every mph over speed limit
#Additional flat fee of $200 for over 90 mph

def main():
    #declare constants for FLATFEE of 50, MPHOVER of 5, and OVER90FEE of 200
    FLATFEE = 50
    MPHOVER = 5
    OVER90FEE = 200
	
    #declare and initialize ints for speedlimit, speed, totalfee
    speedLimit = speed = totalFee = 0
	
    #Intro
    print("Welcome to the Speeding Fine Calculator!\n")
    print("To begin, you will enter a speed limit and the value of the speed the traveler was going," + 
    " you will then see the fine incurred.\n\n")

    try:

        #Prompt for speed limit
        speedLimit = int(input("Please enter the speed limit: "))

        #prompt for speed
        speed = int(input("Please enter the speed traveled: "))

        #Use decision structure to determine if speeding or not	
        #compare speedlimit to speed going
        if speed <= speedLimit:
            print("\n\nGreat driving, no speeding fine!")
        #and display fine if speeding	
        #if over limit but <= 90 set totalFee = (speed - speedlimit) * MPHOVER + FLATFEE
        #if over 90 mph set total fee = (speed - speedlimit) * MPHOVER + FLATFEE + OVER90FEE
        elif speed > speedLimit:
            if speed > 90:
                print("\n\nWhat, over 90! SLOW DOWN!")
                totalFee = (speed - speedLimit) * MPHOVER + FLATFEE + OVER90FEE
                print("\nYour fine is ${:,.2f}".format(totalFee))
            else:
                totalFee = (speed - speedLimit) * MPHOVER + FLATFEE
                print("\nYou were speeding and your fee will be ${:,.2f}".format(totalFee))

        #Now we start the fee payment process
        print("\n\nPlease pay your speeding fee NOW!")
        payAmt = 0
        #Prompt for bills
        #Start with $100 bills
        hundredBill = int(input("How many $100 bills do you have? "))
        payAmt = (100 * hundredBill)
        #check if the amount covers the fee
        if payAmt > totalFee:
            print("\n\nThank you for your payment. Your change is ${:,.2f}".format(payAmt - totalFee))
        else:
            print("\n\nYou need to pay another ${:,.2f}".format(totalFee - payAmt) + " to complete your full fee amount.")
        
        bal = totalFee - payAmt
        
        #$50 bills
        fiftyBill = int(input("\n\nHow many $50 bills do you have? "))
        b50 = []
        for i in range (0,fiftyBill):
            elem = int(50)
            b50.append(elem)
        payAmt = sum(b50)
        #b50 = [50,50] if fiftybil = 2
       
        totalFee = bal
        if payAmt > totalFee:
            print("\n\nThank you for your payment. Your change is ${:,.2f}".format(payAmt - totalFee))
        elif payAmt == totalFee:
            print("\n\nThank you for your payment, please slow down.")
        else:
            print("\n\nYou need to pay another ${:,.2f}".format(totalFee - payAmt) + " to complete your full fee amount.")
        bal = totalFee - payAmt
        
        #$20 bills
        twentyBill = int(input("\n\nHow many $20 bills do you have? "))
        b20 = []
        j = 0
        while j < twentyBill:
            #elem = int(20)
            #b20.append(elem)
            j += 1
        payAmt = payAmt + sum(b20)

        totalFee = bal
        if payAmt > totalFee:
            print("\n\nThank you for your payment. Your change is ${:,.2f}".format(payAmt - totalFee))
        elif payAmt == totalFee:
            print("\n\nThank you for your payment, please slow down.")
        else:
            print("\n\nYou need to pay another ${:,.2f}".format(totalFee - payAmt) + " to complete your full fee amount.")
        bal1 = totalFee - payAmt
        
        #$10 bills
        tenBill = int(input("\n\nHow many $10 bills do you have? "))
        b10 = []
        t = 0
        while t < tenBill:
            t += 1
        payAmt = payAmt + sum(b10)

        totalFee = bal
        if payAmt > totalFee:
            print("\n\nThank you for your payment. Your change is ${:,.2f}".format(payAmt - totalFee))
        elif payAmt == totalFee:
            print("\n\nThank you for your payment, please slow down.")
        else:
            print("\n\nYou need to pay another ${:,.2f}".format(totalFee - payAmt) + " to complete your full fee amount.")
        bal2 = totalFee - payAmt

        #$5 bills
        fiveBill = int(input("\n\nHow many $5 bills do you have? "))
        b5 = []
        for i in range (0,fiveBill):
            i+= 1
        payAmt = payAmt + sum(b5)

        totalFee = bal2
        if payAmt > totalFee:
            print("\n\nThank you for your payment. Your change is ${:,.2f}".format(payAmt - totalFee))
        elif payAmt == totalFee:
            print("\n\nThank you for your payment, please slow down.")
        else:
            print("\n\nYou need to pay another ${:,.2f}".format(totalFee - payAmt) + " to complete your full fee amount.")
        bal3 = totalFee - payAmt
      
        #$1 bills
        dollarBill = int(input("\n\nHow many $1 bills do you have? "))
        b1 = []
        for i in range (0,dollarBill):
            i+= 1
        payAmt = payAmt + sum(b1)

        totalFee = bal3
        if payAmt > totalFee:
            print("\n\nThank you for your payment. Your change is ${:,.2f}".format(payAmt - totalFee))
        elif payAmt == totalFee:
            print("\n\nThank you for your payment, please slow down.")
        else:
            print("\n\nYou need to pay another ${:,.2f}".format(totalFee - payAmt) + " to complete your full fee amount.")
  
        #outro
        print("Thank you! Goodbye!")
    except:
        print("Please enter a number for speed and speed limit")
        main()
main()	
