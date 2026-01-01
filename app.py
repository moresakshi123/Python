#LIST
l1=[]
print("1.List\n2.Tuple\n3.Set\n4.Dictionary\n5.String\n6.Exit")
ch=int(input("Enter your choice:"))


if ch == 1:
        print("\n--- LIST MENU ---")
        print("1.Create List\n2.Addition\n3.Deletion\n4.Exit")
        opt = int(input("Enter your choice in List: "))


        if opt == 1:
            value = input("Enter numbers separated by space: ").split()
            l1.clear()
            l1.extend([int(i) for i in value])
            print("List created:", l1)


        elif opt == 2:
          print("\na. Append an element")
          print("b. Insert an element at a specific position")
          print("c. Extend the list")

          i = input("Enter your choice: ").lower()

          if i == 'a':
            value = int(input("Enter a number to append: "))
            l1.append(value)
            print("Updated list:", l1)

          elif i == 'b':
            index = int(input("Enter index position: "))
            value = int(input("Enter number to insert: "))
            l1.insert(index, value)
            print("Updated list:", l1)

          elif i == 'c':
            values = input("Enter multiple numbers separated by space: ").split()
            l1.extend([int(x) for x in values])
            print("Updated list:", l1)
          else:
            print("Invalid option")

        elif opt==3:
          if not l1:
            print("Create a list first")
          else:
            print("a. Pop an element")
            print("b. Remove an element at a specific position")
            print("c. Clear")
            print("d. Delete the list")

            i= input("Enter your choice:")

            if i=='a':
              value=int(input("Enter a number: "))
              l1.pop(value)
              print("List after Poping element:",l1)
            elif i=='b':
              value=int(input("Enter a number to remove from list: "))
              l1.remove(value)
              print("Updated list:",l1)
            elif i=='c':
              value=int(input("Enter a number:"))
              l1.clear(value)
              print("Updated list:",l1)
            elif i=='d':
              del l1
              print("Deleted the list")
            else:
              print("Invalid Option")


        elif opt==4:
          print("Exit")
        else:
          print("Invalid number.Try between 1 to 4")


#TUPLE
          l2=()
          print("\n  Tuple Menu  ")
          print("1.Create Tuple\n2.Add\n3.Deletion\n4.Exit")
          opt=int(input("Enter your choice in list:"))
          if opt==1:
             value=input("Enter a list of numbers you want in your tuple seperated by space:").split()
             print("Tuple created:",l2)
          elif opt==2:
             print("Tuple is immuatable")
          elif opt==3:
             print("Tuple is immutable")
          elif opt==4:
             print("Exit")
          else:
             print("Invalid number.Try between 1 to 4")


#SET
             l3=set()
             print("1.Create Set\n2.Add\n3.Deletion\n4.Exit")
             opt=int(input("Enter your choice in Set: "))
             if opt==1:
               value=input("Enter a list of numbers you want in your set seperated by space:").split()
               l3=set(value)
               print("Set created:",l3)
             elif opt==2:
                if not l3:
                   print("Create a set first")
                else:
                   print("a. Add an element")
                   print("b. Update the set")

                   i= input("Enter your choice:")

                   if i=='a':
                     value=int(input("Enter a number to add in list: "))
                     l3.add(value)
                     print("After Addition:",l3)
                   elif i=='b':
                      value=input("Enter multiple values to add in set :").split()
                      l3.update(value)
                      print("Updated set:",l3)
                   else:
                      print("Invalid option")

             elif opt==3:
                if not l3:
                  print("Create a set first")
                else:
                  print("a. Remove an element")
                  print("b. Discard an element")
                  print("c. Clear")
                  print("d. Delete the list")

                  i= input("Enter your choice:")

                  if i=='a':
                    value=int(input("Enter a number to remove in set: "))
                    l3.remove(value)
                    print("After removal:",l3)
                  elif i=='b':
                    value=int(input("Enter a number to discard in set: "))
                    l3.discard(value)
                    print("Updated set:",l3)
                  elif i=='c':
                    value=int(input("Enter a number to clear in set: "))
                    l3.clear(value)
                    print("Updated set:",l3)
                  elif i=='d':
                    del l3
                    print("Deleted the set")
                  else:
                    print("Invalid Option")

  #DICTIONARY
                    l4={}
                    print("\n  Dictionary Menu  ")
                    print("1.Create Dictionary\n2.Add\n3.Deletion\n4.Exit")
                    opt=int(input("Enter your choice in Dictionary: "))
                    if opt==1:
                      value=input("Enter a list of numbers you want in your dictionary seperated by space:").split()
                      l4={}
                      print("Dictionary created:",l4)

                    elif opt==2:
                      if not l4:
                        print("Create a dictionary first")
                      else:
                        print("a. Add an element")
                        print("b. Update the dictionary")

                        i= input("Enter your choice:")

                        if i=='a':
                          value=int(input("Enter a number to add : "))
                          l4.add(value)
                          print("After Addition:",l4)
                        elif i=='b':
                           value=input("Enter multiple values to add :").split()
                           l4.update(value)
                           print("Updated dictionary:",l4)
                        else:
                           print("Invalid option")

                    elif opt==3:
                      if not l4:
                        print("Create a dictionary first")
                      else:
                        print("a. Pop an element")
                        print("b. Popitem an element")
                        print("c. Clear")
                        print("d. Delete the dictionary")

                        i= input("Enter your choice:")

                        if i=='a':
                          value=int(input("Enter a number to pop in list: "))
                          l4.pop(value)
                          print("After removal:",l4)
                        elif i=='b':
                          value=int(input("Enter a number: "))
                          l4.popitem(value)
                          print("Updated list:",l4)
                        elif i=='c':
                          value=int(input("Enter a number :"))
                          l4.clear(value)
                          print("Updated list:",l4)
                        elif i=='d':
                          del l4
                          print("Deleted the Dictionary")
                        else:
                          print("Invalid Option")

             elif opt==4:
                print("Exit")
             else:
                print("Invalid number.Try between 1 to 4")

