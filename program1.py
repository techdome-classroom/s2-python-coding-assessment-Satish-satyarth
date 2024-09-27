class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        function romanToInt(s) {
    // Dictionary for Roman numeral values
    const romanDict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };

    let total = 0;

    // Loop through the Roman numeral string
    for (let i = 0; i < s.length; i++) {
        // If the current Roman numeral is smaller than the next one, subtract it
        if (i + 1 < s.length && romanDict[s[i]] < romanDict[s[i + 1]]) {
            total -= romanDict[s[i]];
        } else {
            // Otherwise, add its value to the total
            total += romanDict[s[i]];
        }
    }

    return total;
}

        pass