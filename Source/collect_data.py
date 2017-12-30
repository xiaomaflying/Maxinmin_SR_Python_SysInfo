from lib.server import main_flows
import os

# path = os.path.join(os.path.dirname(__file__), 'data/conf1.xml')
path = os.path.join(os.path.dirname(__file__), 'data')
main_flows(path)