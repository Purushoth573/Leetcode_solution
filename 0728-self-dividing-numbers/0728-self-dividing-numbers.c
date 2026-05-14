/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <stdbool.h>
bool isSelfDividing(int n){
    int temp=n,rem=0;
    while (temp>0){
        rem=temp%10;
        if (rem==0 || n%rem !=0){
            return false;
        }
        temp=temp/10;

    }
    return true;
}
int* selfDividingNumbers(int left, int right, int* returnSize) {
    int *arr = (int*)malloc(sizeof(int) * (right - left + 1));
    int i;
    int index = 0;

    for(i = left; i <= right; i++) {

        if(isSelfDividing(i)) {

            arr[index] = i;
            index++;
        }
    }

    *returnSize = index;

    return arr;

    
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna