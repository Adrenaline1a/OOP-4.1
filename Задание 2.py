#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import argparse


# Создать класс Triangle для представления треугольника. Поля данных должны включать
# углы и стороны. Требуется реализовать операции: получения и изменения полей данных,
# вычисления площади, вычисления периметра, вычисления высот, а также определения
# вида треугольника (равносторонний, равнобедренный или прямоугольный).


class Triangle:
	def __init__(self):
		self.a = 0
		self.b = 0
		self.c = 0
		self.ab = 0
		self.bc = 0
		self.ac = 0
		self.S = 0
		self.p = 0

	def read(self, prompt=None):
		lst = list(map(int, input('Введите 3 стороны и 3 угла в градусах: ').split())) if prompt is None else input(prompt)
		self.a = lst[0]
		self.b = lst[1]
		self.c = lst[2]
		self.ab = lst[3]
		self.bc = lst[4]
		self.ac = lst[5]
		self.p = (self.a + self.b + self.c)/2
		self.S = math.sqrt(self.p*(self.p-self.a)*(self.p-self.b)*(self.p-self.c))

	def display(self):
		print("       Общая сводка ")
		self.data()
		self.square()
		self.perimeter()
		self.heights()
		self.view()

	def data(self):
		print(f"Стороны треугольника {self.a}, {self.b}, {self.c}\nУглы треугольника: {self.ab}, {self.bc}, {self.ac}")

	def square(self):
		print("Площадь треугольника: ", self.S)

	def perimeter(self):
		print("Периметр треугольника: ", self.a + self.b + self.c)

	def heights(self):
		print("Высоты треугольника: ", 2*self.S/self.a, 2*self.S/self.b, 2*self.S/self.c)

	def view(self):
		if self.ab == 60:
			print("Треугольник равносторонний")
		elif self.ab == 90 or self.bc == 90 or self.ac == 90:
			print("Треугольник прямоугольный")
		elif self.a == self.b or self.b == self.c or self.a == self.c:
			print("Треугольник ранобедренный")


if __name__ == "__main__":
	command_line = None
	Tri = Triangle()
	file_parser = argparse.ArgumentParser(add_help=False)
	parser = argparse.ArgumentParser("flights")
	parser.add_argument(
		"--version",
		action="version",
		version="%(prog)s 0.1.0")
	subparsers = parser.add_subparsers(dest="command")
	read = subparsers.add_parser(
		"read",
		parents=[file_parser])
	square = subparsers.add_parser(
		"square",
		parents=[file_parser])
	perimeter = subparsers.add_parser(
		"perimeter",
		parents=[file_parser])
	heights = subparsers.add_parser(
		"heights",
		parents=[file_parser])
	view = subparsers.add_parser(
		"view",
		parents=[file_parser])
	display = subparsers.add_parser(
		"display",
		parents=[file_parser])
	data = subparsers.add_parser(
		"data",
		parents=[file_parser])
	args = parser.parse_args(command_line)
	if args.command == 'read':
		Tri.read()
	elif args.command == 'square':
		Tri.square()
	elif args.command == 'perimeter':
		Tri.perimeter()
	elif args.command == 'heights':
		Tri.heights()
	elif args.command == 'view':
		Tri.view()
	elif args.command == 'display':
		Tri.display()
	elif args.command == 'data':
		Tri.data()
