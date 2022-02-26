#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json


# Поле first — целое положительное число, номинал купюры; номинал может принимать
# значения 1, 2, 5, 10, 50, 100, 500, 1000, 5000. Поле second — целое положительное число,
# количество купюр данного достоинства. Реализовать метод summa() — вычисление
# денежной суммы.


class TaskOne:
   const_list = [1, 2, 5, 10, 50, 100, 500, 1000, 5000]
   def __init__(self):
      self.sum_dict = {}
      self.summ = 0
      self.first = 0
      self.second = 0

   def read(self, prompt=None):
      self.first = input('Введите номинал купюры: ') if prompt is None else input(prompt)
      if int(self.first) in TaskOne.const_list:
         self.second = input('Введите количество купюр данного номинала: ') if prompt is None else input(prompt)
         self.sum_dict[self.first] = self.second
      else:
         print("Такого номинала нет в списке")

   def display(self):
      print("Сумма: ", make_summa(self.sum_dict, self.summ))


def make_summa(sum_dict, summ):
   with open('new_json.json', 'r', encoding='utf-8') as file:
      json_list = json.load(file)
   json_list.append(sum_dict)
   for i in json_list:
      for k, j in i.items():
         summ += int(k) * int(j)
   with open('new_json.json', 'w', encoding='utf-8') as file:
      json.dump(json_list, file)
   return summ


if __name__ == '__main__':
   print("Список доступных номиналов: 1, 2, 5, 10, 50, 100, 500, 1000, 5000")
   while True:
      r2 = TaskOne()
      r2.read()
      r2.display()
