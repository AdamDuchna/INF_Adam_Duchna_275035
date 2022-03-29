#LocalBestPSO ring topology
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters.plotters import plot_contour
from pyswarms.utils.plotters.formatters import Mesher
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9, 'k': 3, 'p': 2}
optimizer = ps.single.LocalBestPSO(n_particles=30, dimensions=2, options=options)
# historia kosztów i pozycji
cost_history, pos_history = optimizer.optimize(fx.sphere, iters=200)
#tworzenie animacji
m = Mesher(func=fx.sphere)
animation = plot_contour(pos_history=optimizer.pos_history,
                         mesher=m,
                         mark=(0,0))
animation.save('plot0.gif', writer='imagemagick', fps=10)

#GeneralBestPSO with pyramid topology
from pyswarms.backend.topology import Pyramid
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters.plotters import plot_contour
from pyswarms.utils.plotters.formatters import Mesher
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
my_topology = Pyramid()
optimizer = ps.single.GeneralOptimizerPSO(n_particles=30, dimensions=2, options=options , topology=my_topology)
# historia kosztów i pozycji
cost_history, pos_history = optimizer.optimize(fx.sphere, iters=200)
#tworzenie animacji
m = Mesher(func=fx.sphere)
animation = plot_contour(pos_history=optimizer.pos_history,
                         mesher=m,
                         mark=(0,0))
animation.save('pyramid.gif', writer='imagemagick', fps=10)

#GeneralBestPSO with vonNeumann topology
from pyswarms.backend.topology import VonNeumann
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters.plotters import plot_contour
from pyswarms.utils.plotters.formatters import Mesher
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9 ,'r':2 ,'p':1 }
my_topology = VonNeumann()
optimizer = ps.single.GeneralOptimizerPSO(n_particles=20, dimensions=2, options=options , topology=my_topology)
# historia kosztów i pozycji
cost_history, pos_history = optimizer.optimize(fx.sphere, iters=200)
#tworzenie animacji
m = Mesher(func=fx.sphere)
animation = plot_contour(pos_history=optimizer.pos_history,
                         mesher=m,
                         mark=(0,0))
animation.save('neumann.gif', writer='imagemagick', fps=10)