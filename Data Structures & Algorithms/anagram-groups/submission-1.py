class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_to_int = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 
                        'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 
                        'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 
                        'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 
                        'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 
                        'z' : 25}
        main_dict = {}
        for string in strs:
            string_int = [0] * 26
            for i in string:
                string_int[char_to_int[i]] += 1
            string_int = tuple(string_int)
            if string_int in main_dict:
                main_dict[string_int].append(string)
            else:
                main_dict[string_int] = [string]
        return list(main_dict.values())