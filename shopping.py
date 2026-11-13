valid = False
while not valid:
    try:
        bill = float(input("bill amount: "))
        discount = float(input("discount percent: "))
        people = int(input("number of people: "))
        discount_amount = bill * discount / 100
        final_bill = bill - discount_amount
        each = final_bill / people
    except ValueError:
        print("please type numbers only.")
    except ZeroDivisionError:
        print("people cannot be 0.")
    else:
        print("final bill:", final_bill)
        print("each person pays:", each)
        valid = True
    finally:
        print("finished")
