HEAD
def convert(usd):
    return usd * 88.22, usd * 0.74, usd * 7.12

while True:
    entered = input("Enter dollar ($) (* to exit): ")
    
    if entered.strip() == "*":
        print("bye")
        break
    
    amounts = entered.split("@")
    
    print(f"{'Dollar ($)':<12}{'Indian Rupee (R)':<20}{'British (Pound)':<20}{'China (Y)'}")
    
    for amt in amounts:
      if amt.isdigit():                      
        usd = int(amt)                    
        inr, gbp, cny = convert(usd)  
        print(f"{usd:<12}{inr:<20.2f}{gbp:<20.2f}{cny:.2f}")
    else:
        print()


def convert(usd):
    return usd * 88.22, usd * 0.74, usd * 7.12

while True:
    entered = input("Enter dollar ($) (* to exit): ")
    
    if entered.strip() == "*":
        print("bye")
        break
    
    amounts = entered.split("@")
    
    print(f"{'Dollar ($)':<12}{'Indian Rupee (R)':<20}{'British (Pound)':<20}{'China (Y)'}")
    
    for amt in amounts:
      if amt.isdigit():                      
        usd = int(amt)                    
        inr, gbp, cny = convert(usd)  
        print(f"{usd:<12}{inr:<20.2f}{gbp:<20.2f}{cny:.2f}")
    else:
        print()

9ac1ef3 (Updated convert.py and added dict.py)
