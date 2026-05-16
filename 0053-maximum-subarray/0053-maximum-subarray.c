int max(int a, int b){
    return a>b? a:b;
}
int maxSubArray(int* nums, int numsSize) {
    if (numsSize == 0){return 0;
    }
    int max_so_far=nums[0];
    int max_ending_here=nums[0];
    for (int i=1 ; i<numsSize;i++){
        max_ending_here=max(nums[i],max_ending_here+nums[i]);
        max_so_far=max(max_so_far,max_ending_here);
    }
    return max_so_far;

    
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna