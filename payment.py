TXT_1 = Select list payment
TXT_2 = Press 1 = Money
TXT_3 = Press 2 = PromptPay
TXT_4 = Press 3 = Bank
TXT_5 = Select number = 
TXT_6 = You have selected the payment method by ( MONEY ). Thank you for using the service.
TXT_7 = You have selected the payment method by ( PromptPay ). Thank you for using the service.
TXT_8 = You have selected the payment method by ( Bank ). Thank you for using the service.


def PAY_MENU() 
  SPACE_ = ' '
  print(TXT_1)
  print((SPACE_8),TXT_2)
  print((SPACE_8),TXT_3)
  print((SPACE_8),TXT_4)
  
def PAYMENT() 
  PAY_MENU()
  NUMBER = int(input(TXT_5))
  if NUMBER == 1 
    print(TXT_6)
  if NUMBER == 2 
    print(TXT_7)
  if NUMBER == 3 
    print(TXT_8)
  

if __name__ == '__main__'
  PAYMENT()