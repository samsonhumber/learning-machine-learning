import sys
currentPath = sys.path[0]
windows_extension = '\\'
mac_extension = '/'
sys.path.append(currentPath + windows_extension + 'backend')
sys.path.append(currentPath + mac_extension + 'backend')
print(sys.path) # Use this to check if your path is correctly processed

from config import app

if __name__ == '__main__':app.run(host="localhost", port=3000)