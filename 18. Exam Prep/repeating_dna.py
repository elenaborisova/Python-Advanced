def get_repeating_dna(string):
    repeating_subsequences = set()
    index = 0

    while index + 10 < len(string):
        subsequence = string[index:index + 10]
        if subsequence in string[index + 1:]:
            repeating_subsequences.add(subsequence)
        index += 1

    return list(repeating_subsequences)


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_dna(test)
print(result)

test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_dna(test)
print(result)

test = "AAAAAAAAAAA"
result = get_repeating_dna(test)
print(result)
