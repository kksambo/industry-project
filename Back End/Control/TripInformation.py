class TripInformation:
    def __init__(self,transportationOptions:str,accommodation:str,weatherForecast:str,safetyTips:str):
        self.transportationOptions=transportationOptions
        self.accommodation=accommodation
        self.weatherForecast=weatherForecast
        self.safetyTips=safetyTips

    def __repr__(self):

            return  (f"Transportion Options=(option={self.transportationOptions}, Accomodation={self.accommodation}, "
                f"Weather Forecast={self.weatherForecast}, Safety Tips={self.safetyTips}")

        
