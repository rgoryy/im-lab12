import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Label, Button

import tkinter as tk
import random
import math


class State:
    def __init__(self, name):
        self.name = name
        self.time = 0


class WeatherForecast(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Погода")
        self.geometry("400x100")
        self.weatherLabel = Label(self, text="Погода", font=("Arial", 14))
        self.weatherLabel.pack()

        self.states = []
        self.states.append(State("Солнечно"))
        self.states.append(State("Дождливо"))
        self.states.append(State("Пасмурно"))

        self.startButton = Button(self, text="Старт", command=self.startTimer)
        self.startButton.pack()

        self.stopButton = Button(self, text="Стоп", command=self.stopTimer)
        self.stopButton.pack()

        self.totalTime = 0
        self.state = 0
        self.t = 0
        self.tau = 0
        self.isRunning = False

    def startTimer(self):
        self.isRunning = True
        self.switchState()

    def stopTimer(self):
        self.isRunning = False

        messagebox.showinfo("Отчет", "Всего прошло времени: " + str(self.totalTime))

        for stateObject in self.states:
            messagebox.showinfo("Отчет",
                                "В состоянии " + stateObject.name + " потрачено: " + str(stateObject.time) + ". " + str(
                                    stateObject.time / self.totalTime))

        chiSquare = 0
        for i in range(len(self.states)):
            chiSquare += (self.states[i].time * self.states[i].time) / (self.totalTime * finalProbs[i])
        chiSquare -= self.totalTime

        messagebox.showinfo("Отчет", "Хи-квадрат: " + str(chiSquare))

        if chiSquare > 6:
            messagebox.showinfo("Отчет", "Различия значительны")
        else:
            messagebox.showinfo("Отчет", "Различия незначительны")

    def switchState(self):
        self.tau = math.log(random.random()) / Q[self.state][self.state]
        self.states[self.state].time += self.tau
        self.totalTime += self.tau
        self.t = 0

        A = random.random()
        for i in range(len(self.states)):
            if i == self.state:
                continue
            A -= -Q[self.state][i] / Q[self.state][self.state]
            if A <= 0:
                self.state = i
                break

        self.weatherLabel.config(text=self.states[self.state].name)

        if self.isRunning:
            self.after(1000, self.switchState)


if __name__ == "__main__":
    Q = [
        [-0.4, 0.3, 0.1],
        [0.4, -0.8, 0.4],
        [0.1, 0.4, -0.5]
    ]

    finalProbs = [
        24.0 / 63.0,
        19.0 / 63.0,
        20.0 / 63.0
    ]

    app = WeatherForecast()
    app.mainloop()