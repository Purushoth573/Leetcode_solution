bool isHappy(int n) {
    int rem,sum;
    while (n!=1 && n!=4){
        sum=0;
        while (n>0){
            rem=n%10;
            sum+=(rem*rem);
            n=n/10;
        }
        n=sum;

    }
    return n==1;
    
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna