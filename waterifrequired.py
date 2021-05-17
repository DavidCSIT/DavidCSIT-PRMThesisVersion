#!/usr/bin/env python3
import rainmaker    #supporting functions
import config       #import configuration variables

def water_if_required() :
    #get current moisture 
    soil_moisture = rainmaker.measure_moisture()
    
    #get latest forecast
    forecasts = rainmaker.get_forecast()
        
    if soil_moisture <= config.SOIL_STRESS_POINT :  #water now
        rainmaker.log_and_notify(f"Watering Started- Soil at stress point - soil moisture {soil_moisture}")
        rainmaker.open_valve(config.WATERING_TIME)
    elif soil_moisture <= config.SOIL_AT_RISK_LEVEL1:   #check 12hr forecast water if required
        if sum(forecasts[:13]) < config.RAIN_FORECAST_12HRS_MIN:
            rainmaker.log_and_notify(f"Watering Started- Soil at risk level 1 moisture {soil_moisture}")
            rainmaker.open_valve(config.WATERING_TIME)
        else:
            rainmaker.log_and_notify(f"Watering Delayed- Soil at risk level 1 rain forecast moisture {soil_moisture}")
    elif soil_moisture <= config.SOIL_AT_RISK_LEVEL2:  #check 48hr forecast water if required
        if sum(forecasts[:]) < config.RAIN_FORECAST_48HRS_MIN:
            rainmaker.log_and_notify(f"Watering Started- Soil at risk level 2 moisture {soil_moisture}")
            rainmaker.open_valve(config.WATERING_TIME)
        else:
            rainmaker.log_and_notify(f"Watering Delayed- Soil at risk level 2 moisture rain forecast moisture {soil_moisture}")
    else:    #no watering required
        rainmaker.log_and_notify(f"Watering Not required- Moisture {soil_moisture}")

water_if_required()    

  

        