import string


def cipher_text(plain_text: str) -> str:
    line = "".join(plain_text.translate(str.maketrans("", "", string.punctuation)).lower().split())
    for r in range(1, len(line)):
        for c in range(1, len(line)):
            if r * c >= len(line) and c >= r and c - r <= 1:
                # I can assume that the first time I get into this condition,
                # that I have the lowest valid possibility

                # Lets create the matrix by iterating over "rows"
                # and slicing the string into "columns"
                table = []
                for i in range(r):
                    row = line[i * c : i * c + c]
                    # we append empty strings if row is smaller than the size of the column
                    table.append(row.ljust(c, " "))

                # now we pivot the table, by constructing the string "column-based"
                final_table = []
                for i in range(c):
                    new_row = ""
                    for j in range(r):
                        new_row += table[j][i]
                    final_table.append(new_row)
                return " ".join(final_table)
    return line
