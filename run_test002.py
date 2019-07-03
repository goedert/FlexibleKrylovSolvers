# Enforce Python3 usage
import sys
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

# Local dir
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '/'

import sys
# Add resources from previous LU Decomp implementation
sys.path.append(dir_path + 'tests/')

# Import local test module
from test002_plot_resid_vs_matmuls import plot_resid_vs_matmuls

# Apply test
plot_resid_vs_matmuls()
