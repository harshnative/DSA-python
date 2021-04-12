
            midPoint = len(iterator)//2

            left = iterator[:midPoint]
            right = iterator[midPoint:]

            cls.mergeSort(left)
            cls.mergeSort(right)

            i = j = k = 0

            while((i < len(left)) and (j < len(right))):
                if(left[i] < right[i]):
                    iterator[k] = left[i]
                    i = i + 1

                else:
                    iterator[k] = right[j]
                    j = j + 1

                k = k + 1 

            
            while(i < len(left)):
                iterator[k] = left[i]
                i += 1
                k += 1
            

            while(j < len(right)):
                iterator[k] = right[j]
                j += 1
                k += 1
