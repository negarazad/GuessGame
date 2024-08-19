import random

def guess_number():
    while True:
        number_to_guess = random.randint(1, 10)
        attempts = 5

        print("یک عدد بین ۱ تا ۱۰ در نظر گرفته شده است. شما پنج بار فرصت دارید تا آن را حدس بزنید.")

        for attempt in range(attempts):
            guess = input("حدس شما: ")

            if guess.lower() == "پایان":
                print("بازی به پایان رسید.")
                return

            try:
                guess = int(guess)
            except ValueError:
                print("لطفاً یک عدد صحیح وارد کنید.")
                continue

            if guess < number_to_guess:
                print("عدد حدس زده شده کمتر است.")
            elif guess > number_to_guess:
                print("عدد حدس زده شده بیشتر است.")
            else:
                print("تبریک! شما عدد را درست حدس زدید.")
                break
        else:
            print(f"متاسفانه شما موفق نشدید. عدد مورد نظر {number_to_guess} بود.")

guess_number()
