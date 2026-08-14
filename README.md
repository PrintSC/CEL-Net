# CEL-Net

Official implementation of **CEL-Net: Cross-Scale and Edge-Aware Representation Learning for Aerial Small Object Detection**.

CEL-Net is a lightweight detector for small objects in challenging aerial scenes. It combines a Cross-Scale Interaction Module (CIM), a Spatial Attention Module (SAM), and an Edge-enhanced Large Kernel Border (ELKB) module to improve multi-scale feature fusion, suppress background interference, and preserve object boundaries. The method is evaluated on VisDrone, AI-TOD, and UAVDT.

## Overview

### Motivation

![Motivation and feature visualization of CEL-Net](assert/first.jpg)

### Architecture

![CEL-Net architecture](assert/overview.jpg)

## Qualitative Results

### VisDrone

![CEL-Net qualitative results on VisDrone](assert/visualizations/visdrone_results.png)

### AI-TOD

![CEL-Net qualitative results on AI-TOD](assert/visualizations/ai_tod_results.png)

### UAVDT

![CEL-Net qualitative results on UAVDT](assert/visualizations/uavdt_results.png)

## Main Results

Representative results reported in the paper are shown below. FPS is measured on a single RTX 4090 with 640 x 640 input.

| Dataset | Model | mAP50 (%) | mAP50:95 (%) | FPS |
| --- | --- | ---: | ---: | ---: |
| VisDrone | CEL-Net-X | 47.3 | 31.5 | 65 |
| AI-TOD | CEL-Net-M | 59.8 | 29.2 | - |
| UAVDT | CEL-Net-X | 33.0 | 21.0 | 65 |

CEL-Net provides five model scales for different accuracy and efficiency requirements.

| Model | Layer depth | Parameters (M) | FLOPs (G) |
| --- | ---: | ---: | ---: |
| CEL-Net-N | 125 | 2.643 | 7.7 |
| CEL-Net-S | 216 | 4.933 | 22.5 |
| CEL-Net-M | 353 | 15.325 | 48.4 |
| CEL-Net-L | 329 | 24.321 | 81.9 |
| CEL-Net-X | 378 | 36.298 | 122.3 |

## Repository Structure

```text
CEL-Net/
+-- assert/                         # Paper figures and qualitative results
+-- results/                        # Example training and validation outputs
+-- ultralytics/
|   +-- cfg/datasets/               # AI-TOD, VisDrone, and UAVDT data configs
|   +-- cfg/models/CEL-Net/         # CEL-Net-N/S/M/L/X model configs
|   +-- nn/modules/conv.py          # CIM, SAM, and large-kernel modules
+-- train_model.py                  # Training entry point
+-- requirement.txt                 # Reference environment package versions
+-- pyproject.toml                  # Package metadata and dependencies
```

The model configuration filenames retain the legacy `R2-YOLO_*.yaml` naming, but they define the CEL-Net variants used by this repository.

## Installation

Create an isolated environment and install a PyTorch build compatible with your CUDA driver. Then install this repository in editable mode.

```bash
conda create -n celnet python=3.9 -y
conda activate celnet

# Install PyTorch for your CUDA environment first, then:
pip install -e .
```

`requirement.txt` records the package versions used in the reference environment, including PyTorch 1.10.1 with CUDA 11.3.

## Dataset Preparation

Dataset configuration files are provided for all three benchmarks:

```text
ultralytics/cfg/datasets/AI-TOD.yaml
ultralytics/cfg/datasets/VisDrone.yaml
ultralytics/cfg/datasets/UAVDT.yaml
```

Download each dataset from its official source and convert its annotations to YOLO format. Before training, update the `path` field in the selected YAML file to the corresponding dataset root.

```text
dataset_root/
+-- images/
|   +-- train/
|   +-- val/
+-- labels/
    +-- train/
    +-- val/
```

## Training

Train CEL-Net-N on VisDrone:

```bash
yolo detect train \
  model=ultralytics/cfg/models/CEL-Net/R2-YOLO_n.yaml \
  data=ultralytics/cfg/datasets/VisDrone.yaml \
  epochs=500 batch=32 imgsz=640 device=0,1
```

Change the dataset configuration to train on AI-TOD or UAVDT:

```bash
yolo detect train model=ultralytics/cfg/models/CEL-Net/R2-YOLO_n.yaml data=ultralytics/cfg/datasets/AI-TOD.yaml epochs=500 batch=32 imgsz=640 device=0,1
yolo detect train model=ultralytics/cfg/models/CEL-Net/R2-YOLO_n.yaml data=ultralytics/cfg/datasets/UAVDT.yaml epochs=500 batch=32 imgsz=640 device=0,1
```

Available model configurations are `R2-YOLO_n.yaml`, `R2-YOLO_s.yaml`, `R2-YOLO_m.yaml`, `R2-YOLO_l.yaml`, and `R2-YOLO_x.yaml`.

## Validation and Inference

Validate a trained checkpoint:

```bash
yolo detect val model=path/to/best.pt data=ultralytics/cfg/datasets/VisDrone.yaml imgsz=640 device=0
```

Run inference on an image or directory:

```bash
yolo detect predict model=path/to/best.pt source=path/to/images imgsz=640 device=0
```

## Notes

- Pretrained weights and datasets are not included.
- Dataset paths in the YAML files must be updated before training or evaluation.
- The codebase is built on Ultralytics and distributed under the AGPL-3.0 license.

## Citation

The complete citation will be added when the paper is formally published. Until then, please cite the paper by its full title:

> CEL-Net: Cross-Scale and Edge-Aware Representation Learning for Aerial Small Object Detection
