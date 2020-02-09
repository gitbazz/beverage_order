# Beverage Order (Coffee or Tea, I see). Prompt user to enter order information. The program will display the user's specific order along with the cost.


# Prompt user for order information and validate input
# Name
customerName = str(input("What is your name? "))

# Beverage Type
beverageType = input("Would you like to order coffee or tea? ").lower()
if beverageType not in ['coffee', 'c', 'tea', 't']:
    print("You entered an invalid beverage.")
    quit()

# Beverage size
beverageSize = input("What size beverage would you like (small, medium, large)? ").lower()
if beverageSize not in ['small', 's', 'medium', 'm', 'large', 'l']:
    print("You entered an invalid size.")
    quit()

# Additional flavour for coffee or tea
if beverageType in ['coffee', 'c']:
    coffeeFlavour = input("Would you like to add any additional flavours to your coffee (vanilla, chocolate, none)? ").lower()
    if coffeeFlavour not in ['vanilla', 'v', 'chocolate', 'c', 'none', '']:
        print("You entered an invalid flavour.")
        quit()
elif beverageType in ['tea', 't']:
    teaFlavour = input("Would you like to add any additional flavours to your tea (lemon, mint, none)? ").lower()
    if teaFlavour not in ['lemon', 'l', 'mint', 'm', 'none', '']:
        print("You entered an invalid flavour.")
        quit()


# Cost for specific beverage size and additional flavours
# Size
SMALL_COST = 1.50
MEDIUM_COST = 2.50
LARGE_COST = 3.25

# Coffee flavours
VANILLA_COST = 0.25
CHOCOLATE_COST = 0.75

# Tea flavours
LEMON_COST = 0.25
MINT_COST = 0.50

# Additional tax
TAX_PERCENT = 1.13


# Convert user input into variables to use for cost calculation
# Store appropriate beverage size and cost into variables
if beverageSize in ['small', 's']:
    dispensedSize = "small"
    sizeCost = SMALL_COST
elif beverageSize in ['medium', 'm']:
    dispensedSize = "medium"
    sizeCost = MEDIUM_COST
elif beverageSize in ['large', 'l']:
    dispensedSize = "large"
    sizeCost = LARGE_COST

# Store appropriate beverage flavour & cost into variables. Use these variables to compute the total cost of the ordered beverage
if beverageType in ['coffee', 'c']:
    if coffeeFlavour in ['vanilla', 'v']:
        dispensedCoffeeFlavour = "vanilla"
        coffeeFlavourCost = VANILLA_COST
    elif coffeeFlavour in ['chocolate', 'c']:
        dispensedCoffeeFlavour = "chocolate"
        coffeeFlavourCost = CHOCOLATE_COST
    elif coffeeFlavour in ['none', '']:
        dispensedCoffeeFlavour = "no flavouring"
        coffeeFlavourCost = 0
    totalCost = (sizeCost + coffeeFlavourCost)*TAX_PERCENT
    # Print customer output
    print("For " + customerName + " a " + dispensedSize + " coffee, " + dispensedCoffeeFlavour + ", cost: $%.2f" % (round(totalCost, 2)))
elif beverageType in ['tea', 't']:
    if teaFlavour in ['lemon', 'l']:
        dispensedTeaFlavour = "lemon"
        teaFlavourCost = LEMON_COST
    elif teaFlavour in ['mint', 'm']:
        dispensedTeaFlavour = "mint"
        teaFlavourCost = MINT_COST
    elif teaFlavour in ['none', '']:
        dispensedTeaFlavour = "no flavouring"
        teaFlavourCost = 0
    totalCost = (sizeCost + teaFlavourCost)*TAX_PERCENT
     # Print customer output
    print("For " + customerName + " a " + dispensedSize + " tea, " + dispensedTeaFlavour + ", cost: $%.2f" % (round(totalCost, 2)))
