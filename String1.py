greeting="Namaste"
name="Alice"
full_greeting=greeting+', '+name+'!'
print(full_greeting)

formatted_greeting="{}, {}!".format(greeting,name)
formatted_greeting_f=f"{greeting}, {name}!"

print(formatted_greeting)
print(formatted_greeting_f)

text="  Python Programming"

stripped_text=text.strip()
print(stripped_text)

uppercase_text=text.upper()
print(uppercase_text)

starts_with_python=text.startswith("Python")
print(starts_with_python)

replaced_text=text.replace("Programming","Coding")
print(replaced_text)