from torchvision import transforms
import pytorch_lightning as pl
import torch.nn as nn
import numpy as np
import pandas as pd
import torch.nn.functional as F
import torchmetrics
from torchmetrics.functional import accuracy
import torchsummary
from torchsummary import summary
from pytorch_lightning.loggers import CSVLogger
import torch
from flask import Flask, request, render_template, redirect, url_for
import io
import base64
import os
from werkzeug.utils import secure_filename
import openai
from sklearn.feature_extraction.text import CountVectorizer
import MeCab
mecab = MeCab.Tagger('-Owakati')

class Net(pl.LightningModule):
    def __init__(self):
      super().__init__()
      self.fc1 = nn.Linear(545, 100)
      self.fc2 = nn.Linear(100, 26)

    def forward(self, x):
      x = F.relu(self.fc1(x))
      x = self.fc2(x)
      return x