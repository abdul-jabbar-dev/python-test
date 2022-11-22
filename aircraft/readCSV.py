import csv


with open('./currency.csv', 'r') as files:
    lines = csv.reader(files)

    user = True

    userAns = input("Witch type currency you want: taka to dollar (ttd)/ dollar to taka (dtt) :")

    while (user ):
        cun = input("Enter currency code: ") 
        amo = input("Enter amount: ")

        for line in lines:
            if cun.lower() == line[1].lower():
                if userAns == 'dtt':
                    print(float(line[2])* float(amo))
                else:
                    print(float(line[3])* float(amo))
 
