class Traveller:
    def __init__(self,name:str ,lastname:str,email:str,password:str):
        self.name=name
        self.lastname=lastname
        self.email=lastname
        self.password=password


    
    def __repr__(self):
        return (f"Traveller Name=(name={self.name}, lastname={self.lastname}, "
                f"email={self.email}, password={self.password}")
     
        