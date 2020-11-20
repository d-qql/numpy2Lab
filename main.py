import numpy as np
import matplotlib.pyplot as plt
filenumb = "03"
file = open("signals/signal" + filenumb + ".dat").read()
def move_filt(a, n = 10):
    k = []
    for i in range(len(a)):
        if i < n-1:
            k.append(sum(a[:i+1])/(i+1))
        else:
            k.append(sum(a[i-(n-1) : i+1])/10)
    return np.array(k)
sig = np.array([float(i) for i in file.split()])
x = [i for i in range(len(sig))]

plt.subplot(2, 1, 1)
plt.plot(x, sig)
plt.title("input signal" + filenumb)
plt.subplot(2,1,2)
plt.plot(x, move_filt(sig))
plt.title("Filtered")
plt.savefig("sig" + filenumb + "res.jpg")