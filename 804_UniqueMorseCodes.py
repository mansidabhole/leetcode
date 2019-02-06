class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        unique=words
        morse=set()
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in range(len(words)):
            morse.add(''.join(code[ord(words[i][c])-97] for c in range(len(words[i]))))
        return len(morse) 