from custom_enums import Terrain
from gui import LandscapeGUI
import random
import numpy as np

class ProbabilisticHunting:

    def __init__(self, dimension):
        self.Map = []
        self.Belief = []
        self.dimension = dimension

        self.currentTime = 0
        self.beta = 1

        self.NotFound_given_Present_Flat = 0.1
        self.NotFound_given_Present_Hilly = 0.3
        self.NotFound_given_Present_Forest = 0.7
        self.NotFound_given_Present_Cave = 0.9

        self.target_i = 1
        self.target_j = 1

        self._initialiseMap()

    def getMap(self):
        return self.Map

    def _initialiseMap(self):

        self.beta = 1

        flatProbability = 0.2
        hillyProbability = 0.3
        forestProbability = 0.3
        caveProbability = 0.2

        visited = []
        for i in range(0, self.dimension):
            visited.append([])
            self.Map.append([])
            for j in range(0, self.dimension):
                visited[i].append(False)
                self.Map[i].append(Terrain.CAVE)

        totalCells = self.dimension * self.dimension
        flatCells = totalCells * flatProbability
        hillyCells = totalCells * hillyProbability
        forestcells = totalCells * forestProbability

        count = flatCells
        while(count > 0):
            i = random.randint(0, self.dimension-1)
            j = random.randint(0, self.dimension-1)
            if(visited[i][j] == False):
                self.Map[i][j] = Terrain.FLAT
                visited[i][j] = True
                count -= 1
        count = hillyCells
        while (count > 0):
            i = random.randint (0, self.dimension - 1)
            j = random.randint (0, self.dimension - 1)
            if (visited[i][j] == False):
                self.Map[i][j] = Terrain.HILLY
                visited[i][j] = True
                count -= 1
        count = forestcells
        while (count > 0):
            i = random.randint (0, self.dimension - 1)
            j = random.randint (0, self.dimension - 1)
            if (visited[i][j] == False):
                self.Map[i][j] = Terrain.FOREST
                visited[i][j] = True
                count -= 1

        self._setTarget()

    def _setTarget(self):
        self.target_i = random.randint(0, self.dimension - 1)
        self.target_j = random.randint(0, self.dimension - 1)

    def showMap(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(self.Map[i][j].name, end = " ")
            print()

    def initialiseBelief(self):
        for i in range(0, self.dimension):
            self.Belief.append([])
            for j in range(0, self.dimension):
                self.Belief.append(1/(self.dimension * self.dimension))

    def updateBelief(self, i, j):
        pass

    def targetFound(self, i, j):

        success_probability = 1

        if(self.target_i != i or self.target_j != j):
            return False

        if(self.Map[i][j] == Terrain.FLAT):
            success_probability = 10
        elif(self.Map[i][j] == Terrain.HILLY):
            success_probability = 30
        elif(self.Map[i][j] == Terrain.HILLY):
            success_probability = 70
        else:
            success_probability = 90

        random_number = random.randint(1, 100)
        if(random_number >= success_probability):
            return True
        return False

    # search Belief for the highest probability
    # if more than one found, select random
    def getNextSearchCell(self):
        # self.Belief[0][3] = 0.02
        # self.Belief[2][2] = 0.02
        # self.Belief[2][3] = 0.02
        arrayBelief = np.array(self.Belief)
        minBelief = np.where(arrayBelief == arrayBelief.min())
        if(len(minBelief[0]) > 1):
            # choice = random.choice(minBelief[0])
            choicePos = random.randrange(len(minBelief[0]))
            # choicePos = np.where( minBelief[0] == choice)[0][0]
            print(minBelief[0])
            # print(np.where( minBelief[0] == choice)[0][0])
            # print(choice)
            # print(minBelief[0][choicePos], minBelief[1][choicePos])
            return minBelief[0][choicePos], minBelief[1][choicePos]
        else:
            # print(minBelief[0][0], minBelief[1][0])
            return minBelief[0][0], minBelief[1][0]

    def startHunt(self):

        while(True):
            (i, j) = self.getNextSearchCell()
            found = self.targetFound(i, j)
            if(found):
                print("!! FOUND IT !!")
                break
            else:
                self.updateBelief(i, j)
                self.currentTime += 1

if __name__ == '__main__':
    ph = ProbabilisticHunting(50)
    root = Tk ()
    grid = LandscapeGUI (root)
    grid.paint_map (ph.getMap())
    root.mainloop ()