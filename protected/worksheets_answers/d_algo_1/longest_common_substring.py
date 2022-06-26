# write function to compare two strings and retrieve longest common sequence length. return integer.
# sequence doesnt not have to be consecutive. But must be in order in both strings.
# eg: Harry and sally share a common sub sequence of "ay"


def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    matrix = [[0 for i in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    return matrix[m][n]
