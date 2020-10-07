#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    //create a variable to store the string "text"
    string text = get_string("Text: ");
    //find the length of the string
    int n = strlen(text);
    //set a variable counter for letters, words and sentences. Word counter may start at 1 as the
    int L = 0;
    int W = 1;
    int S = 0;
    // Create a string to print the case grade is 16+
    char advanced[4] = {"16+"};
    char remedial[45] = {"Before Grade 1"};

    printf("Reading level\n");

    //count the number of letter, words and sentences
    for (int i = 0; i < n ; i++)
    {
        //count the number of letters
        if (isalpha(text[i]))
        {
            L++;
        }
        //count the number of words by counting spaces and correcting for double spaces
        if (text[i] == ' ' && text[i - 1] == ' ')
        {
            W--;
        }
        if (text[i - 1] == 32)
        {
            W++;
        }
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            S++;
        }
    }
    //calculate readability
    float av_L = 100 / ((float) W / (float) L);
    float av_S = 100 / ((float) W / (float) S);
    float index_t = (0.0588 * av_L) - (0.296 * av_S)  - 15.8;
    int index =  round(index_t);

    if (index >= 16)
    {
        printf("Grade %s\n", advanced);
        return 0;
    }
    if (index < 1)
    {
        printf("Grade %s\n", remedial);
        return 0;
    }

    printf("Grade %i\n", index);
    return 0;
}
