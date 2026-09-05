stock={
    "AAPL":180, "TSLA":250,"MSFT":400,"GOOGL":170,"AMZN":190,"META":500,"NVDA":120,"NFLX":700
    }
total_sum=0
print("=======================================")
print("               STOCK PORTFOLIO TRACKER              ")
print("=======================================")
while(True):
    product=(input("Enter stock:")).upper()
    quantity=int(input("Enter quantity:"))
    check=stock.get(product)
    if(check==None):
        print("Stock is not avalible")
        repeat=(input("Do you want to add another stock?")).upper()
        if(repeat=="NO"):
            break
    else:
        investment=check*quantity
        total_sum=total_sum+investment
        print(product,"Investment =₹",investment)
        repeat1=(input("Do you want to add another stock?")).upper()
        if(repeat1=="NO"):
            break
print("Total investment:₹",total_sum)
file=open("C:/Users/Mohd Azeem/investment.txt","a")
file.write("total investment:")
file.write(str(total_sum))
file.write("\n")
file.close()
        
    


    
