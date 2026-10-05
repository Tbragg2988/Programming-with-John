print("Car checker: are you safe to drive?")

""" 
The car may only drive if:
  1. ALL doors (and the boot) are closed.
  2. EVERY seat that has a person in it has its seatbelt fastened.

  so sensors check if doors x4 closed, bums in seats x 4 and if there is a bum in seat that there is a seatbelt fastened

"""
frontDriverD = True
frontPassD = True
rearDriverD = True
rearPassD = False

doorSecure = frontDriverD and frontPassD and rearDriverD and rearPassD 

fDriverS = True
fPassS = False
rDriverS = False
rPassS = False

SeatActive = fDriverS and fPassS and rDriverS and rPassS

# no point checking the belt sensor if there is no bum in seat.
if doorSecure and SeatActive == False:

    if doorSecure == False:
        print("check doors")
        if frontDriverD == False:
            print("Front driver side door is open")
        if frontPassD == False:
            print("Front passenger side door is open")
        if frontDriverD == False:
            print("Rear driver side door is open")
        else:
            print("Rear passenger side door is open")

    if SeatActive == False:
