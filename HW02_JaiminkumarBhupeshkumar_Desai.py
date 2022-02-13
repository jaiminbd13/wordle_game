EXPECT_WORD: str = 'AARON'
MAX_TRIAL: int = 6

given_word: list = []
attempt: int = 1

while attempt <= MAX_TRIAL:
    input_word: str = input(f"enter the guess #{attempt}: ").upper()

    if input_word == EXPECT_WORD:
        print("Congratulations...!!")
        break

    if input_word in given_word:
        print("Word already guessed, try again!")
        continue

    if len(input_word) != len(EXPECT_WORD):
        print(f"only {len(EXPECT_WORD)} letters are allowed only!")
        continue

    if not input_word.isalpha():
        print("The word only contain alphabet letters!")
        continue

    attempt += 1
    given_word.append(input_word)

    letter_count: dict = {}
    appraisal = []

    for letter in EXPECT_WORD:
        if letter in letter_count.keys():
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for index in range(len(EXPECT_WORD)):
        if input_word[index] == EXPECT_WORD[index]:
            appraisal.append(' ')
            letter_count[EXPECT_WORD[index]] -= 1
        else:
            appraisal.append('"')

    for index in range(len(EXPECT_WORD)):
        if input_word[index] != EXPECT_WORD[index] and input_word[index] in letter_count:
            if letter_count[input_word[index]] > 0:
                letter_count[input_word[index]] -= 1
                appraisal[index] = "'"

    print(" "*18 + "---" + ''.join(appraisal) + "---")

else:
    print("fail to guess in 6 tries, better luck next time")
