# import time

class AlarmClock:
    '''Alarm Clock class'''

    def __init__(self, time, alarm = "OFF"):
        self.time = self.validate_time(time)
        self.alarm = alarm
        self.history = list()
        self.count = 0
        print(f"Create new clock: time - {self.time}, alarm - {self.alarm}")

    @staticmethod
    def validate_time(x):
        if not isinstance(x, str):
            raise TypeError(r"You must insert time as %%:%% format")
        
        return x
    
    def set_time(self, time):
        self.time = self.validate_time(time)
        print(f"Set new time {self.time}")

    def set_alarm(self, alarm):
        self.alarm = self.validate_time(alarm)
        print(f"Set new alarm {self.alarm}")

    def check_alarm(self):
        if self.alarm != self.time:
            print(f"You can sleep")
        else:
            print(f"Wake up!")
            self.count += 1
            self.history.append(
                {
                    'Count' : self.count,
                    "Alarm time" : self.alarm
                }
            )

    
    def set_snooze(self, snooze : int):
        # 1
        # hours = int(self.alarm.split(":")[0])
        # minutes = int(self.alarm.split(":")[1])
        # 2
        # print(self.alarm.split(":")) => ["08", "00"] if time is "08:00"
        hours, minutes = map(int, self.alarm.split(":")) # ["08", "00"] => hours = 8, minutes = 0 
        minutes += snooze
        # 04:31, +30(0) => 05:01
        # 61 min
        if minutes >= 60:
            hours += minutes // 60
            minutes = minutes % 60
        # 23:59, +40 => 00:39
        if hours >= 24:
            hours = hours % 24
        
        # 04:31, +30(0) => 05:1
        self.alarm = str(hours).zfill(2) + ":" + str(minutes).zfill(2) # 05:01, if zfill(5) => 05:00001
        print(f"New alarm after snooze is {self.alarm}")


    def get_stats(self):
        for record in self.history:
            print(record)

clock = AlarmClock("00:00")
clock.set_time("15:26")
clock.set_alarm("14:30")
clock.check_alarm()
clock.set_snooze(56)
clock.check_alarm()
