class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word))+ '#' + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0;

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            # [Start_of_SubString : end of sub string]
            result.append(s[j + 1: j + 1 + length])

            i = j + 1 + length

        return result
            # Step 1: Find the '#' to get length
            # Step 2: Extract the length number
            # Step 3: Skip '#' and read that many characters
            # Step 4: Move i forward

        