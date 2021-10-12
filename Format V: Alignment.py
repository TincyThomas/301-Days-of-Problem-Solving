"""left_align = "yourtemplatestringhere"
center_align = "yourtemplatestringhere"
right_align = "yourtemplatestringhere""""


name = "John"

left_align = "My name is {:<30}."
center_align = "My name is {:^30}."
right_align = "My name is {:>30}."

print(left_align.format(name))
print(center_align.format(name))
print(right_align.format(name))
