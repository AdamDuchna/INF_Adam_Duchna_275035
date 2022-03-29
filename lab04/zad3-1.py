#CZESC 1
import matplotlib.pyplot as plt
from pyswarms.utils.plotters import plot_cost_history
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx

options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
#Matyas function
#cost, pos = optimizer.optimize(fx.matyas, iters=1000)
#Ackley function
#cost, pos = optimizer.optimize(fx.ackley, iters=1000)
#Treehump function
cost, pos = optimizer.optimize(fx.threehump, iters=1000)

cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()


#CZESC 2
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters.plotters import plot_contour
from pyswarms.utils.plotters.formatters import Mesher
import matplotlib.animation as pyAnimation
options = {'c1':0.5, 'c2':0.3, 'w':0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
#Matyas function
#cost_history, pos_history = optimizer.optimize(fx.matyas, iters=100)
#m = Mesher(func=fx.matyas)
#animation = plot_contour(pos_history=optimizer.pos_history,
#                        mesher=m,
#                        mark=(0,0))
#animation.save('matyas.gif', writer='imagemagick', fps=10)

#Ackley function

#cost_history, pos_history = optimizer.optimize(fx.ackley, iters=100)
#m = Mesher(func=fx.ackley)
#animation = plot_contour(pos_history=optimizer.pos_history,
#                         mesher=m,
#                        mark=(0,0))
#animation.save('ackley.gif', writer='imagemagick', fps=10)

#Treehump function
cost_history, pos_history = optimizer.optimize(fx.threehump, iters=100)
m = Mesher(func=fx.threehump)
animation = plot_contour(pos_history=optimizer.pos_history,
                         mesher=m,
                         mark=(0,0))
animation.save('treehump.gif', writer='imagemagick', fps=10)