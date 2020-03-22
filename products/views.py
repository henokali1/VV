from django.views.generic import TemplateView
from django.shortcuts import render
from .models import *
import urllib.parse
import ast
import requests
import time
import json
import datetime
from statistics import variance, mean
import concurrent.futures
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def dashboard(request):
    return render(request, 'products/dashboard.html')

def vv_product(request):
    return render(request, 'products/vv_product.html')