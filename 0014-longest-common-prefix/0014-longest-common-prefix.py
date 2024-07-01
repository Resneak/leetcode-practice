class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        list1 = []
        count = 0
        isFirst = True



        if len(set(strs)) == 1:
            return strs[0]

        while True:

            

            for index, element in enumerate(strs):

                #list1.append(element[count])

                try:
                    test = list1[index] # error out if element doesn't exist

                    test = test + element[count]
                    list1[index] = test

                except IndexError: # element doesnt exist OR index doesnt exist in word
                    
                    try:
                        list1.append(element[count]) # if element doesn't exist

                    except IndexError: # character index doesn't exist in word

                        if isFirst == True: # index = 0
                            print('here')
                            return ""

                        else:

                            try:

                                test = list1[index] # error out if element doesn't exist

                                test = test + "_"
                                list1[index] = test

                            except IndexError:

                                list1.append("_")


            count = count + 1


            if len(list1) == 1 and '_' in list1[0]:
                return list1[0][:-1]

            elif len(set(list1)) == 1: # every list element is equal to each other
                
                pass # keep going

            elif isFirst == True and count != 1:
                print('here')
                return ""

            else:
                
                

                final = list1[0]

                if final == '_':
                    print('here3')
                    return ""

                elif '_' in final:
                    final = final.strip('_')
                    return final

                else:

                    final = final[:-1]


                    return final

            
            isFirst = False


            