import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++)
        {
            int comp = target - nums[i];
            if (map.containsKey(comp))
            {
                return new int[] {map.get(comp), i};
            }
            map.put(nums[i], i);
        }
        return new int[] {-1 , -1};
    };

    public static void main(String[] args) {
        Solution n1 = new Solution();
        int[] answer = n1.twoSum(new int[] {2,7,11,15},9);
        System.out.println("Sum is [" + answer[0] + "," + answer[1] + "]");
    };
}

