import os

import gdown
import torch
import torchvision


def resnet50(pretrained=True, download=True):
    filename = "resnet50_cifar10.pth"
    gdrive_id = "1Ng7pSYL9T2qIcmpLWazpAHJBtLEoptsg"

    if not pretrained and download:
        print("Warning: pretrained=False and download=True. Setting download=False.")

    model = torchvision.models.resnet50(weights=None, num_classes=10)
    model.maxpool = torch.nn.Identity()

    if not pretrained:
        return model

    if download and not os.path.exists(filename):
        gdown.download(id=gdrive_id, output=filename, quiet=False)

    assert os.path.exists(filename), "Pretrained model not found. Set download=True to download the model."

    model.load_state_dict(torch.load(filename))
    return model


def resnet18(pretrained=True, download=True):
    filename = "resnet18_cifar10.pth"
    gdrive_id = "1b0ruLwOuL-_wfSIWMHLBAyknKxmS7x9N"

    if not pretrained and download:
        print("Warning: pretrained=False and download=True. Setting download=False.")

    model = torchvision.models.resnet18(weights=None, num_classes=10)
    model.maxpool = torch.nn.Identity()

    if not pretrained:
        return model

    if download and not os.path.exists(filename):
        gdown.download(id=gdrive_id, output=filename, quiet=False)

    assert os.path.exists(filename), "Pretrained model not found. Set download=True to download the model."

    model.load_state_dict(torch.load(filename))
    return model


def resnext101_64x4d(pretrained=True, download=True):
    filename = "resnext101_cifar10.pth"
    gdrive_id = "108G120wW2KG6A8PDkYkP1vgcK7sEvlCM"

    if not pretrained and download:
        print("Warning: pretrained=False and download=True. Setting download=False.")

    model = torchvision.models.resnext101_64x4d(weights=None, num_classes=10)
    model.maxpool = torch.nn.Identity()

    if not pretrained:
        return model

    if download and not os.path.exists(filename):
        gdown.download(id=gdrive_id, output=filename, quiet=False)

    assert os.path.exists(filename), "Pretrained model not found. Set download=True to download the model."

    model.load_state_dict(torch.load(filename))
    return model
