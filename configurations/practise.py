class Practise:
    def prime(self):
        a = int(input())
        b = int(input())
        l1=[]
        for i in range (a,b):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                l1.append(i)
        print(l1)

    def sorting(self):
        a= int(input())
        l1=[]
        for i in range(a):
            b=int(input())
            l1.append(b)
        for j in range(0,len(l1)):
            for k in range(j,len(l1)):
                if l1[j]>=l1[k]:
                        temp=l1[j]
                        l1[j]=l1[k]
                        l1[k]=temp
        print(l1)


    def sort_the_zeroes(self):
        a=int(input())
        l1=[]
        for i in range (a):
            b=int(input())
            l1.append(b)

        pointer=0
        for j in range(0,len(l1)):
            if l1[j]!=0:
                temp=l1[pointer]
                l1[pointer]=l1[j]
                l1[j]=temp
                pointer+=1

        print(l1)

    def pelendrome(self):
        a = int(input())
        rev = 0
        x = a

        while (a > 0):
            rev = (rev*10)+a % 10
            a = a//10

        if rev==x:
            print("pelendroem")

        else:
            print("kfsvsmcj k")

    def permutation(self):
        nums = [0,2,1,5,3,4]
        ans=[]
        for i in range(len(nums)):
            value=nums[nums[i]]
            ans.append(value)

obj = Practise()
#obj.prime()
#obj.sorting()
#obj.sort_the_zeroes()
obj.permutation()
