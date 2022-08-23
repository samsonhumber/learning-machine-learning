import sys
sys.path.append('/server/backend')
import index 
from config import app

if __name__ == '__main__':app.run(host="localhost", port=3000)