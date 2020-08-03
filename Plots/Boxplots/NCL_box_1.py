"""NCL_box_1.py===============This script illustrates the following concepts:   - Drawing box plots   - Explicitly setting the X tickmark labels in a box plotSee following URLs to see the reproduced NCL plot & script:    - Original NCL script: https://www.ncl.ucar.edu/Applications/Scripts/box_1.ncl    - Original NCL plot: https://www.ncl.ucar.edu/Applications/Images/box_1_lg.png"""################################################################################ Import packages:import numpy as npimport matplotlib.pyplot as plt################################################################################ Generate fake data:seed = 200np.random.seed(seed)data = np.random.lognormal(size=(40, 3), mean=1, sigma=.7)for a in range(len(data)):    data[a] = [x-4 for x in data[a]]################################################################################ Plot:# Create figure and axisfig, ax = plt.subplots(figsize=(6,6))boxplots = ax.boxplot(data, labels=['Control', '-2Xna', '2Xna'],                      widths=[0.4, 0.4, 0.4], showfliers=False)# Set w iskers style to dashedplt.setp(boxplots['whiskers'], linestyle='--')plt.show()