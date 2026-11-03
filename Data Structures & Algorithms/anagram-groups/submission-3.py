from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            index = [0]*26
            for char in word:
                index[ord(char)-ord('a')] += 1
            anagrams[tuple(index)].append(word)

        return list(anagrams.values())

        # is "c ar anagram of car? as it have an empty space", there are only lowercase english letters?
        # the brute force would be for every word look the rest of the array but this would take O(n²) time but we can
        # do much better by using sorta of a hash and grouping by the similar elements

        # what we can do is, use an array on 26 letters as a index, and count the number of times a char appears in the word, and use as index of the hash, them print the result

        # time complexity O(n * K) for every word we iterate every char
        # space O(n * K) cause we are storing every word in a dict