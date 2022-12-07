import numpy as np


class DifferenceScheme:
    def __init__(self, R = 8, T = 130, k = 0.59, c = 1.65, l = 0.2, I = 40, K = 6400 ) -> None:
        self.R = R
        self.T = T
        self.k = k
        self.c = c
        self.l = l
        self.K = K
        self.I = I
        self.h_teta = np.pi/2 / I
        self.h_t = T / K
        self.v = np.zeros((K + 1, I + 1))
        self.arr_t_k = np.zeros(K + 1)
        self.arr_teta_i = np.zeros(I + 1)
        for k in range(len(self.arr_t_k)):
            self.arr_t_k[k] = self.t_k(k)
        for i in range(len(self.arr_teta_i)):
            self.arr_teta_i[i] = self.teta_i(i)
        self.array_filling()

    def psi(self, teta) -> float:
        #print(8 * pow(np.cos(teta), 4))
        return 8 * pow(np.cos(teta), 4)

    def teta_i(self, i: int) -> float:
        return i * self.h_teta

    def t_k(self, k: int) -> float:
        return k * self.h_t

    def array_filling(self):
        for i in range(self.I + 1):
          self.v[0][i] = self.psi(self.teta_i(i)) #Заполнение 0 строки по времени функцией psi(teta)
        gamma = (self.k * self.h_t) / (self.c * (self.R ** 2) * (self.h_teta ** 2)) # фиксируем консанту
        self.v[1][0] = self.v[0][0] + 2 * gamma * (2 * self.v[0][1] - 2 * self.v[0][0]) # для более понятного условия запишем первую строку вне цикла
        for i in range(1, self.I-1 + 1):
          self.v[1][i] = self.v[0][i] + gamma * ((np.cos(self.teta_i(i))/np.sin(self.teta_i(i))) * self.h_teta * (self.v[0][i+1] - self.v[0][i]) + (self.v[0][i+1] - 2 * self.v[0][i] + self.v[0][i-1]))
        #self.v[1][self.I-1] = self.v[1][self.I-2]
        for k in range(1, self.K - 1 + 1): # основной цикл для заполнения остальных строк
          for i in range(self.I-1 + 1):
            if i == 0:
              self.v[k+1][i] = self.v[k][i] + 2 * gamma * (2 * self.v[k][i+1] - 2 * self.v[k][i])
            else:
              if i == (self.I - 2 + 1):
                self.v[k][self.I-1 + 1] = self.v[k][self.I-2 + 1]
                #print(i)
              #else:
              self.v[k+1][i] = self.v[k][i] + gamma * ((np.cos(self.teta_i(i))/np.sin(self.teta_i(i))) * self.h_teta * (self.v[k][i+1] - self.v[k][i]) + (self.v[k][i+1] - 2 * self.v[k][i] + self.v[k][i-1]))
        self.v[self.K-1 + 1][self.I-1 + 1] = self.v[self.K-1 + 1][self.I-2 + 1]


class DifferenceScheme_MOD:
    def __init__(self, R = 8, T = 130, k = 0.59, c = 1.65, l = 0.2, I = 40, K = 6400 ) -> None:
        self.R = R
        self.T = T
        self.k = k
        self.c = c
        self.l = l
        self.K = K
        self.I = I
        self.h_teta = np.pi/2 / I
        self.h_t = T / K
        self.v = np.zeros((K + 1, I + 1))
        self.arr_t_k = np.zeros(K + 1)
        self.arr_teta_i = np.zeros(I + 1)
        for k in range(len(self.arr_t_k)):
            self.arr_t_k[k] = self.t_k(k)
        for i in range(len(self.arr_teta_i)):
            self.arr_teta_i[i] = self.teta_i(i)
        self.array_filling()

    def psi(self, teta):
        return 8 * pow(np.cos(teta), 4)

    def teta_i(self, i : int):
        return i * self.h_teta

    def t_k(self, k : int):
        return k * self.h_t

    def array_filling(self):
            for i in range(self.I + 1):
              self.v[0][i] = self.psi(self.teta_i(i)) #Заполнение 0 строки по времени функцией psi(teta)
            gamma = (self.k * self.h_t) / (self.c * (self.R ** 2) * (self.h_teta ** 2)) # фиксируем консанту
            self.v[1][0] = self.v[0][0] + 2 * gamma * (2 * self.v[0][1] - 2 * self.v[0][0]) # для более понятного условия запишем первую строку вне цикла
            for i in range(1, self.I-1 + 1):
              self.v[1][i] = self.v[0][i] + gamma * ((np.cos(self.teta_i(i))/np.sin(self.teta_i(i))) * self.h_teta * ((self.v[0][i+1] - self.v[0][i-1]) / 2) + (self.v[0][i+1] - 2 * self.v[0][i] + self.v[0][i-1]))
            self.v[1][self.I - 1 + 1] = self.v[1][self.I - 1 + 1] + 2 * gamma * (self.v[1][self.I - 1 + 1 -1] - self.v[1][self.I - 1 + 1])
            for k in range(1, self.K - 1 + 1): # основной цикл для заполнения остальных строк
              for i in range(self.I + 1):
                if i == 0:
                  self.v[k+1][i] = self.v[k][i] + 2 * gamma * (2 * self.v[k][i+1] - 2 * self.v[k][i])
                else:
                  if i == (self.I - 1 + 1):
                    self.v[k+1][i] = self.v[k][i] + 2 * gamma * (self.v[k][i-1] - self.v[k][i])
                    #print(i)
                  else:
                    self.v[k+1][i] = self.v[k][i] + gamma * ((np.cos(self.teta_i(i))/np.sin(self.teta_i(i))) * self.h_teta * ((self.v[k][i+1] - self.v[k][i-1]) / 2) + (self.v[k][i+1] - 2 * self.v[k][i] + self.v[k][i-1]))