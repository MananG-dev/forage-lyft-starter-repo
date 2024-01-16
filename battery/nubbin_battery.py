from battery.battery import battery
from utils import add_yearTodate


class NubbinBattery(battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def serviceNeed(self):
        serviceDate = add_yearTodate(self.last_service_date, 4)
        if serviceDate < self.current_date:
            return True
        else:
            return False