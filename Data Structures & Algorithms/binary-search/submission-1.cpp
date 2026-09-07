class Solution {
public:
    int search(vector<int>& nums, int target) {
        int p1 = 0;
        int p2 = nums.size() - 1;
        while (true){
            int middleIndex = p1 + ((p2 - p1) / 2);
            int val = nums[middleIndex];
            if (nums[p1] == target){
                return p1;
            }else if (nums[p2] == target){
                return p2;
            }
            if (middleIndex == p1) {
                return -1;
            }
            if (val == target) {
                return middleIndex;
            } else if (val > target) {
                p2 = middleIndex;
            } else {
                p1 = middleIndex;
            }
        }

        return -1;
    }
};
