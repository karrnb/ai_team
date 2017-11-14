import random
from tkinter import Canvas, Frame, BOTH
from tkinter import Tk
from custom_enums import Terrain
from probabilistic_hunting import ProbabilisticHunting
import random

class ProbabilisticHunting_TargetFound(ProbabilisticHunting):

    def updateBelief(self, i, j):

        scaling_factor = 1

        if(self.Map[i][j] == Terrain.FLAT):
            scaling_factor = self.NotFound_given_Present_Flat
        elif(self.Map[i][j] == Terrain.HILLY):
            scaling_factor = self.NotFound_given_Present_Hilly
        elif(self.Map[i][j] == Terrain.FOREST):
            scaling_factor = self.NotFound_given_Present_Forest
        else:
            scaling_factor = self.NotFound_given_Present_Cave

        old_belief_i = self.Belief[i][j]
        belief_present = self.Belief[i][j]
        belief_not_present = 1 - self.Belief[i][j]

        belief_present = belief_present * scaling_factor

        self.beta = self.beta - (old_belief_i - belief_present)

        self.Belief[i][j] = belief_present

        self.beta = 0
        for ii in range(0, self.dimension):
            for jj in range(0, self.dimension):
                self.beta += self.Belief[ii][jj]

        for ii in range(0, self.dimension):
            for jj in range(0, self.dimension):
                self.Belief[ii][jj] /= self.beta


if __name__ == '__main__':
    ph = ProbabilisticHunting(50)