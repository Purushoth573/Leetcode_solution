/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int *arr=malloc(2*sizeof(int));
    *returnSize=2;
    for (int i=0;i<=numsSize-1;i++){
        for (int j=i+1;j<numsSize ;j++){
            if(nums[i]+nums[j]==target){
                arr[0]=i;arr[1]=j;
                return arr;
            }
        }
    
    }
    return arr;
    
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna