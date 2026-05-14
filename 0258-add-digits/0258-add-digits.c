int addDigits(int num) {
    int sum,rem;
    while (num>=10){
        sum=0;
        while(num>0){
            rem=num%10;
            sum+=rem;
            num=num/10;
    
        }
        num=sum;
    }
    return sum;
    
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna