class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.channel = 1
        self.price = price
        self.inches = inches
        self.on_off_status = False  # Initially, the TV is off
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, new_channel):
        if 1 <= new_channel <= 50:
            self.channel = new_channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        on_off = "on" if self.on_off_status else "off"
        return f"{self.brand} TV is {on_off} at channel {self.channel}, volume {self.volume}"

# Function to interact with the user
def main():
    brand = input("Enter the brand of the TV: ")
    price = float(input("Enter the price of the TV: "))
    inches = int(input("Enter the size of the TV (in inches): "))

    tv = TV(brand, price, inches)
    
    while True:
        print("\nOptions:")
        print("1. Turn TV On/Off")
        print("2. Increase Volume")
        print("3. Decrease Volume")
        print("4. Set Channel")
        print("5. Reset TV")
        print("6. Show Status")
        print("7. Exit")
        
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            tv.on_off_status = not tv.on_off_status
            print("TV turned on" if tv.on_off_status else "TV turned off")
        elif choice == 2:
            tv.increase_volume()
        elif choice == 3:
            tv.decrease_volume()
        elif choice == 4:
            new_channel = int(input("Enter the new channel (1-50): "))
            tv.set_channel(new_channel)
        elif choice == 5:
            tv.reset_tv()
        elif choice == 6:
            print(tv.status())
        elif choice == 7:
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

