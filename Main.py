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



def wgs84_to_gmg(lat, lon):
        """Convert WGS84 coordinates to Ghana Meter Grid (meters)."""
        false_easting = 500000
        false_northing = 0
        scale_factor = 1.0
        central_meridian = -1.0

        lat_rad = np.radians(lat)
        lon_rad = np.radians(lon - central_meridian)

    #The value 6378137 in the code represents the semi-major axis of the WGS84 ellipsoid, measured in meters
        easting = scale_factor * lon_rad * 6378137 + false_easting
        northing = scale_factor * lat_rad * 6378137 + false_northing

        return easting, northing

def gmg_to_wgs84(easting, northing):
        """Convert Ghana Meter Grid (meters) to WGS84 coordinates."""
        false_easting = 500000
        false_northing = 0
        scale_factor = 1.0
        central_meridian = -1.0
    #The value 6378137 in the code represents the semi-major axis of the WGS84 ellipsoid, measured in meters
        lon_rad = (easting - false_easting) / (scale_factor * 6378137)
        lat_rad = (northing - false_northing) / (scale_factor * 6378137)

        lat = np.degrees(lat_rad)
        lon = np.degrees(lon_rad) + central_meridian

        return lat, lon






def gng_to_wgs84(easting_ft, northing_ft):
        """Convert Ghana National Grid (feet) to WGS84 coordinates."""
        false_easting = 900000
        false_northing = 0
        scale_factor = 0.9996
        central_meridian = -1.0
    #   Here we divide by the constant 3.28084 to change from feet to meters
        easting = easting_ft / 3.28084
        northing = northing_ft / 3.28084
    # Here convert from GNG to WGS84
    #The value 6378137 in the code represents the semi-major axis of the WGS84 ellipsoid, measured in meters
        lon_rad = (easting - false_easting) / (scale_factor * 6378137)
        lat_rad = (northing - false_northing) / (scale_factor * 6378137)
   # here we use numpy which was imported as np to convert degrees to radians
        lat = np.degrees(lat_rad)
        lon = np.degrees(lon_rad) + central_meridian

        return lat, lon






    #The function first checks if the user chose "WGS84 to GNG" from the menu.
    #It reads the Latitude and Longitude in Degrees, Minutes, and Seconds from the input boxes (like wgs84_lat_deg_entry.get())
def convert_coordinates():
    try:
        print("Choose Conversion Type:")
        print("1. WGS84 to GNG")
        print("2. GNG to WGS84")
        print("3. WGS84 to GMG")
        print("4. GMG to WGS84")

        choice = input("Enter option number (1-4): ")

        # ---------------- WGS84 TO GNG ----------------
        if choice == "1":
            lat_deg = float(input("Latitude Degrees: "))
            lat_min = float(input("Latitude Minutes: "))
            lat_sec = float(input("Latitude Seconds: "))
            lon_deg = float(input("Longitude Degrees: "))
            lon_min = float(input("Longitude Minutes: "))
            lon_sec = float(input("Longitude Seconds: "))

            lat = dms_to_dd(lat_deg, lat_min, lat_sec)
            lon = dms_to_dd(lon_deg, lon_min, lon_sec)

            easting_ft, northing_ft = wgs84_to_gng(lat, lon)

            print(f"Easting (ft): {easting_ft:.2f}")
            print(f"Northing (ft): {northing_ft:.2f}")

        # ---------------- GNG TO WGS84 ----------------
        elif choice == "2":
            easting_ft = float(input("Easting (ft): "))
            northing_ft = float(input("Northing (ft): "))

            lat, lon = gng_to_wgs84(easting_ft, northing_ft)

            lat_deg, lat_min, lat_sec = decimal_to_dms(lat)
            lon_deg, lon_min, lon_sec = decimal_to_dms(lon)

            print("Latitude (DMS):", int(lat_deg), int(lat_min), f"{lat_sec:.2f}")
            print("Longitude (DMS):", int(lon_deg), int(lon_min), f"{lon_sec:.2f}")

        # ---------------- WGS84 TO GMG ----------------
        elif choice == "3":
            lat_deg = float(input("Latitude Degrees: "))
            lat_min = float(input("Latitude Minutes: "))
            lat_sec = float(input("Latitude Seconds: "))
            lon_deg = float(input("Longitude Degrees: "))
            lon_min = float(input("Longitude Minutes: "))
            lon_sec = float(input("Longitude Seconds: "))

            lat = dms_to_dd(lat_deg, lat_min, lat_sec)
            lon = dms_to_dd(lon_deg, lon_min, lon_sec)

            easting, northing = wgs84_to_gmg(lat, lon)

            print(f"Easting: {easting:.2f}")
            print(f"Northing: {northing:.2f}")

        # ---------------- GMG TO WGS84 ----------------
        elif choice == "4":
            easting = float(input("Easting: "))
            northing = float(input("Northing: "))

            lat, lon = gmg_to_wgs84(easting, northing)

            lat_deg, lat_min, lat_sec = decimal_to_dms(lat)
            lon_deg, lon_min, lon_sec = decimal_to_dms(lon)

            print("Latitude (DMS):", int(lat_deg), int(lat_min), f"{lat_sec:.2f}")
            print("Longitude (DMS):", int(lon_deg), int(lon_min), f"{lon_sec:.2f}")

        else:
            print("Invalid option selected.")

    except ValueError:
        print("Input Error: Please enter valid numeric values.")