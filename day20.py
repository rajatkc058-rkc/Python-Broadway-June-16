#error handling
try:
    # print(1/a)
    #print()
    a = "1"
    int(a)
    print(d)
except ZeroDivisionError:
    print("Zero division error")
except ValueError:
    print("value Error")
except:
    print("something went wrong")
finally:
    print("completed")


#error handling
try:
    print(c)
    print(1/1)
    #print()
    a = "ladas"
    int(a)
    
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("completed")


#file handling

    f = open('day2.py','r')
    print(f.read())


f = open ("day17.py","w")
f.write("this is from file mode\n")
f.close()

f = open ('day17.py','a')
f.write('this is from file mode \n')
f.close()

# f = open("day21.text","w")
# f.write('this is me')
# f.close()

# f = open('day22.img','w')
# f.write('this is me')
# f.close()

#error handling
def error_message(file_name, message):
    f = open(file_name,"a")
    f.write(message)
    f.close()
    return True
try:
    print(c)
    print(1/1)
    a = "ladas"
    int(a)
except ZeroDivisionError as e:
    error_message('zero.txt',str(e))
except ValueError as e:
    error_message('value.txt',str(e))
except Exception as e:
    error_message('exc.txt', (e))
finally:
    print("completed")





with open('day2.py','r') as f:
    print(f.read())

    
