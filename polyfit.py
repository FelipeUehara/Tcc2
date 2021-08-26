import os
import sys
import pandas as pd
import numpy as np
from numpy.polynomial import Polynomial as P
filepath = os.path.dirname(os.path.abspath("")) + "/ToPython"
import matplotlib.pyplot as plt
import sympy
# ERRO norm(VETOR_ORIGINAL - VETOR_GERADO_PELO_POLINOMIO).^2 / norm(VETOR_ORIGINAL).^2
#https://www.youtube.com/watch?v=_pJX2SFoFtY
# https://www.studytonight.com/post/what-is-mean-squared-error-mean-absolute-error-root-mean-squared-error-and-r-squared

class Polyfit:
    def __init__(self):
        self.xm = list(range(1440))
        self.main()
        

    def sub_sub_main(self,df,index):
        day = df.iloc[index][1:1441]
        ym = np.array(day)
        return ym

    def sub_main(self,tipo):
        filename = f'dados_{tipo}.csv'
        df = pd.read_csv(filename)
        self.erro_list = []
        for index in list(range(7)):
            ym1 = self.sub_sub_main(df,index)
            ym2 = self.sub_sub_main(df,index+7)

            p1 = P.fit(self.xm, ym1, 12)
            p2 = P.fit(self.xm, ym2, 12)

            p = (p1+p2)/2
            day3 = df.iloc[index+14][1:1441]
            dayr = []
            for each in list(range(1440)):
                dayr.append(p(each))
            erro = np.linalg.norm(day3 - dayr)**2/np.linalg.norm(day3)**2
            self.erro_list.append(erro)
            
    def main(self):
        tipos = ['bytes','pacotes']
        for tipo in tipos:
            self.sub_main(tipo)

if __name__ == "__main__":
    interval = [1,5,10,30]
    Polyfit()