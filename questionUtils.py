# Модуль для подготовки файлов к отправке в Телеграмм и ВК


def parse_quiz_file(filename):	
	with open(f"quiz-questions/{filename}", "r", encoding="KOI8-R") as file:
		file_content = file.read().split("\n\n")
		print (file_content)




if __name__ == '__main__':
	parse_quiz_file("1vs1200.txt")
