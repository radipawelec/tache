from django.db import models
from .context_processor import *


class ListBoard(models.Model):
    board_name = models.CharField(max_length=100, verbose_name="Board")
    board_active_status = models.BooleanField(default=True, verbose_name='Active')
    board_background = models.CharField(max_length=500)

    def __str__(self):
        return self.board_name

    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'


class ListList(models.Model):
    list_board = models.ForeignKey(ListBoard, on_delete=models.CASCADE, blank=False)
    list_name = models.CharField(max_length=100, verbose_name='Name')
    list_description = models.TextField(blank=True, verbose_name='Description')
    list_active_status = models.BooleanField(default=True, verbose_name='Active')
    list_create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Create date')
    list_modify_date = models.DateTimeField(auto_now=True, editable=True, verbose_name='Last activity')

    def __str__(self):
        return self.list_name

    class Meta:
        verbose_name = 'List'
        verbose_name_plural = 'Lists'

class ListCard(models.Model):

    card_list = models.ForeignKey(ListList, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=100)
    card_description = models.TextField(blank=True)
    card_active_status = models.BooleanField(default=True)
    card_priority = models.IntegerField(choices=((1, 'Normal'), (2, 'High'), (3, 'ASAP'), (4, 'NOW')), default=1)
    card_create_date = models.DateTimeField(auto_now_add=True, editable=False)
    card_modify_date = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.card_name

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
