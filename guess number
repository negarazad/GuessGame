import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    attempts = 5

    print("یک عدد بین ۱ تا ۱۰ در نظر گرفته شده است. شما پنج بار فرصت دارید تا آن را حدس بزنید.")

    for attempt in range(attempts):
        guess = int(input("حدس شما: "))

        if guess < number_to_guess:
            print("عدد حدس زده شده کمتر است.")
        elif guess > number_to_guess:
            print("عدد حدس زده شده بیشتر است.")
        else:
            print("تبریک! شما عدد را درست حدس زدید.")
            return

    print(f"متاسفانه شما موفق نشدید. عدد مورد نظر {number_to_guess} بود.")

guess_number()
