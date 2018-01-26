
phonebook={"jhone":2345785776, "jill":463663875 , "jack":676776778785 ,"jessy":3565365}
print phonebook
i=raw_input("enter the the i to delete")
if i in phonebook:
    del phonebook[i]
    print "delete"
else:
    print "i doesnt exits"
    
