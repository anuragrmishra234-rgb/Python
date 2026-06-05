def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_score = (
        combined_names.count("t")
        + combined_names.count("r")
        + combined_names.count("u")
        + combined_names.count("e")
    )

    love_score = (
        combined_names.count("l")
        + combined_names.count("o")
        + combined_names.count("v")
        + combined_names.count("e")
    )

    print(f"{true_score}{love_score}")


# Test
calculate_love_score("Rahul", "Ritu")