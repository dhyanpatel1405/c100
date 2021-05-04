class Atm():

    def __init__(self,card_number,pin_number):
        self.Card_number = card_number
        self.Pin_number = pin_number

    def check_balance(self):
        print("you have gained access of your account. your current balance is $500000")

    def cash(self,amount):
        print("you have withdrawn-->"+str(amount)) 

def main():
# Card_number=input('enter your card number here')
#Pin_number=input('enter your pin here')

#        user1 = Atm('2932sdksjk',1234)
#
 #"""   print('choose an option')
  # print("1.Balance Enquriy 2.withdrawl")
   # activity = int(input("enter activity number "))
    #if (activity == 1):
     #   user1.check_balance()
  
    #elif(activity == 2):   
     #   amount = int(input("enter the amount"))
      #  user1.cash(amount)

   # else:
    #    print("bye bye have a bad day")

 #if __name__=="__main__":
  #  main()
