class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length;
        int[] res = new int[2];

        if (len <= 2) {
            res[0] = 0;
            res[1] = 1;
            return res;
        }

        for (int i=0; i < len; i++) {
            for (int j=i + 1; j < len; j++) {
                if ((nums[i] + nums[j]) == target) {
                    res[0] = i;
                    res[1] = j;
                    break;
                }
            }
        }

        return res;
    }

    public static void main(String []args) {
        Solution t = new Solution();

        int[] nums = {1, 2, 5, 7, 15};
        int target = 8;

        int[] res = t.twoSum(nums, target);
        System.out.println("Resultado: " + res[0] + " - " + res[1]);
    }
}


