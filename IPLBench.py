class IPL:

    
    def __init__(self, max_num_vertexes = 70):
        self.PlayerTeam = []
        self.edges = [[0] * max_num_vertexes for _ in range(max_num_vertexes)]    
        self.num_of_vertex = 0
    
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
        print ("--------Function displayFranchises --------")
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
            
            
        print ("Total no. of franchises: ", num_of_franchise)
        print ("Total no. of players: ", num_of_players)
        
        print ("\nList of Franchises")
        print (*list_franchise, sep ="\n")
        
        print ("\nList of players")
        print (*list_players, sep ="\n")
        
    def displayFranchises(self, player):    
        franchise_list = []
        
        # get the index for the player
        player_index = self.get_vertex_index(player)
        
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                if (self.edges[i][j] != 0 and j == player_index):
                    if self.PlayerTeam[i] not in franchise_list: 
                        franchise_list.append(self.PlayerTeam[i])
        
        print("\n--------Function displayFranchises --------")
        print (*franchise_list, sep ="\n")
        
    def displayPlayers(self, franchise):
        players_list = []
        
        # get the index for the player
        player_index = self.get_vertex_index(franchise)
        
        
        for j in range(self.num_of_vertex):
            if (self.edges[player_index][j] != 0):
                if self.PlayerTeam[j] not in players_list: 
                    players_list.append(self.PlayerTeam[j])
        
        print("\n--------Function displayPlayers --------")
        print (*players_list, sep ="\n")
        
    
    def printMatrix(self, franchise):     
        print ("\n***********************")
        print (self.num_of_vertex)
        print ("***********************")
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                print(self.edges[i][j], end=' ')
            print()
        
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
               
        print("\n--------Function franchiseBuddies --------")
        print ("Player A: ", playerA)
        print ("Player B: ", playerB)
        if (count):
            print ("Franchise Buddies: Yes, ", *team_buddy)
        else:
            print ("They never playered together")
        
    def findPlayerConnect(self, playerA, playerB):
        pass
        
if __name__ == "__main__":
    iplBench = IPL()
    iplBench.readInputfile()
    iplBench.displayAll()
    iplBench.displayFranchises("Andrew Tye")
    iplBench.displayPlayers("KKR")
    iplBench.franchiseBuddies("Krunal Pandya", "Ishan Kishan" )
    iplBench.findPlayerConnect(None, None)
    print('ALL IPL bench functionalities are executed')
    