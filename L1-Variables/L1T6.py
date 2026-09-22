print("Hello let me help you convert mpg to kilometers.")

mpg_one_s = input("Enter the MPG:  ")
mpg_num = float(mpg_one_s)

km_num = (mpg_num*1.609)/3.785
km_num = round(km_num, 2)
print("The km/l of", mpg_one_s, "equals:", km_num)