import string
# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressing", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_word(text, phrase_word):
    test_chars = string.punctuation + ' '
    for char in test_chars:
        text = text.replace(phrase_word + char, '*' * len(phrase_word) + char)
        text = text.replace(phrase_word.capitalize() + char, '*' * len(phrase_word) + char)
        text = text.replace(phrase_word.upper() + char, '*' * len(phrase_word) + char)


    return text

email_one_censored = censor_word(email_one, 'learning algorithms')

def censor_from_list(text, lst):
    for word in lst:
        text = censor_word(text, word)

    return text

email_two_censored = censor_from_list(email_two, proprietary_terms)

def censor_negative_words(text, lst, negative_lst):
    text = censor_from_list(text, lst)
    negative = False

    for word in text.split():
        if word in negative_lst:
            negative_lst.remove(word)
            if negative:
                text = censor_from_list(text, negative_lst)
            else:
                negative = True

    return text

email_three_censored = censor_negative_words(email_three, proprietary_terms, negative_words)

def censor_multiple_words(text, lst, negative_lst):
    text = censor_negative_words(text, lst, negative_lst).splitlines()
    new_email = []

    for line in text:
        line = line.split()
        temp_line = []

        for i in range(len(line)):
            if '**' in line[i - 1]:
                continue
            if '**' in line[i]:
                temp_line.append('*' * len(line[i - 1]))
                temp_line.append(line[i])
                temp_line.append('*' * len(line[i + 1]))
            else:
                temp_line.append(line[i])

        if len(temp_line) == 0:
            temp_line = '\n'
        else:
            temp_line[-1] += '\n'

        new_email.append(' '.join(temp_line))

    return ''.join(new_email)


email_four_censored = censor_multiple_words(email_four, proprietary_terms, negative_words)