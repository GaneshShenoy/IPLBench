class IPL:
    def __init__(self):
        print("***** init function called ******")
    
    def readInputfile(self, inputfile):
        print("***** readInputfile function called ******")
        
    def displayAll(self):
        print("***** displayAll function called ******")
        
    def displayFranchises(self, player):
        print("***** displayFranchises function called ******")
    
    def displayPlayers(self, franchise):
        print("***** displayPlayers function called ******")
        
    def franchiseBuddies(self, playerA, playerB):
        print("***** franchiseBuddies function called ******")
    
    def findPlayerConnect(self, playerA, playerB):
        print("***** findPlayerConnect function called ******")
        
        
        
if __name__ == "__main__":
    iplBench = IPL()
    iplBench.readInputfile(None)
    iplBench.displayAll()
    iplBench.displayFranchises(None)
    iplBench.displayPlayers(None)
    iplBench.franchiseBuddies(None, None)
    iplBench.findPlayerConnect(None, None)
    print('ALL IPL bench functionalities are executed')
    