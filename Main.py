import numpy as np



#CONVERT DMS TO DD
def dms_to_dd(Degrees,Minutes,Seconds):
    return Degrees + (Minutes/60) + (Seconds/3600)

def DD_to_DMS(DecimalDegrees):
    """Convert Decimal Degree to Degree Minute Seconds"""
   Degrees = int(DecimalDegrees)
   Minutes = int((DecimalDegrees - Degrees) * 60)
   Seconds = (DecimalDegrees - Degrees - (Minutes/60)) * 3600
   return Degrees, Minutes, Seconds


    
def wgs84_to_gng(lat, lon):
        """Convert WGS84 coordinates to Ghana National Grid (feet)."""
        false_easting = 900000
        false_northing = 0
        scale_factor = 0.9996
        central_meridian = -1.0

  #numpy is imported as np and is used here to convert the lat and long to radians
        lat_rad = np.radians(lat)
        lon_rad = np.radians(lon - central_meridian)

    # The value 6378137 in the code represents the semi-major axis of the WGS84 ellipsoid, measured in meters
        easting = scale_factor * lon_rad * 6378137 + false_easting
        northing = scale_factor * lat_rad * 6378137 + false_northing
    # Here we convert the eastings and northings to feet by multipying by the constant 3.28084
        easting_ft = easting * 3.28084
        northing_ft = northing * 3.28084

        return easting_ft, northing_ft