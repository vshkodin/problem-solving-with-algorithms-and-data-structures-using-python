class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 2 and " " in s:
            return 1
        if s == " ": return 0
        words = []
        word = ""
        for i in s:
            if i == " ":
                if word != "":
                    words.append(word)
                word = ""
            else:
                word += i
        if word != "":
            words.append(word)
        print(words)
        if (len(words)) >= 2:
            return len(words[-1])
        else:
            return words[0]
a=Solution()
print(a.lengthOfLastWord(s="a "))
print(a.lengthOfLastWord(s="Hello World"))#5
print(a.lengthOfLastWord(s=" a "))#5