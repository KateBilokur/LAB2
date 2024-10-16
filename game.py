def guess_number():

  max_number = int(input("Введіть максимальне число для відгадування: "))
  number = random.randint(1, max_number)
  guess = 0
  attempts = 0

  while guess != number:
    guess = int(input("Вгадайте число: "))
    attempts += 1

    if guess < number:
      print("Моє число більше.")
    elif guess > number:
      print("Моє число менше.")
    else:
      print("Ви вгадали! Кількість спроб:", attempts)
