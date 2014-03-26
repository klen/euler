""" Project Euler problem #17. """


def problem():
    """ Solve the problem.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?.

    Answer: 21124

    """
    cnv = {
        0: '',
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
        12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty', 90: 'ninety'}

    def num_to_words(num, space=' ', hypthen='-'):
        if num == 1000:
            return 'one' + space + 'thousand'

        text = ''
        hundreds, rest = divmod(num, 100)
        if hundreds:
            text = num_to_words(hundreds, space=space, hypthen=hypthen) \
                + space + 'hundred'

            if not rest:
                return text

            text += space + 'and' + space

        if cnv.get(rest):
            return text + cnv[rest]

        tens, rest = divmod(rest, 10)
        text += cnv[tens * 10]
        if rest:
            text += hypthen + cnv[rest]
        return text

    return sum(
        len(num_to_words(n, space='', hypthen=''))
        for n in range(1, 1001))


if __name__ == '__main__':
    print problem()
