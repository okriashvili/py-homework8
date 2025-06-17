print("python functions homework8")
"""დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს მომხმარებლის მიერ შეყვანილ ტექსტს 
   და ამ ტექსტში დათვლის რამდენი სიმბოლო იყო მაღალ რეგისტრში
   შეყვანილი და ასევე ამ ტექსტს გადააქცევს uppercase-ად ანუ მაღალ რეგისტრში დააბრუნებს, მაგალითად, 
   მომხმარებელმა თუ შეიყვანა ტექსტი Hello woRld, 
   ფუნქციამ უნდა დააბრუნოს რომ 2 დიდი ამ ტექსტში და ეს ტექსტი აქციოს HELLO WORLD-ად.
"""
def text():
    input_text = input("enter a text: ")
    count_upper_case = 0

    # uppercase_count = sum(1 for char in input_text if char.isupper())
    for char in input_text:
        if char.isupper():
            count_upper_case += char.isupper()

    upper_case_input_text = input_text.upper()

    return upper_case_input_text, count_upper_case
# print(text())
input_text_in_upper_case, count_upper_case_input_text = text()
print(f"წინადადებაში,მაღალ რესსტრში გვხვდება {count_upper_case_input_text} ასო")
print(f"მაღალ რესტრში გადავაქციეთ სიტყვა {input_text_in_upper_case}")


# დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს ე.წ. camel case ცვლადებს და დააბრუნებს snake case სახით, ანუ თუ გადავცემთ ცვლადს
# firstName დააბრუნებს first_name, name დააბრუნებს ისევ name, preferredFirstName დააბრუნებს preferred_first_name, lastName დააბრუნებს
# last_name და ასე შემდეგ.







































