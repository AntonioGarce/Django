from django.http import JsonResponse
from django.shortcuts import render
from product.models import Products
from .models import *
from sitehandlers.models import Site_handlers
from users.models import Favourite
from item_s.models import *
from loguru import logger


# Create your views here.

