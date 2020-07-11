'''
IPL class solves the IPL bench for Auctioning the players for the teams.
The diagraph is considered for the solution
The below logic is considered for explaining the solution considering below example
TEAM1   A   B   C
TEAM2   L   M   N
TEAM3   C   Q   L 

------------------------------------------------------------------------------------------------------------------------------------------------
        | TEAM1 |   A   |   B   |   C   | TEAM2 |   L   |   M   |   N   | TEAM3 |   Q   |      |      |       |       |      |      |       | 
------------------------------------------------------------------------------------------------------------------------------------------------
 TEAM1  |       |   1   |   1   |   1   |       |       |       |       |       |       |      |      |       |       |      |      |       | 
 ------------------------------------------------------------------------------------------------------------------------------------------------
 A      |       |       |       |       |       |       |       |       |       |       |      |      |       |       |      |      |       | 
 ------------------------------------------------------------------------------------------------------------------------------------------------
 B      |       |       |       |       |       |       |       |       |       |       |      |      |       |       |      |      |       | 
 ------------------------------------------------------------------------------------------------------------------------------------------------
 C      |       |       |       |       |       |       |       |       |       |       |      |      |       |       |      |      |       | 
 ------------------------------------------------------------------------------------------------------------------------------------------------
 TEAM2  |       |       |       |       |       |   1   |   1   |   1   |       |       |      |      |       |       |      |      |       | 
 ------------------------------------------------------------------------------------------------------------------------------------------------
 L      |       |       |       |       |       |       |       |       |       |       |      |      |       |       |      |      |       | 
 ------------------------------------------------------------------------------------------------------------------------------------------------
 M      |       |       |       |       |       |       |       |       |       |       |      |      |       |       |      |      |       | 
 ------------------------------------------------------------------------------------------------------------------------------------------------
 N      |       |       |       |       |       |       |       |       |       |       |      |      |       |       |      |      |       | 
 ------------------------------------------------------------------------------------------------------------------------------------------------
 TEAM3  |       |       |       |   1   |       |   1   |       |       |       |   1   |      |      |       |       |      |      |       | 
 ------------------------------------------------------------------------------------------------------------------------------------------------
 Q      |       |       |       |       |       |       |       |       |       |       |      |      |       |       |      |      |       | 
 ------------------------------------------------------------------------------------------------------------------------------------------------

'''
class IPL:

    '''
    This funciton intialize the member variables of the the IPL class 
    '''
    def __init__(self, max_num_vertexes = 90):
        
        self.PlayerTeam =  []                                                     # Unique team name and the player names
        self.edges = [[0] * max_num_vertexes for _ in range(max_num_vertexes)]    # Matrix to store directed edges (association)
        self.num_of_vertex = 0                                                    # Number of the vertexes
        self.file_output = open("outputPS10.txt", "w")                            # File creation for output of execution
    
    '''
    distruction of the class
    '''
    def __del__(self): 
        self.file_output.close()
        
    '''
    Add the vertex to the array
    Also counts the number of vertex added to the array
    '''
    def add_vertex(self, vertex):                                   
        if vertex not in self.PlayerTeam: 
            self.PlayerTeam.append(vertex)
            self.num_of_vertex += 1
            
    '''
    Returns index of the vertex for the given name
    '''
    def get_vertex_index(self, key):
        return self.PlayerTeam.index(key)
       
    '''
    Add edges to the double dimension array
    '''
    def add_edge(self, from_key, to_key):       
        #self.add_vertex(from_key) # this keey is already added.
        self.add_vertex(to_key)
        self.edges[self.get_vertex_index(from_key)][self.get_vertex_index(to_key)] = 1

    '''
    Read the input file for the data of team and players
    By default the input file name is inputPS10.txt
    '''
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
    
    '''
    Read the prompts file for execution of defined function in with parameters
    By default the input file name is promptsPS10.txt
    ''' 
    def readPromptsfile(self, inputfile = "promptsPS10.txt"):
        with open(inputfile) as input_file_reader:
            line = input_file_reader.readline()
            while line != '':
                prompt = [prompts.strip() for prompts in line.split(':')]
              
                if (prompt[0] == "findFranchise"):                    
                    iplBench.displayFranchises(prompt[1])
                if (prompt[0] == "listPlayers"):                    
                    iplBench.displayPlayers(prompt[1])
                if (prompt[0] == "franchiseBuddies"):                    
                    iplBench.franchiseBuddies(prompt[1], prompt[2] )    
                if (prompt[0] == "playerConnect"):                    
                    iplBench.findPlayerConnect(prompt[1], prompt[2] )  
 
                line = input_file_reader.readline()
        input_file_reader.close()      
    
    '''
    Display all the parameters
    '''
    def displayAll(self):
        list_franchise= []
        list_players = []
        found_franchise = 0
        num_of_franchise = 0
        num_of_players = 0
        
        for i in range(self.num_of_vertex):
            found_player = 0
            for j in range(self.num_of_vertex):
                if self.edges[i][j] != 0:
                    found_player = 1
                    if self.PlayerTeam[j] not in list_players:
                        list_players.append(self.PlayerTeam[j])
                        num_of_players += 1
            if (found_player):
                list_franchise.append(self.PlayerTeam[i])
                num_of_franchise += 1
         
        self.file_output.write ("\n--------Function displayAll--------")
        self.file_output.write ("\nTotal no. of franchises: {0}".format(num_of_franchise))
        self.file_output.write ("\nTotal no. of players: {0}".format(num_of_players))        
        self.file_output.write ("\nList of Franchises:\n")
        self.file_output.write ('\n'.join(list_franchise))        
        self.file_output.write ("\n\nList of players:\n")
        self.file_output.write ('\n'.join(list_players))
        self.file_output.write ("\n-----------------------------------")
        
    '''
    Display all the franchises for the given player
    '''
    def displayFranchises(self, player):
        if player not in self.PlayerTeam:
            self.file_output.write ("\nPlayer {0} not in input file".format(player))
            return
        franchise_list = []
        
        # get the index for the player
        player_index = self.get_vertex_index(player)
        
        for i in range(self.num_of_vertex):
            if self.edges[i][player_index]:
                if self.PlayerTeam[i] not in franchise_list:
                    franchise_list.append(self.PlayerTeam[i])
                        
        self.file_output.write ("\n\n--------Function displayFranchises --------")
        self.file_output.write ("\nPlayer name: {0}".format(player))
        self.file_output.write ("\nList of Franchises:\n")
        self.file_output.write ('\n'.join(franchise_list))
        self.file_output.write ("\n-------------------------------------------")
        
    '''
    Display all the players for the given franchise
    '''
    def displayPlayers(self, franchise):
        players_list = []
        
        # get the index for the player
        franchise_index = self.get_vertex_index(franchise)
        
        
        for j in range(self.num_of_vertex):
            if (self.edges[franchise_index][j] != 0):
                if self.PlayerTeam[j] not in players_list: 
                    players_list.append(self.PlayerTeam[j])
        
        self.file_output.write ("\n\n--------Function displayPlayers --------")
        self.file_output.write ("\nFranchise name: {0}".format(franchise))
        self.file_output.write ("\nList of players:\n")
        self.file_output.write ('\n'.join(players_list))
        self.file_output.write ("\n-------------------------------------------")
            
    def printMatrix(self, franchise):     
        print ("\n***********************")
        print (self.num_of_vertex)
        print ("***********************")
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                print(self.edges[i][j], end=' ')
            print()
            
    '''
    Returns the team index value for the planyers from the edge table.
    Assumption: As per the given problem, one player can exist in maximum of two teams
    '''
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
        
    '''
    Check whether the players are in the same franchise
    '''
    def franchiseBuddies(self, playerA, playerB):
        if playerA not in self.PlayerTeam or playerB not in self.PlayerTeam:
            self.file_output.write ("\nPlayer(s) {0} {1} not in input file".format(playerA, playerB))
            return
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
        
        self.file_output.write ("\n\n--------Function franchiseBuddies --------")
        self.file_output.write ("\nPlayer A: {0}".format(playerA))
        self.file_output.write ("\nPlayer B: {0}".format(playerB))
        if (count):
            self.file_output.write ("\nFranchise Buddies: Yes, ")
            self.file_output.write ('\n'.join(team_buddy))
        else :
            self.file_output.write ("\nThey never playered together")
        self.file_output.write ("\n------------------------------------------")
         
    '''
    Check wether the players are connected based on other player who shares the two franchises.
    '''
    def findPlayerConnect(self, playerA, playerB):
        if playerA not in self.PlayerTeam or playerB not in self.PlayerTeam:
            self.file_output.write ("\nPlayer(s) {0} {1} not in input file".format(playerA, playerB))
            return
        # Find which team the player belongs to for both the players
        # loop through both the team and find where both the values are 1
        playerA_teams, playerB_teams = self.getTeamIndexForPlayers(playerA, playerB)      
        found_player = False;
        
        self.file_output.write  ("\n--------Function findPlayerConnect --------")
        self.file_output.write  ("\nPlayer A: {0}".format(playerA))
        self.file_output.write  ("\nPlayer B: {0}".format(playerB))
        
        '''
        # Player might be in maximum of two teams
        for player_a in range (2) :
            if (playerA_teams[player_a] == None): 
                continue
            
            # For each player, there might be two teams we can compare with.
            for player_b in range(2) :
                if (playerB_teams[player_b] == None): 
                    continue
                
                # If we find that the player shares both the team
                for edge in range(self.num_of_vertex):
                    if (self.edges[playerA_teams[player_a]][edge] and self.edges[playerB_teams[player_b]][edge]):                       
                        self.file_output.write  ('\nRelated: Yes, {0} > {1} > {2} > {3} > {4}'.format(playerA, self.PlayerTeam[playerA_teams[player_a]], 
                                                                                                      self.PlayerTeam[edge], self.PlayerTeam[playerB_teams[player_b]], playerB))
                        found_player = True
        '''
        for edge in range (self.num_of_vertex):
            
            if (playerA_teams[0] != None and playerA_teams[0] != None ): 
                if (self.edges[playerA_teams[0]][edge] and self.edges[playerB_teams[0]][edge]):
                    self.file_output.write  ('\nRelated: Yes, {0} > {1} > {2} > {3} > {4}'.format(playerA, self.PlayerTeam[playerA_teams[0]], 
                                                                                                      self.PlayerTeam[edge], self.PlayerTeam[playerB_teams[0]], playerB))
                    found_player = True
            if (playerA_teams[0] != None and playerA_teams[1] != None ): 
                if (self.edges[playerA_teams[0]][edge] and self.edges[playerB_teams[1]][edge]):
                    self.file_output.write  ('\nRelated: Yes, {0} > {1} > {2} > {3} > {4}'.format(playerA, self.PlayerTeam[playerA_teams[0]], 
                                                                                                      self.PlayerTeam[edge], self.PlayerTeam[playerB_teams[1]], playerB))
                    found_player = True                                                                                                            
           
            if (playerA_teams[1] != None and playerA_teams[0] != None ): 
                if (self.edges[playerA_teams[1]][edge] and self.edges[playerB_teams[0]][edge]):
                    self.file_output.write  ('\nRelated: Yes, {0} > {1} > {2} > {3} > {4}'.format(playerA, self.PlayerTeam[playerA_teams[1]], 
                                                                                                      self.PlayerTeam[edge], self.PlayerTeam[playerB_teams[0]], playerB))   
                    found_player = True                                                                                                      
            if (playerA_teams[1] != None and playerA_teams[1] != None ): 
                if (self.edges[playerA_teams[1]][edge] and self.edges[playerB_teams[1]][edge]):
                    self.file_output.write  ('\nRelated: Yes, {0} > {1} > {2} > {3} > {4}'.format(playerA, self.PlayerTeam[playerA_teams[1]], 
                                                                                                      self.PlayerTeam[edge], self.PlayerTeam[playerB_teams[1]], playerB)) 
                    found_player = True                                                                                                      
        
        if (False == found_player):
            self.file_output.write  ("\nNo common player found between planyers {0} and {1}".format(playerA, playerB))
            
        self.file_output.write  ("\n-------------------------------------------")
        
if __name__ == "__main__":
    iplBench = IPL()
    iplBench.readInputfile("inputPS10.txt")
    iplBench.readPromptsfile("promptsPS10.txt")
    iplBench.displayAll()
    
    '''
    iplBench.displayFranchises("Andrew Tye")
    iplBench.displayPlayers("KKR")
    iplBench.franchiseBuddies("Krunal Pandya", "Ishan Kishan" )
    iplBench.findPlayerConnect("Kedar Jadhav", "Ishan Kishan")
    '''