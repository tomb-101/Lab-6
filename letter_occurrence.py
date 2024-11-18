def letter_occurrence(input_string):
    # complete function implementation...
    count=0
    for letter in input_string:
        if letter=="A" or letter=="a":
            count+=1
    return count

# print(letter_occurrence("Always aim ambitiously"))