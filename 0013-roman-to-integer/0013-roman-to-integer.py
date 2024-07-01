class Solution:
    def romanToInt(self, s: str) -> int:
        romanV = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        total = 0

        if 'IV' in s:
            s = s.replace('IV','IIII')
        if 'IX' in s:
            s = s.replace('IX','VIIII')
        if 'XL' in s:
            s = s.replace('XL','XXXX')
        if 'XC' in s:
            s = s.replace('XC','LXXXX')
        if 'CD' in s:
            s = s.replace('CD','CCCC')
        if 'CM' in s:
            s = s.replace('CM','DCCCC')

        for index, element in enumerate(s):
            total = total + romanV[element]

        return total