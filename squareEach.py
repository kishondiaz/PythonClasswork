##name: Kishon Diaz
##program name:squareEach.py

def squareEach(nums):
    for i in nums:
        squared = []
        newS = []
        newJ = ""
        w,x,y,z = nums[0],nums[1],nums[2],nums[3]
        squared = [w**2,x**2,y**2,z**2]
        newS = str([squared])
        newJ= newS.replace(",", "").replace("]", " ").replace("["," ")
    print("Squared numbers",newJ)
def main():
    print("Numbers are 3,6,4,5 ")
    numlist =[3,6,4,5]
    getsum = squareEach(numlist)

if __name__ =="__main__":
    main()
