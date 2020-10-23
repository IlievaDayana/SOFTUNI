def reverse(string):
    text_elements = [i for i in string]
    new = []
    while text_elements:
        element_to_add = text_elements.pop()
        new.append(element_to_add)
    return "".join(new)

print(reverse(input()))

