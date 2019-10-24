import random
with open('d.txt','r') as f:
    store=f.read()

store=store.split("    ")
#print(store)


word_store=('choose','convert','glory','MIGHTY','NATION')
choose_word=random.choice(word_store)
choose_word=choose_word.lower()
length_choose=len(choose_word)
show_word={}
index={}
for i in range(length_choose):
    show_word[i]="_" 
   
print(show_word)
print(choose_word)
i=0

g=0
get_input=" "
show_word1=" "
m=0
#get_input=raw_input("WHAT IS THE CHARACTER:")
print(get_input)
while i<length_choose:
    print("YOU HAVE ",length_choose-i," CHANCE")
    get_input=input("WHAT IS THE CHARACTER:")
    get_input=get_input.lower()
    if get_input not in show_word1 and len(get_input)==1:
        
        if get_input in choose_word:
            for j in range(length_choose):
                if get_input==choose_word[j]:
                    show_word[j]=choose_word[j]
                    show_word1+=choose_word[j]
                    index[g]=j
                    g+=1
                    
                    m+=1
            print("YOU CHOOSE RIGHT LETTER AND HAVE NOT LOOSE A CHANCE")
        else:
           
            i+=1
            print("WRONG YOU LOSE A CHANCE")
            hint=input("If you want hint press y")
            if hint in ('y','Y') and g!=0:
                i+=1
                flg1=0
                while flg1!=1:
                    store1=random.choice(store)
                    #print(store1)
                    flg=0
                    while flg!=1:
                        choose_index=random.randrange(length_choose)


                    
                        if (choose_index not in index):
                            flg=1
                            break
                    if choose_word[choose_index] in store1:
                        print("hint is:",store1)
                        flg1=1
                        break      	    
            elif hint in ('y','Y') and g==0:
                i+=1
                flg=0
                while flg!=1: 
                    store1=random.choice(store)                                            
                    choose_index=random.randrange(length_choose)             
                    if choose_word[choose_index] in store1:
                        print("hint is:",store1)	
                        flg=1
                        break   
           
    else:
        if len(get_input)>1:
            print("please give one character at a time.")
        else:
            
            print("YOU have already CHOOSE the letter")
    print(show_word)
    
    if m==length_choose:
        break
    

if(m<length_choose):
    print("Game over","you are dead")
else:
    print("victory")







