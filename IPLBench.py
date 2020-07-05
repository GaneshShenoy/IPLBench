class IPL:

    
    def __init__(self, max_num_vertexes = 70):
        self.PlayerTeam = []
        self.edges = [[0] * max_num_vertexes for _ in range(max_num_vertexes)]    
        self.num_of_vertex = 0
        self.file_output = open("outputPS10.txt", "a")
        
    def __del__(self): 
        self.file_output.close()
        
    def add_vertex(self, vertex):                                   
        if vertex not in self.PlayerTeam: 
            self.PlayerTeam.append(vertex)
            self.num_of_vertex += 1
            
    def get_vertex_index(self, key):
        return self.PlayerTeam.index(key)
        
    def add_edge(self, from_key, to_key):       
        #self.add_vertex(from_key) # this keey is already added.
        self.add_vertex(to_key)
        self.edges[self.get_vertex_index(from_key)][self.get_vertex_index(to_key)] = 1      
        
    def readInputfile(self, inputfile = "inputPS10.txt"):       
        with open(inputfile) as input_file_reader:
            line = input_file_reader.readline()
            while line != '':
                player_team = [team.strip() for team in line.split('/')]
                
                # add the first key to the vertex so that we avoid search and insert for this key.
                self.add_vertex(player_team[0])
                for item in player_team[1:]:  
                    self.add_edge (player_team[0], item)             
                
                line = input_file_reader.readline()
            input_file_reader.close()      
    
    def displayAll(self):
        list_franchise= []
        list_players = []
        found_franchise = 0
        num_of_franchise = 0
        num_of_players = 0
        
        for i in range(self.num_of_vertex):
            found_player = 0
            for j in range(self.num_of_vertex):
                if (self.edges[i][j] != 0):
                    list_players.append(self.PlayerTeam[j])
                    found_player = 1
                    num_of_players += 1
            if (found_player):
                list_franchise.append(self.PlayerTeam[i])
                num_of_franchise += 1
         
        print ("--------Function displayAll--------")
        print ("Total no. of franchises: ", num_of_franchise)
        print ("Total no. of players: ", num_of_players)
        
        print ("\nList of Franchises:")
        print (*list_franchise, sep ="\n")
        
        print ("\nList of players:")
        print (*list_players, sep ="\n")
        print ("-----------------------------------")
        
        
    def displayFranchises(self, player):    
        franchise_list = []
        
        # get the index for the player
        player_index = self.get_vertex_index(player)
        
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                if (self.edges[i][j] != 0 and j == player_index):
                    if self.PlayerTeam[i] not in franchise_list: 
                        franchise_list.append(self.PlayerTeam[i])
        
        print("--------Function displayFranchises --------")
        print("Player name: {0}".format(player))
        print("List of Franchises:")
        print (*franchise_list, sep ="\n")
        print("-------------------------------------------")
        
    def displayPlayers(self, franchise):
        players_list = []
        
        # get the index for the player
        player_index = self.get_vertex_index(franchise)
        
        
        for j in range(self.num_of_vertex):
            if (self.edges[player_index][j] != 0):
                if self.PlayerTeam[j] not in players_list: 
                    players_list.append(self.PlayerTeam[j])
        
        print("--------Function displayPlayers --------")
        print("Franchise name: {0}".format(franchise))
        print("List of players:")
        print (*players_list, sep ="\n")
        print("----------------------------------------")
    
    def printMatrix(self, franchise):     
        print ("\n***********************")
        print (self.num_of_vertex)
        print ("***********************")
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                print(self.edges[i][j], end=' ')
            print()
            
    def getTeamIndexForPlayers(self, playerA, playerB):
        player_a_index = self.get_vertex_index(playerA)
        player_b_index = self.get_vertex_index(playerB)
        
        # considering player in maximum 2 teams
        playerA_teams = [None]*2
        playerB_teams = [None]*2
        for i in range(self.num_of_vertex):
            if (self.edges[i][player_a_index]):
                if (playerA_teams[0] == None) :
                    playerA_teams[0] = i
                else :
                    playerA_teams[1] = i
            if (self.edges[i][player_b_index]):
                if (playerB_teams[0] == None) :
                    playerB_teams[0] = i
                else :
                    playerB_teams[1] = i
        return playerA_teams, playerB_teams
        
    def franchiseBuddies(self, playerA, playerB):
        # Get the index of both the players
        # traverse through the column see where both the players have value 1
        # get that index and that is the index where they are in the same team
        player_a_index = self.get_vertex_index(playerA)
        player_b_index = self.get_vertex_index(playerB)
        count = 0;
        team_buddy = []
        for i in range(self.num_of_vertex):
            if (self.edges[i][player_a_index] and self.edges[i][player_b_index]):
                team_buddy.append(self.PlayerTeam[i])
                count += 1              
        
        print("--------Function franchiseBuddies --------")
        print("Player A: {0}".format(playerA))
        print("Player B: {0}".format(playerB))
        if (count):
            print ("Franchise Buddies: Yes, ", *team_buddy)
        else:
            print ("They never playered together")
        print("------------------------------------------")
         
    def findPlayerConnect(self, playerA, playerB):
        # Find which team the player belongs to for both the players
        # loop through both the team and find where both the values are 1
        playerA_teams, playerB_teams = self.getTeamIndexForPlayers(playerA, playerB)      
        found_player = False;
        
        print ("--------Function findPlayerConnect --------")
        print ("Player A: {0}".format(playerA))
        print ("Player B: {0}".format(playerB))
        for player_a in range (2) :
            if (playerA_teams[player_a] == None): 
                continue
            
            for player_b in range(2) :
                if (playerB_teams[player_b] == None): 
                    continue
                
                for edge in range(self.num_of_vertex):
                    if (self.edges[playerA_teams[player_a]][edge] and self.edges[playerB_teams[player_b]][edge]):                       
                        print ('Related: Yes, {0} > {1} > {2} > {3} > {4}'.format(playerA, self.PlayerTeam[playerA_teams[player_a]], self.PlayerTeam[edge], self.PlayerTeam[playerB_teams[player_b]], playerB))
                        found_player = True

        if (False == found_player):
            print ("No common player found between planyers {0} and {1}".format(playerA, playerB))
            
        print ("-------------------------------------------")
        
if __name__ == "__main__":
    iplBench = IPL()
    iplBench.readInputfile()
    iplBench.displayAll()
    iplBench.displayFranchises("Andrew Tye")
    iplBench.displayPlayers("KKR")
    iplBench.franchiseBuddies("Krunal Pandya", "Ishan Kishan" )
    iplBench.findPlayerConnect("Kedar Jadhav", "Ishan Kishan")
    print('ALL IPL bench functionalities are executed')
    