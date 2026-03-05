def fix_sequence(sequence_list: list):
    fixed_sequence = []
    for item in sequence_list:
        if str(item).isnumeric():
            fixed_sequence.append(item)

    return fixed_sequence


def is_sequence_valid(iterable) -> bool:
    valid = True

    for i in iterable:
        print("Now checking:", i)
        if not str(i).isnumeric():
            valid = False
            break
    return valid


if __name__ == "__main__":
    seq = input("Type Seq. >> ").replace(" ", "").split(",")
    seq = fix_sequence(seq)

    if is_sequence_valid(seq):
        print("Válida!")
    else:
        print("Sequência inválida.")

    print(seq)
