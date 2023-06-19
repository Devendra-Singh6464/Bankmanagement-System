import mysql.connector
from datetime import date
con = mysql.connector.connect(
    host='localhost', user='root', password='', database='benkprodb')
cur = con.cursor()
dt = date.today()

print("Pres 1 TO Create Account-->")
print("Pres 2 To Withdraw Ammount-->")
print("Pres 3 To Deposit Ammount-->")
print("Pres 4 TO Fund Transfer-->")
print("Pres 5 TO Belence Check-->")
print("Pres 6 TO Pin Change-->")
print("Pres 7 TO Account Summery-->")


x = int(input("Select your Choice: "))
if (x == 1):
    q = "select * from account"
    cur.execute(q)
    ac = "SBI"
    x = 0
    for row in cur:
        x = x+1
        if x > 0:
            x = x+101
            ac = ac+str(x)
        else:
            ac = "SBI101"

    n = input("Enter your NAME: ")
    fn = input("Enter your FATHER NAME: ")
    em = input("Enter your EMAIL: ")
    ph = int(input("Enter your PHONE: "))
    p = input("Create PIN: ")
    s = input("Enter your STATE: ")
    c = input("Enter your CITY: ")
    am = input("Enter your AMOUNT: ")
    q = "insert into account values('"+ac+"','"+str(p)+"','"+n+"','" + \
        fn+"','"+em+"','"+str(ph)+"','"+s+"','"+str(c)+"','"+am+"')"
    cur.execute(q)
    con.commit()
    print("Account Open with account Number-- ", ac)


elif (x==2):
    ac = input("Enter Account Number: ")
    p = input("Enter Pin Number: ")
    q = "select * from account where acno ='"+ac+"' and pin='"+p+"'"
    cur.execute(q)
    x = 0
    camt = 0
    for row in cur:
        x = x+1
        camt = int(row[8])

    if x > 0:
        w = int(input("Enter Amount to withdraw: "))
        if camt >= w:
            camt = camt-w
            q = "update account set amount='"+str(camt)+"' where acno='"+ac+"'"
            cur.execute(q)
            con.commit()
            q = "insert into mytable(acno,amount,dt,ds)values('" + \
                ac+"','"+str(w)+"','"+str(dt)+"','withdraw')"
            cur.execute(q)
            con.commit()
            print("After Witdraw ", w, " Current blaance is = ", camt)
        else:
            print("Insufficient blaance")
    else:
        print("Invalid Account or Pin")


elif (x==3):
    ac = input("Enter your Account Number: ")
    p = input("Enter your Pin: ")
    q = "SELECT * FROM account WHERE acno = '"+ac+"' and pin='"+p+"'"
    cur.execute(q)
    x = 0
    camt = 0
    for row in cur:
        x = x+1
        camt = int(row[8])

    if x > 0:
        dp = int(input("Enter Amount to withdraw: "))
        camt = dp+camt
        q = "UPDATE account SET Amount='"+str(camt)+"' WHERE acno='"+ac+"'"
        cur.execute(q)
        con.commit()
        q = "insert into mytable(acno,amount,dt,ds)values('" + \
            ac+"','"+str(dp)+"','"+str(dt)+"','deposit')"
        cur.execute(q)
        con.commit()

        print("After Deposit", dp, " Cruent Amount = ", camt)
    else:
        print("Invalid account and Pin")


elif (x==4):
    ac = input("Enter Account Number: ")
    p = input("Enter Pin Number: ")
    q = "select * from account where acno ='"+ac+"' and pin='"+p+"'"
    cur.execute(q)
    x = 0
    camt = 0
    for row in cur:
        x = x+1
        camt = int(row[8])

    if x > 0:
        w = int(input("Enter Amount to withdraw: "))
        if camt >= w:
            tac = input("Enter Acount to Transfer:   ")
            q = "select * from account where acno='"+tac+"'"
            cur.execute(q)
            x1 = 0
            tamt = 0
            for row in cur:
                x1 = x1+1
                tamt = int(row[8])

            if x1 > 0:

                camt = camt-w
                tamt = tamt+w
                q = "update account set amount='" + \
                    str(camt)+"' where acno='"+ac+"'"
                cur.execute(q)
                con.commit()
                q = "update account set amount='" + \
                    str(tamt)+"' where acno='"+tac+"'"
                cur.execute(q)
                con.commit()
                q = "insert into mytable(acno,amount,dt,ds)values('" + \
                    ac+"','"+str(w)+"','"+str(dt)+"','Transfer')"
                cur.execute(q)
                con.commit()
                q = "insert into mytable(acno,amount,dt,ds)values('" + \
                    tac+"','"+str(w)+"','"+str(dt)+"','Recive')"
                cur.execute(q)
                con.commit()

                print("After Transfer ", w, " Current blaance is = ", camt)
            else:
                print("Invalid Benficiary Account")
        else:
            print("Insufficient blaance")
    else:
        print("Invalid Account or Pin")


elif (x == 5):
    ac = input("Enter your Account Number: ")
    p = input("Enter your Pin Number: ")
    t = "SELECT * FROM account WHERE acno ='"+ac+"' and pin='"+p+"'"
    cur.execute(t)
    x = 0
    camt = 0
    for row in cur:
        x = x+1
        camt = int(row[8])

    if x > 0:
        print("Your Balance is  = ", camt)
    else:
        print("Invalid Account Number and Pin")


elif (x == 6):
    ac = input("Enter your Account Number: ")
    p = input("Enter your Pin: ")
    d = "SELECT * FROM account WHERE acno = '"+ac+"' and pin='"+p+"'"
    cur.execute(d)
    x = 0
    for row in cur:
        x = x+1

    if x > 0:
        op = input("Enter your Change pin: ")
        np = input("Enter New Pin: ")
        u = "UPDATE account SET pin='"+np+"' WHERE acno='"+ac+"'"
        cur.execute(u)
        con.commit()
        print("After Change", op, "New Pin=", np)

    else:
        print("Worng Pin")


elif (x == 7):

    ac = input("Enter your Account Number: ")
    p = input("Enter your Pin: ")
    q = "SELECT * FROM account WHERE acno='"+ac+"' and pin='"+p+"'"
    cur.execute(q)

    x = 0
    for row in cur:
        x = x+1

    if x >= 0:

        i = "SELECT *FROM mytable WHERE acno='"+ac+"'"
        cur.execute(i)
        for row in cur:
            print(row[0], "\t", row[1], "\t",
                  row[2], "\t", row[3], "\t", row[4])

    else:
        print("Worng Account and Pin")


else:
    print("Choose the Correct Number")
