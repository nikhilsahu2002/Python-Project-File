def dayOfProgrammer(year):
    if year %4==0 and year % 400 ==0:
        x = -245 + 256
        print(f"{x}.09.{year}")
    else :
        x= -244 + 256
        print(f"{x}.09.{year}")
    
dayOfProgrammer(1800)