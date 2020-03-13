class Time():
    def __init__(self, hours, minutes, seconds):
        self._hours = 0
        self._minutes = 0
        self._seconds = 0 
        
        def set_hours(value):
            if self._hours < 0:
                self._hours = 0
            elif hours > 23:
                self._hours = 23
            else:
                self._hours = hours           
        
        def get_hours(self):
            return self._hours
                
        def set_minutes(self, value):
            if minutes < 0:
                self._minutes = 0
            elif minutes > 59:
                self._minutes = 59
            else:
                self._minutes = minutes
                
        def get_minutes(self, _minutes):
            return self._minutes
        
        def set_seconds(self, value):
            if seconds < 0:
                self._seconds = 0
            elif seconds > 59:
                self._seconds = 59
            else:
                self._seconds = seconds            
        
        def get_seconds(self):
            return self._seconds       
        
    
    def display(self):
        print("{}:{}:{}".format(self._hours, self._minutes, self._seconds))
        
        
def main():
    new_time = Time(3, 5, 8)
    _hours = new_time.set_hours(input("Enter hours: "))
    _minutes = new_time.set_minutes(input("Enter minutes: "))
    _seconds = new_time.set_seconds(input("Enter seconds: "))
    new_time.display(_hours, _minutes, _seconds)
        
        
if __name__ == "__main__":
    main()