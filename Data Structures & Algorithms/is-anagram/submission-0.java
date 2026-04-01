class Solution {
    public boolean isAnagram(String s, String t) {
        int[] charCount = new int[26];
        for(char c:s.toCharArray()) charCount[c -'a']++;
        for(char c:t.toCharArray()) charCount[c -'a']--;

        for(int c : charCount) {
            if(c!=0) return false;
        }

        return true;
    }
}
