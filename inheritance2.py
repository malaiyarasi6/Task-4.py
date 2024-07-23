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


class AdvancedTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Wide viewing angle"

    def backlight(self):
        return "LED backlight"

    def display_details(self):
        return (
            f"Brand: {self.brand}\n"
            f"Price: ${self.price}\n"
            f"Size: {self.inches} inches\n"
            f"Screen Thickness: {self.screen_thickness} cm\n"
            f"Energy Usage: {self.energy_usage} kWh/year\n"
            f"Lifespan: {self.lifespan} hours\n"
            f"Refresh Rate: {self.refresh_rate} Hz\n"
            f"Viewing Angle: {self.viewing_angle()}\n"
            f"Backlight: {self.backlight()}"
        )

# Example usage:
adv_tv = AdvancedTV(
    brand="Sony", 
    price=1200, 
    inches=65, 
    screen_thickness=5, 
    energy_usage=150, 
    lifespan=50000, 
    refresh_rate=120
)

print(adv_tv.status())  # Basic status
print(adv_tv.display_details())  # Detailed features
