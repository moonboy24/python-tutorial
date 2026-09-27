
# Abstraction means to hide the details - abstractmethod used to inherit all the methods to run and needed to be done

from abc import ABC , abstractmethod

class manager(ABC):
    
    @abstractmethod
    def login(self):
        pass
    
    @abstractmethod
    def logout(self):
        pass
    
class emp(manager):
    
    def login(self):
        print("Login created")
        
    def logout(self):
        print("Logout Created")
        
emp1 = emp()
emp1.login()
emp1.logout()