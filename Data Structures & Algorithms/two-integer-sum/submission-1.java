class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> comp = new HashMap();

        for(int i=0;i<nums.length;i++) {
            int diff = target - nums[i];
            if(comp.containsKey(diff)) {
                return new int[] { comp.get(diff), i};
            }
            comp.put(nums[i], i);
        }

        return new int[] {};
    }
}
