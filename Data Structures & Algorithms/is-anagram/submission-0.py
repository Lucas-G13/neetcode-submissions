class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_dict1 = {}
        for i in s:
            str_dict1[i] = str_dict1[i] + 1 if i in str_dict1 else 1
        str_dict2 = {}
        for i in t:
            str_dict2[i] = str_dict2[i] + 1 if i in str_dict2 else 1
        return str_dict1 == str_dict2