from data import puzzle_data, example_data
import datetime


data = puzzle_data()

start = datetime.datetime.now()

res = []


class Element:

    def __init__(self, elements):
        self.elements = elements
        self.used_space = sum([ 1 if el is not None else 0 for el in self.elements])
        self.free_space = sum([ 1 if el is None else 0 for el in self.elements])

    def get_elements(self):
        return self.__elements

    def has_space(self, len_elements : int):
        return self.free_space >= len_elements

    def reset_space(self):
        self.used_space = 0
        self.free_space = len(self.elements)
        self.elements = [None for _ in range(len(self.elements))]
    
    def fill_elements(self, elements):

        idx = min([idx for idx in range(len(self.elements)) if self.elements[idx] is None])

        for el in elements:
            self.elements[idx] = el
            idx += 1
        
        self.used_space = sum([ 1 if el is not None else 0 for el in self.elements])
        self.free_space = sum([ 1 if el is None else 0 for el in self.elements])


jdx = 0
for idx, el in enumerate(data):
    
    if idx % 2 == 0 and el != 0:
        res.append(Element([jdx for _ in range(el)]))
        jdx += 1

    if idx % 2 != 0 and el != 0:
        res.append(Element([None for _ in range(el)]))


idx = len(res) - 1
while True:

    current_element = res[idx]
    
    if idx < 0:
        break

    if current_element.used_space != 0:
        for jdx in range(len(res)):
            
            if idx <= jdx:
                break
            
            el = res[jdx]

            if el.has_space(current_element.used_space):
                el.fill_elements(current_element.elements)
                current_element.reset_space()
                break
    
    idx -= 1

ans = []

for e in res:
    ans.extend(e.elements)

ans = sum([idx * el for idx, el in enumerate(ans) if el is not None])
end = datetime.datetime.now()

print("Ans : ", ans) 
print(f"Time taken: {(end - start).total_seconds() * 1000:.2f} ms")