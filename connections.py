import time
class Connections():

    def read(self):
        with open("friendship_test.txt","r") as file:
            read_files = file.readlines()

        rows_data = list()
        for row in read_files:
            rows_data.append(row)

        return rows_data

    def guess(self):
        while True:
            try:
                guess = int(input("Enter a user id to suggest some friends: "))
                break
            except ValueError:
                print("You must be enter a number!")

        return guess

    def file(self):
        rows_list = self.read()
        suggestion = self.guess()
        foundlist = list()
        for row in rows_list:
            row = row.strip()
            inner = list(map(int,row.split("\t")))
            if suggestion == inner[0]:
                foundlist.append(inner[1])
            elif suggestion == inner[1]:
                foundlist.append(inner[0])

        if len(foundlist) < 1:
            print("There is no friend to suggest!")
            time.sleep(1)
        else:
            text = ", ".join([str(x) for x in sorted(foundlist)])
            print(text)
            time.sleep(1)


connection = Connections()
connection.read()
connection.file()