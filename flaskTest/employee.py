class Employee():
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def toJSON(self):
        # JSON 문법형식으로 보내줌
        return {"emp":{'firstName':self.firstName,
                        'lastName':self.lastName}}