import UI.main
from definitions import MODEL_CNN_PATH
import os.path
from service.createModel import main
if __name__ == '__main__':
    model = os.path.exists(MODEL_CNN_PATH)
    if model:
        UI.main.startApp()
    else:
        main()
        UI.main.startApp()




