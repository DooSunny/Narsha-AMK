
class question_db:
    database = []
    def set_create(self): # create new same-meaning set 
        return
    def set_find(self): # is there the keyword in the set?  
        return 
    def set_delete(self): # delete the set that the keyword is existing
        return 
    def keyword_add(self): # add the keyword in the set     
        return  
    def keyword_delete(self): # delete the keyword in the set
        return 
    def key_get(self): # return the key if the keyword is in the database
        return 
   


class answer_db:
    database = []
    # 하나의  딕셔너리에 있는 모든 가중치의 합은 반드시 1이 되어야 함
    # 총 비율을 유지해야 한다는 뜻
    def weight_get(self, keyword): # get the weight of the keyword. 
        return
    def weight_increase(self, keyword): # increase weight of the keyword and adjust other weights
        return  
    def weight_decrease(self, keyword): # decrease weight of the keyword and adjust other weights
        return
    def keyword_add(self, key, keyword): # add keyword to dictionary. need a key to access dictionary
        return
    def keyword_delete(self, key): # delete keyword to dictionary. need a key to access dictionary
        return