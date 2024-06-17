from det3d.utils import build_from_cfg
from torch import nn

from .registry import (
    BACKBONES,
    DETECTORS,
    HEADS,
    LOSSES,
    NECKS,
    READERS,
    SECOND_STAGE,
    ROI_HEAD
)


def build(cfg, registry, default_args=None):
    if isinstance(cfg, list):
        print('\n***************************model is sequential***************************')
        modules = [build_from_cfg(cfg_, registry, default_args) for cfg_ in cfg]
        return nn.Sequential(*modules)
    else:
        print('\n***************************model is build_from_cfg***************************')
        return build_from_cfg(cfg, registry, default_args)

def build_second_stage_module(cfg):
    return build(cfg, SECOND_STAGE)

def build_roi_head(cfg):
    return build(cfg, ROI_HEAD)


def build_reader(cfg):
    return build(cfg, READERS)


def build_backbone(cfg):
    return build(cfg, BACKBONES)


def build_neck(cfg):
    return build(cfg, NECKS)

def build_head(cfg):
    return build(cfg, HEADS)


def build_loss(cfg):
    return build(cfg, LOSSES)


def build_detector(cfg, train_cfg=None, test_cfg=None):
    print("\n\nExecuted build_detector")
    print('[In build_detector]name of Registry ', DETECTORS.name)
    print('[In build_detector]_module_dict ', DETECTORS.module_dict)
    return build(cfg, DETECTORS, dict(train_cfg=train_cfg, test_cfg=test_cfg))
