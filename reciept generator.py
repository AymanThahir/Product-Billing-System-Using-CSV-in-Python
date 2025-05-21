#reciept generator
import csv

def addProduct(pid,name,price):
    with open("products.csv",mode='a',newline='') as file:
        writer = csv.writer(file)
        data = [[pid,name,price]]
        writer.writerows(data)
        


def retriveProducts(pid):
    with open("products.csv",mode='r',newline='') as file:
        reader = csv.reader(file)
        dat = list(reader)
        found = 0
        for i in dat:
            if (i[0]==pid):
                return [i[0],i[1],i[2]]
                found = 1
        if(found == 0):
            return ("Not found")
        
bill = []
def billProducts():
    while True:
        epid = input("Enter pid(exit):")
        if(epid=='exit'):
            break
        temp = retriveProducts(epid)
        if(temp=="Not found"):
            print("Product not Found")
            continue
        qnt  = int(input("Enter Quantity: "))
        temp.append(qnt)
        bill.append(temp)

def printBill():
    final = []
    with open("bill.csv",mode='w',newline='') as file:
        writer = csv.writer(file)
        data = [['PID','Product_Name','Price','Quantity','Total']]
        writer.writerows(data)
        for i in bill:
            temp = (int(i[2])) * i[3]
            final.append(temp)
            data = [[i[0],i[1],i[2],i[3],temp]]
            writer.writerows(data)
        data = [['','','','TOTAL:',sum(final)]]
        writer.writerows(data)
        print("Bill Generated Succesfully")

if __name__=="__main__":
    
    while True:
        print(" ")
        print("S-Mart Shopping")
        print("Enter 1 for billing")
        print("Enter 2 for adding inventory")
        inp = (input("Enter: "))
        if(inp not in ('1','2')):
            print(" ")
            print("Enter 1 or 2")
            continue

        elif(inp=='2'):
            print("How many items would you like to add?")
            inc = int(input("Enter: "))
            for i in range(inc):
                tpid = input("Enter PID: ")
                tname = input("Enter Name: ")
                tprice = input("Enter Price: ")
                addProduct(tpid,tname,tprice)
                print("Item added")
            print("All Items Added")

        elif(inp=='1'):
            billProducts()
            printBill()




