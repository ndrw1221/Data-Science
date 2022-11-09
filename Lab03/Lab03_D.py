class MyEnumerate():
    def __init__(self, data, label):
        self.data = data
        self.label = label
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.data) != len(self.label):
            print("Data and Lable doesn't match in length")
            raise StopIteration

        if self.index >= len(self.data):
            raise StopIteration

        current_data = self.data[self.index]
        current_label = self.label[self.index]
        self.index += 1

        return self.index-1, current_data, current_label

def main():

    data = [[174, 63], [165, 45], [168, 61], [180, 85], [163, 52]]
    label = ['male', 'female', 'male', 'male', 'female']

    for index, info, target in MyEnumerate(data, label):
        print(f"id:{index} | height:{info[0]} weight:{info[1]} -> {target}")

    # the output should look like the following:
    # id:0 | height:174 weight:63 -> male
    # id:1 | height:165 weight:45 -> female
    # id:2 | height:168 weight:61 -> male
    # id:3 | height:180 weight:85 -> male
    # id:4 | height:163 weight:52 -> female


if __name__ == "__main__":
    main()