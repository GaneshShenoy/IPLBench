'''
IPL class solves the IPL bench for Auctioning the players for the teams.
Undirected graph is considered for the solution
'''
class IPL:

    '''
    This funciton intialize the member variables of the the IPL class 
    '''
    def __init__(self):
        
        self.file_output = open("outputPS10.txt", "w")                            # File creation for output of execution
        self.PlayerTeam  = list()
        self.edges       = dict()
        
        self.pred =[]
        self.dist =[]
        
    '''
    distruction of the class
    '''
    def __del__(self): 
        self.file_output.close()
        
    def insert_data(self, from_key, to_key):
        if not (from_key in self.PlayerTeam):
            self.PlayerTeam.append(from_key)
            self.edges[from_key]=list()
        if not (to_key in self.PlayerTeam):
            self.PlayerTeam.append(to_key)
            self.edges[to_key]=list()
        self.edges[from_key].append(to_key)
        self.edges[to_key].append(from_key)


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
                for item in player_team[1:]:  
                    self.insert_data(player_team[0], item)
                
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
        
    def displayPlayers(self, franchise):
        self.file_output.write ("\n\n--------Function displayPlayers --------")
        self.file_output.write ("\nFranchise name: {0}".format(franchise))
        self.file_output.write ("\nList of players:\n")
        self.file_output.write ('\n'.join(self.edges[franchise]))
        self.file_output.write ("\n-------------------------------------------")
    
    '''
    Display all the franchises for the given player
    '''
    def displayFranchises(self, player):
        self.file_output.write ("\n\n--------Function displayFranchises --------")
        self.file_output.write ("\nPlayer name: {0}".format(player))
        self.file_output.write ("\nList of Franchises:\n")
        self.file_output.write ('\n'.join(self.edges[player]))
        self.file_output.write ("\n-------------------------------------------")
        
    '''
    Check whether the players are in the same franchise
    '''
    def franchiseBuddies(self, playerA, playerB):
        self.file_output.write ("\n\n--------Function franchiseBuddies --------")
        self.file_output.write ("\nPlayer A: {0}".format(playerA))
        self.file_output.write ("\nPlayer B: {0}".format(playerB))
        
        if (False == self.isConnected(playerA, playerB)): 
            self.file_output.write ("\nThey never playered together")
            self.file_output.write ("\n-------------------------------------------")
            return
            
        path, path_len = self.get_path_parameters (playerA, playerB)
        
        if (path_len != 2 ):
            self.file_output.write ("\nThey never playered together")
            self.file_output.write ("\n-------------------------------------------")
            return
                        
        else :
            if (len(path) == 3 ):
                self.file_output.write ("\nFranchise Buddies: Yes, ")
                self.file_output.write ('\n {0}'.format(path[1]))
        self.file_output.write ("\n-------------------------------------------")        
        
    def findPlayerConnect(self, playerA, playerB ):
    
        self.file_output.write  ("\n--------Function findPlayerConnect --------")
        self.file_output.write  ("\nPlayer A: {0}".format(playerA))
        self.file_output.write  ("\nPlayer B: {0}".format(playerB))
        
        if (False == self.isConnected(playerA, playerB)): 
            self.file_output.write  ("\nNo common player found between planyers {0} and {1}".format(playerA, playerB))
            self.file_output.write ("\n-------------------------------------------")
            return
            
        path, path_len = self.get_path_parameters (playerA, playerB)
        
        if (path_len != 4 ):
            self.file_output.write  ("\nPlayer {0} and {1} connected with different path".format(playerA, playerB))
                        
        else :
            if (len(path) == 5 ):
                self.file_output.write  ('\nRelated: Yes, {0} > {1} > {2} > {3} > {4}'.format(path[4], path[3], path[2], path[1], path[0]))
        self.file_output.write ("\n-------------------------------------------")
  
    def get_path_parameters(self, source, dest):
        path = []
        crawl = dest
        path.append(crawl)
        crawl_index = self.pred[self.PlayerTeam.index(crawl)]
        while crawl_index != -1:
            path.append(self.PlayerTeam[crawl_index])
            crawl_index = self.pred[crawl_index]
        
        return path, self.dist[self.PlayerTeam.index(dest)]
     
        
    # Verify the players are connected
    def isConnected(self, playerA, playerB): 
        
        # Flags to mark the visited vertices
        visited =[False]*len(self.PlayerTeam) 
        self.pred =[-1]*len(self.PlayerTeam) 
        self.dist =[None]*len(self.PlayerTeam) 
   
        # Queue to track the traversal
        queue=[] 
   
        # Mark the source node as visited and enqueue it 
        queue.append(playerA) 
        visited[self.PlayerTeam.index(playerA)] = True
        self.dist[self.PlayerTeam.index(playerA)] = 0
   
        while queue: 
  
            # Dequue from the storage
            n = queue.pop(0) 
            
            #  continue to do BFS 
            for i in range (len(self.edges[n])): 
                index = self.PlayerTeam.index(self.edges[n][i])
                
                if visited[index] == False: 
                    visited[index] = True
                    self.dist[index] = self.dist[self.PlayerTeam.index(n)] + 1
                    self.pred[index] = self.PlayerTeam.index(n)
                    queue.append(self.PlayerTeam[index])                     
                    visited[index] = True
                    
                    if (self.edges[n][i] == playerB):
                        return True
        
        # The BFS completed but we didnt visited playerB 
        return False
    def displayAll(self):
        print(self.PlayerTeam)
        print(self.edges )
        
if __name__ == "__main__":
    iplBench = IPL()
    iplBench.readInputfile("inputPS10.txt")
    iplBench.readPromptsfile("promptsPS10.txt")
    iplBench.displayAll()
    