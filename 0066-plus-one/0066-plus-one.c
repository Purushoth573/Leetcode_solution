/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int *res=(int *)malloc(sizeof (int)*(digitsSize+1));
    for (int i=0;i<digitsSize;i++){
        res[i]=digits[i];
    }
    int carry=1;
    for (int i=digitsSize-1;i>=0;i--){
        if(carry==0){
            break;
        }
        if (res[i]==9){
            res[i]=0;
        }
        else{
            res[i]++;
            carry=0;
        }
    }
    if (carry==1){
        res[0]=1;
        for (int i=1;i<=digitsSize;i++){
            res[i]=0;
        }
        *returnSize=digitsSize+1;
    }
    else{
        *returnSize=digitsSize;
    }
    return res;
    
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna