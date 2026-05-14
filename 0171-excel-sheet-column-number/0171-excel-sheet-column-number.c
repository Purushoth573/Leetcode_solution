int titleToNumber(char* columnTitle) {
    int result = 0;

    int i = 0;



    while(columnTitle[i] != '\0') {



        result = result * 26 + (columnTitle[i] - 'A' + 1);



        i++;

    }



    return result;


}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna