#!/usr/bin/env python3


def compare_triplets(a, b):
    a_score = 0
    b_score = 0
    for index, val in enumerate(a):
        if b[index] > val:
            b_score += 1
        if b[index] < val:
            a_score += 1
    return [a_score, b_score]


def test_compare_triplets(a, b, expected_output):
    print('Testing with ' + str(a) + ' and ' + str(b))
    print('Expected output: ' + str(expected_output))
    result = compare_triplets(a, b)
    print('Result: ' + str(result))
    assert(expected_output == result), 'Test failed!!!'


def main():
    test_compare_triplets([1, 37, 23], [3, 8, 89], [1, 2])
    test_compare_triplets([6, 7, 8], [3, 7, 89], [1, 1])
    test_compare_triplets([11, 66, 0], [54, 8, 12], [1, 2])


if __name__ == '__main__':
    main()
