_, shift = list(map(int, input().split()))
words = input().split()

print(" ".join(words[shift:] + words[:shift]))
