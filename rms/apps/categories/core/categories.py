from typing import List

from rest_framework.parsers import JSONParser

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpRequest

from ..models import CategoriesModel

from ..serializers import CategoriesModelSerializer




# =============================================GET=============================================

def get_categorie_core(request: HttpRequest) -> List[CategoriesModel]:
    categories = CategoriesModel.objects.all()
    return CategoriesModelSerializer(categories, many=True)
