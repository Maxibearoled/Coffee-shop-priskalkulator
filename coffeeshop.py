#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")
#Her gir jeg de ulike valgene Kaffi pris. Deretter lagde jeg en løkke som vil spørre programmet om og om igjen hvilke kaffi jeg vil ha hvis jeg skriver feil.


price = 0
def coffeelist():
   coffee = input("What type of coffee would you like?").lower()
   global price
   if coffee=="espresso":
      price = price + 2.50
   elif coffee=="americano":
      price = price + 3
   elif coffee=="latte":
      price = price + 2.50
   elif coffee=="cappuccino":
      price = price + 3
   elif coffee=="macchiato":
      price = price + 2.50
   elif coffee=="mocha":
      price = price + 3.50
   elif coffee=="flat white":
      price = price + 2.50
   else:
      print("Ugjyldig valg.")
      coffeelist()
coffeelist()

#Her spør jeg om de vil ha de ulike valgene av størrelse Medium , Large og Extra Large.
def sizelist():
   global price
   size = input("what size would you like?").lower()
   if size=="medium":
      price = price + 0
   elif size=="large":
      price = price + 1
   elif size=="xl":
      price = price + 1.50
   else:
      print("Ugjyldig valg.")
      sizelist()

sizelist()
   
#Her så gir jeg de valget om å ta med seg kaffien eller drikke den inne.
#Der etter lagde jeg en funksjon som får programmet til å stille spørsmål om hva de vil ha igjen med en løkke sånn at den ikke hopper over første steg ved feil skriving.
def takeaway():
   global price
   Takeaway = input("Would you like to sit inside or takeaway?").lower()
   if Takeaway=="inside":
      price = price + 0
   elif Takeaway=="takeaway":
      price = price + 1
   else:
      print("Ugjyldig valg.")
      takeaway()

takeaway()







#Complete the code here...
print("----------------------------")
print("Total Cost: £" + str(price))
