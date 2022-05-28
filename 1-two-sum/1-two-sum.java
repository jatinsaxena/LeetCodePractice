import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hmn = new HashMap<Integer, Integer>();
        int[] arr = new int[2];
        for(int i=0;i<nums.length;i++)
        {
            if(hmn.containsKey(target-nums[i]))
               {
                   arr[0] = hmn.get(target-nums[i]);
                    arr[1]  = i;
               }
              else
               {   
                   hmn.put(nums[i], i);
               }
        }
        return arr;
    }
}