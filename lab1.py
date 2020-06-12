# Laba1. Only signal generation

import numpy as np
import matplotlib.pyplot as plt

from random import random
import math

N = 256 #number of discrete
n = 10 #number of harmonic
w = 2700 #cutoff frequency
A = 5 # max amplitude
x = np.arange(0, N, 1)

class DrawOption():
  def __init__(self, pl_title, pl_type="plot", x_range=x):
    self.pl_title = pl_title
    self.pl_type = pl_type
    self.x_range = x_range

def draw_plot(axes, data_plot, options_plot):
  axes.set_title(options_plot.pl_title)
  if options_plot.pl_type == "bar":
    axes.bar(options_plot.x_range, data_plot)
  elif options_plot.pl_type == "plot":
    axes.plot(options_plot.x_range, data_plot)
  elif options_plot.pl_type == "stem":
    axes.stem(options_plot.x_range, data_plot, use_line_collection=True)

def draw(data, options, picture_name):
  data_length = len(data)
  if len(data) > 1:
    _, axes = plt.subplots(len(data), sharex=False, figsize=(10, 8))
    for i in range(data_length):
      draw_plot(axes[i], data[i], options[i])
  else:
    plt.figure(figsize=(10,8))
    plt.plot(x, data[0])
  plt.savefig(picture_name)
  plt.show()

def generate_signal(t):
  sum_res = 0
  wp = w / n

  for _ in range(n):
    a = A * random()
    fi = 2 * math.pi * random()
    sum_res += a * math.sin(wp * t + fi)
    wp += w / n

  return sum_res

def main_fn():
  signal = np.array([generate_signal(i) for i in range(N)])
  options = [
    DrawOption("Signal", "plot"),
  ]
  draw([signal], options, "lab1.png")

if __name__ == '__main__':
  main_fn()