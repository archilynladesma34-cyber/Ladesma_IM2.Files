def convert_usd(usd):
    """Convert USD to INR, GBP, and CNY"""
    return usd * 88.22, usd * 0.74, usd * 7.12

while True:
    s = input("Enter dollar ($) (* to exit): ")
    if s == "*":
        print("Bye")
        break

    # Split multiple inputs with '@'
    amounts = s.split("@")

    # Print header once
    print(f"{'Dollar ($)':<12}{'Indian Rupee (R)':<20}{'British Pound (£)':<20}{'Chinese Yuan (¥)'}")

    # Convert and print each amount
    for amt in amounts:
        try:
            usd = float(amt)
            inr, gbp, cny = convert_usd(usd)
            print(f"{usd:<12.2f}{inr:<20.2f}{gbp:<20.2f}{cny:.2f}")
        except:
            print(f"Invalid input: {amt}")
