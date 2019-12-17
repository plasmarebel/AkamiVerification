from colorama import init, Fore, Back, Style
init(convert=True)

print(Fore.CYAN + "Welcome to Plasma's Akami Verification Script")

while True:
    print(Fore.WHITE + "Please select a site")
    print("1: Footpatrol\n2: Size\n3: Information\n4: Footsites\n5: Yeezy Supply")
    token = input("Enter a site: ")

    if token == "1":
        print(Fore.MAGENTA + "====== Footpatrol Cookie Validation ======")
        fpToken = input("Enter the _abck cookie: ")
        count = 0
        for c in fpToken:
            count += 1

        if count == 397:
            print(Fore.GREEN + "Valid Cookie")
        else:
            print(Fore.RED + "Invalid Cookie")

    elif token == "2":
        print("Not yet baby cakes")

    elif token == "3":
        print(Fore.MAGENTA + "====== Testing Area ======")
        fpToken = input("Enter the _abck cookie: ")
        count = 0
        for c in fpToken:
            count += 1
        print(Fore.YELLOW + "The cookie was " + str(count) + " characters long.")

    elif token == "4":
        print(Fore.MAGENTA + "====== Footsite Cookie Validation ======")
        footsiteToken = input("Enter the _abck cookie: ")
        if "~0~" in footsiteToken:
            print(Fore.GREEN + "Valid Cookie")
        else:
            print(Fore.RED + "Invalid Cookie")

    elif token == "5":
        print(Fore.MAGENTA + "====== Yeezy Supply Cookie Validation ======")
        ysToken = input("Enter the _abck cookie: ")
        if "==" in ysToken:
            print(Fore.GREEN + "Valid Cookie")
        else:
            print(Fore.RED + "Invalid Cookie")

    else:
        print("Site not supported")