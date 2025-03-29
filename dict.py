

bid_mem = {
    "dimpu": "350",
    "sam" : "200"
}

name = str(input("Enter your name: "))
bid_amt = int(input("Enter your bid amount: "))

bid_mem(key = name, value= bid_amt).append(bid_mem)
print(bid_mem)
