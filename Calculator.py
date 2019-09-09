from datetime import datetime,timedelta
now = datetime.now()
def calc_fun():
    print("What do you want to calculate?")
    print("1: When should I go to bed if i want to wake up at...")
    print("2.When should I get up?")
    n = int(input())
    if n==1:
        print("When do you want to wake up? [format(24hr) - HH:MM] ?")
        wtime = input()
        waking_time =  datetime.strptime(wtime, '%H:%M')
        print("To wake up feeling refreshed at {}, you need to sleep at the following times - ".format(wtime))
        for i in range(0,6):
            seconds_to_subtract = 900 +(6-i)*5400
            sleep_time = waking_time - timedelta(seconds=seconds_to_subtract)
            print(sleep_time.strftime('%H:%M'))
    if n==2:
        print("If you go to sleep right now, you must try to  wake up at one of these times - ")
        for i in range(0,6):
            seconds_to_add = 900 + (i+1)*5400
            awake_time = now + timedelta(seconds=seconds_to_add)
            print(awake_time.strftime('%H:%M'))
    print("Calculate again?")
    x = input("Enter 1 for yes and 0 for no:")
    if x !=0:
        calc_fun()

calc_fun()