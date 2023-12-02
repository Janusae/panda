def information():
    import pandas as p
    ask_name = input("Inter your name: ")
    ask_surname = input("Inter your last name: ")
    ask_age = input("Inter your age: ")
    df = p.DataFrame(
        {"Name" : [ask_name] ,
         "Last_name" : [ask_surname] ,
         "Age" : [ask_age]
         }
    )
    done = input("Do you want to see your information: ")
    if done.capitalize() == "Yes":
        print(df)
information()
