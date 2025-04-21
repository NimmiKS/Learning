from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from .import views
from block_array.views import BlockArrayView, ExportCSVView

urlpatterns = [
    path('',BlockArrayView.as_view(),name='block'),
    path('export-csv/', ExportCSVView.as_view(), name='export_csv'),
]
