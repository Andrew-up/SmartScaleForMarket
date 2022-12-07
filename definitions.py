import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

DATABASE_DIR = os.path.join(ROOT_DIR, "data_base/db.db")
MODEL_CNN_PATH = os.path.join(ROOT_DIR, "modelDataCNN/resultModelCNN/saved_model.h5")
# print(os.path.join(ROOT_DIR, "data_base/db.db"))

TRAIN_PATH = os.path.join(ROOT_DIR, "modelDataCNN/data/train")
TEST_PATH = os.path.join(ROOT_DIR, "modelDataCNN/data/testimage")
