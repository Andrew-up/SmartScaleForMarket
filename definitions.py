import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root

DATABASE_DIR = os.path.join(ROOT_DIR, "backend/data_base/db.db")
MODEL_CNN_PATH = os.path.join(ROOT_DIR, "backend/models_cnn/saved_model.h5")
# print(os.path.join(ROOT_DIR, "data_base/db.db"))

TRAIN_PATH = os.path.join(ROOT_DIR, "backend/models_cnn/data/train")
TEST_PATH = os.path.join(ROOT_DIR, "backend/models_cnn/data/testimage")

VIDEO_OR_IMAGE_TEST_PATH = os.path.join(ROOT_DIR, "frontend/data_test/")
