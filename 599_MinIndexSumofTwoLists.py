class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        rest=dict()
        small=len(list1)+len(list2)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    if i+j==small:
                        rest[list1[i]]=i+j
                    elif i+j<small:
                        rest[list1[i]]=i+j
                        small=i+j
        answer=[key for key in rest.keys()]
        return answer
                -