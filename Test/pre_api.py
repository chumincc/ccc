# -*- coding:utf-8 -*-

import json
import os
import openpyxl

excel_file = 'data.xlsx'
wb = openpyxl.load_workbook(excel_file)
sheet = wb['pre_api']

def pre_method(method):
    for cell in sheet['B']:
        print(cell.value)


