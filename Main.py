#CONVERT DMS TO DD
def dms_to_dd(Degrees,Minutes,Seconds):
    return Degrees + (Minutes/60) + (Seconds/3600)

def DD_to_DMS(DecimalDegrees):
   Degrees = int(DecimalDegrees)
   Minutes = int((DecimalDegrees - Degrees) * 60)
   Seconds = (DecimalDegrees - Degrees - (Minutes/60)) * 3600
   return Degrees, Minutes, Seconds

