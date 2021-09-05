from matplotlib import pyplot as plt
plt.bar([0.25,1.25,2.25,3,3.35,3.75],[50,40,80,87,90,65],label="BMW",width=.5)
plt.bar([.75,1.65,1.95,2.0,2.25],[80,20,20,50,60],label="AUDI",WIDTH=.5)
plt.legend()
plt.xlabel("DAYS")
plt.ylabel("distance(kms)")
plt.title("information")
plt.show()
