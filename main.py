import frontend.view.main
from definitions import MODEL_CNN_PATH
import os.path
from backend.service.createModel import main
if __name__ == '__main__':
    model = os.path.exists(MODEL_CNN_PATH)
    if model:
        frontend.view.main.startApp()
    else:
        main()
        frontend.view.main.startApp()




