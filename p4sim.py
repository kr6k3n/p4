



class PowerSim:
    def __init___(self):
        self.state =  [[0]*7 for l in range(6)]
        self.turn = "X"

    
    def __repr__(self):
        for l in range(5,-1,-1):
            for c in range(0,7):
                if g[l][c ] == 0:
                    print(' ', end = ' | ')
                elif g[l][c] == 1:
                    print('O', end = ' | ')
                else :
                    print('X', end = ' | ')
            print(" ")
        print(" ")


    def coup_possible(self, col):
        return not (g[5][c] != 0)
    
    def jouer(self, col):
        l = 0;
        while g[l][c] != 0:
            l += 1
        g[l][c] = j
        