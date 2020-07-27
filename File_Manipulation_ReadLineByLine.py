def readingLines():
    count = 0

    try:
        with open('system_config.txt') as file_object:
            contents = file_object.readlines()
            for line in contents:
                count += 1
                print("Line " + str(count) + ": " + line)
    except FileExistsError as booboo:

        print("We had a booboo!!"
        print(booboo)


readinglines()              
            

