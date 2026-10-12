import argparse
import os
from ultralytics import YOLO
from utils.parser import parse_args

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

if __name__ == '__main__':
    argparse = parse_args
    args = parse_args()
    model_path = args.model
    print(model_path)
    model = YOLO(model_path)
    train_model = model.train()
