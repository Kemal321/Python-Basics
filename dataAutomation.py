def swap_case(s):
    news = ""
    for i in s:
        if i.islower():
            news += i.upper()
        else:
            news += i.lower()
    return news

print(swap_case('HackerRank.com presents "Pythonist 2".'))