double_list = [0, 0, 0]
count = 1
word_text = "none"
word_list = []
word_text_list = []

for i in range(3):
    word = input(f"Введите {count} слово: ")
    count += 1
    word_list.append(word)
print()

while word_text != "end":
    word_text = input("Введите слово из текста: ")
    if word_text == "end":
        break
    else:
        word_text_list.append(word_text)
print()
print("Подсчёт слов в тексте")
print(f"{word_list[0]}: ", end="")
print(word_text_list.count(word_list[0]))
print(f"{word_list[1]}: ", end="")
print(word_text_list.count(word_list[1]))
print(f"{word_list[2]}: ", end="")
print(word_text_list.count(word_list[2]))
