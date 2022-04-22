name_db = []
volunteer_bln = []
volunteer_type = []
am_paid_bln = []
date_of_joining = []
ticket_purchase_id = [54321, 32134]
paid_fee = []
people_sponsored = []
spornsor_receipt_id = [86421, 97535]
sponsorer_message = []
def count_much(words, word_to_count):
    count = 0
    username_ass = []
    for word in words:
        if word == word_to_count:
            pos = words.index(word_to_count, count)
            count = count + 1
            username_ass.append(name_db[pos])
    return username_ass, count
def registration_mode():
    while True:
        first_last_name = input("Enter first and last name in the following format firstname_lastname: ")
        name_db.append(first_last_name)#volunteer checking
        while True:
                    vol_or_not = input("Do you wish to volunteer? y/n  ")
                    if vol_or_not == 'y':
                        volunteer_bln.append(vol_or_not)
                        type_vol = input("Please enter which area you want to volunteer: pier entrance gate [peir_gate] or gift shop [gift_shop] or painting/decorating [painting_decoration]   ")
                    else:
                        break
                    if type_vol == 'peir_gate':
                        volunteer_type.append(type_vol)
                        break
                    elif type_vol == 'gift_shop':
                        volunteer_type.append(type_vol)
                        break
                    elif type_vol == 'painting_decoration':
                        volunteer_type.append(type_vol)
                        break
                    elif type_vol != 'gift_shop' or 'peir_gate' or 'painting_decoration':
                        print("Error, choose correct option")
                        continue
    
                    elif vol_or_not == 'n':
                        volunteer_bln.append(vol_or_not)
                        break
                    elif vol_or_not != 'y' or 'n':
                        print('error please correctly choose y/n')
                        continue

        
        while True: #chec day
            day_ask = int(input("Enter day of entry: "))
            if day_ask not in range(1, 31):
                print("Error, please enter correct date")
                continue
            else:
                break
        
        
        while True: #check month
            month_ask = int(input("Enter month of entry: "))
            if month_ask not in range(1, 13):
                print("Error, please enter correct date")
                continue
            else:
                break
        
        while True: #check year
            year_ask = int(input("Enter year of entry: "))
            if year_ask < 2022:
                print("Error, please enter correct date")
                continue
            else:
                break
        
        final_date = f'D{day_ask}M{month_ask}Y{year_ask}' #compiling validated data
        date_of_joining.append(final_date) #add to database

        while True: #check payment, ticket id number
            ticket_id = int(input("Please enter the 5 digit code on your receipt you recieved upon paying the $75 fee (If you have not yet paid the fees then reply [0] )    "))
            if ticket_id == 0:
                print("Note that the fees for this account is not paid")
                paid_fee.append("not_paid")
                break
            try:
                validation_no = ticket_purchase_id.index(ticket_id)
                cnfrm = input(f"Are you sure you want to confirm the following receipt no. [{ticket_id}] with {first_last_name}   y/n  ")
                if cnfrm == 'y':
                    ticket_purchase_id.pop(validation_no)
                    print("Successfully claimed code")
                    paid_fee.append("Paid")
                    break
            except:
                print("Error: code not found try again")
        print("Account created")
        break

def data_insight():
    print(f"Members who have chosen to work as volunteers: {count_much(volunteer_bln, 'y')},")
    print(f"Peir Gate: {count_much(volunteer_type, 'peir_gate')} | Gift Shop: {count_much(volunteer_type, 'gift_shop')} | Paint and Decorating: {count_much(volunteer_type, 'painting_decoration')}")
    print(f"Members who has not paid: {count_much(paid_fee, 'not_paid')}")
def sponsor():
    while True:
        login_data = input("Please login with the user name you want to use to sponsor   ")
        try:
            name_db.index(login_data)
            break
        except:
            print("Please enter correct username")
            continue
    while True:
        message_of_sponsorer = input("Please enter the message you want to sponsor: (e to cancel)  ")
        if message_of_sponsorer == 'e':
            break
        sponsororno = int(input("To sponsor you need to enter the receipt id given to you when you paid the $200 fee [0] to cancel   "))
        if sponsororno == 0:
            print("Cancelled")
            break
        try:
            pos_of_code = spornsor_receipt_id.index(sponsororno)
            confrm = input(f"Id valid: Are you sure you want to claim id: {sponsororno} with {login_data} under the message {message_of_sponsorer} [y] [n]?  ")
            if confrm == 'y':
                spornsor_receipt_id.pop(pos_of_code)
                people_sponsored.append(login_data)
                sponsorer_message.append(message_of_sponsorer)
                print("Successfully claimed code, message has been saved")
                break
            elif confrm != 'y':
                print("Cancelled")
                break
        except ValueError:
            print("Sponsor id failed")
            continue

while True:
    choose_mode = input("To register enter [reg] to check data [ins] to sponsor a wooden plank [sponsor]")
    if choose_mode == 'reg':
        registration_mode()
        continue
    elif choose_mode == 'ins':
        data_insight()
        continue
    elif choose_mode == 'sponsor':
        sponsor()
        continue
    elif choose_mode != 'sponsor' or 'ins' or 'reg':
        print("Error; enter correct mode")
        continue