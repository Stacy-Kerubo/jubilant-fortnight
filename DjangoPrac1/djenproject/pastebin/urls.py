from django.urls import path
from .views import PasteCreate,PasteDetail,PasteList,PasteDelete,PasteUpdate

urlpatterns = [
path('', PasteCreate.as_view(), name='create'),
path('paste/', PasteList.as_view(), name='pastebin_paste_list'),
path('paste/<int:pk>', PasteDetail.as_view(), name='pastebin_paste_detail'),
path('paste/delete/<int:pk>', PasteDelete.as_view(), name='pastebin_paste_delete'),

path('paste/edit/<int:pk>', PasteUpdate.as_view(), name='pastebin_paste_edit'),
]




