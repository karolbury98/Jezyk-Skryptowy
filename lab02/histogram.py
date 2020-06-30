def histogram(tekst):
    dictionary = {}

    for znak in tekst:
        if znak != " ":
            if znak in dictionary:
                dictionary[znak] += 1
            else:
                dictionary[znak] = 1

    return dictionary


print(histogram("Ala ma kota"))