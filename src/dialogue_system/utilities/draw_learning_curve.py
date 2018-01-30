# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import pickle


class Ploter(object):
    def __init__(self, performance_file):
        self.performance_file = performance_file
        self.performance = pickle.load(file=open(self.performance_file, "rb"))
        self.epoch_index = []
        self.success_rate = []
        self.average_reward = []
        self.average_wrong_disease = []
        self.__prepare_data()

    def __prepare_data(self, epoch_size = 50):
        epoch_size = max(epoch_size, len(self.performance.keys()))
        for epoch_index in range(0, epoch_size, 1):
            self.epoch_index.append(epoch_index)
            self.success_rate.append(self.performance[epoch_index]["success_rate"])
            self.average_reward.append(self.performance[epoch_index]["average_reward"])
            self.average_wrong_disease.append(self.performance[epoch_index]["average_wrong_disease"])

    def plot(self, save_name):
        plt.plot(self.epoch_index,self.success_rate, label="DQN Agent", linewidth=1)
        plt.xlabel("Simulation Epoch")
        plt.ylabel("Success Rate")
        plt.title("Learning Curve")
        plt.hlines(0.15,0,400,label="Random Agent", linewidth=1, colors="r")
        plt.hlines(0.41,0,400,label="Rule Agent", linewidth=1, colors="purple")
        plt.grid(True)
        plt.legend(loc="lower right")
        plt.savefig(save_name,dpi=400)

        plt.show()


if __name__ == "__main__":
    file_name = "./../model/dqn/learning_rate/learning_rate_e400.p"
    save_name = "./../model/dqn/learning_rate/learning_rate_e400_0.9.p" + ".png"
    ploter = Ploter(file_name)
    ploter.plot(save_name)