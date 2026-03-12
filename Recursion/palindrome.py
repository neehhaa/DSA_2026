def palindrome(i, word, n):
    if i >= n/2:
        return True

    if word[i] != word[n-i-1]:
        return False

    return palindrome(i+1, word, n-i)

word = "MADAM"
print(palindrome(0,word,len(word)))