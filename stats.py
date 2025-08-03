import sys
def get_num_words(): 
    with open(f"/home/sairohit/Bookbot/{sys.argv[1]}") as f:
        f_con = f.read()
        i = 0 
        for j in f_con.split():
            i += 1 
        
    return i

def count_char(): 
    with open(f"/home/sairohit/Bookbot/{sys.argv[1]}") as f:
        f_con = f.read()
        i = {}
        for j in f_con.lower():
            if j not in i:
                x = {j:1}
                i.update(x)
            else:
                i[j] = i[j] + 1
        return(i)  

def get_report(no):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    print (f"Found {no} total words")
    print("--------- Character Count -------")
    cc = count_char()
    sorted_list = sorted(cc.items(), key = lambda item: item[1], reverse= True)
    for i,j in sorted_list: 
        if i.isalpha():
            print (f"{i}: {j}")
    print("============= END ===============")

    
    
        

           
    
        