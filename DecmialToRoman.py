roman_dic={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
exception_dic = {4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
exception_list=[4,9,40,90,400,900]
roman_list=[1,5,10,50,100,500,1000,4000]
def checkwhere(n):
    temp=1
    if(n!=9):
        for i in range(len(roman_list)):
            if(roman_list[i]>n):
                temp=roman_list[i-1]
                diveder = n//temp
                mod = n%temp
                return {"temp":temp,"diveder":diveder,"mod":mod}
    else:
        return {"temp":1,"diveder":9,"mod":0}
            
   
try:
    cnvtdectoroman=int(input("Convert Decimal to Roman (1:3999): "))

    if(cnvtdectoroman <=0 or cnvtdectoroman>=4000):
        print("Please give input in limit")
    else:
        result_dic = {"temp":0,"diveder":0,"mod":cnvtdectoroman}


        output = ""
        while(result_dic.get("mod")!=0):
            result_dic= checkwhere(result_dic.get("mod"))
            var = result_dic.get("temp")*result_dic.get("diveder")
            if(var in exception_list):
                output+=exception_dic.get(var)
            else:
                output+=(roman_dic.get(result_dic.get("temp"))*result_dic.get("diveder"))

        print(output)

except:
  print("Pls Enter Intger")