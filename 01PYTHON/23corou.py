def searcher():
    import time
    # Some 4 seconds time consuming time
    book="This is a book on harry and code with harry"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("your text in book")
        else:
            print("Text is not in book")
        
search=searcher()
print("Search Started")
next(search)
print("Next method Run")
search.send("harry")

# search.close()
# search.send("harry")

input("Press any key")
search.send("harry and")
input("Press any key")
search.send("this is ")
input("Press any key")
search.send("joker")
input("Press any key")
search.send("like")