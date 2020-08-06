
def word_count(s):
    # Your code here

    cache = {}

    for word in s.split():
        # handle case
        word = word.lower()

        # handle punctuation
        punctuation = '":;,.-+=/\\|[]{}()*^&'
        for ele in word:
            if ele in punctuation:
                word = word.replace(ele, "")

        # look for word in cache
        if word in cache:
        # if found, increment
            cache[word] += 1

        # if not found, create new key-value in cache
        elif word != '':
            cache.update({ word: 1 })

    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))