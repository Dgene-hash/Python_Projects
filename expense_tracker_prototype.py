try:
    number=int(input("How many expenses?: "))
except ValueError:
    print("Invalid Input")
else:
    if number<0:
        print("Invalid Expense Count")
        exit()
    elif number==0:
        print("Please enter at least 1 expense")
        exit()
    else:
        def collect_expenses(data):
            array=[]
            i=1
            while i<=data:
                try:
                    expense=float(input("Enter expense: "))
                    if expense<0:
                        print("Invalid Input")
                        continue
                except ValueError:
                    print("Invalid Input")
                else:
                    category=input("Enter Category: ")
                    category=category.lower()
                    i+=1
                    array.append([expense,category])
            return array
        array=collect_expenses(number)
        def expense_summary(data):
            highest_expense=data[0][0]
            lowest_expense=data[0][0]
            total=0
            for n in data:
                total+=n[0]
                if highest_expense<n[0]:
                    highest_expense=n[0]
                if lowest_expense>n[0]:
                    lowest_expense=n[0]
            average_expense=total/len(data)
            return total,highest_expense,lowest_expense,average_expense
        total,highest,lowest,average=expense_summary(array)
        try:
            budget=int(input("Enter Monthly Budget: "))
        except ValueError:
            print("Invalid Input")
            exit()
        else:
            def budget_checker(total,b):
                if b<=0:
                    return "Invalid budget"
                else:
                    if total<b:
                        return f"Monthly Budget: {b}\nTotal Expenses: {total}\n\nStatus: Within Budget\nRemaining Budget: {b-total}"
                    elif total==b:
                        return f"Monthly Budget: {b}\nTotal Expenses: {total}\n\nStatus: Budget Fully Used\nRemaining Budget: {b-total}"
                    else:
                        return f"Monthly Budget: {b}\nTotal Expenses: {total}\n\nStatus: Budget Exceeded\nRemaining Budget: {b-total}"
            array1=budget_checker(total,budget) 
            print(array1)
            if array1=="Invalid budget":
                exit()
            search=input("Enter category to search: ")
            search=search.lower()
            def search_expenses(s,t):
                full=[]           
                for a in t:
                    if a[1]==s:
                        full.append(a)
                if not full:
                    return "No expenses Found"
                else:
                    return full
            result=search_expenses(search,array)
            print(result)        



