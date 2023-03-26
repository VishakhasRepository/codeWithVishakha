import datetime as dt


class Employee:
    def __init__(self, id: str, gender: str, salary: int, perfomance_rating: int):
        self.id, self.gender, self.salary, self.perfomance_rating = id, gender, salary, perfomance_rating

    def get_id(self):
        return self.id

    def get_gender(self):
        return self.gender

    def get_salary(self):
        return self.salary

    def get_perf_rat(self):
        return self.perfomance_rating


class JoiningDetail(Employee):
    def __init__(self, id: str, gender: str, salary: int, perfomance_rating: int, date: dt.date):
        super().__init__(id, gender, salary, perfomance_rating)
        self.date = date

    def get_DoJ(self):
        return self.date

    def __str__(self):
        return f"id {self.id} : {self.date}"


class Information:
    def __init__(self, e_list):
        self.e_list = e_list

    def readData(self):
        N = len(self.e_list)
        for i in range(N - 1):
            for j in range(N - i - 1):
                if self.e_list[j].get_perf_rat() > self.e_list[j + 1].get_perf_rat():
                    self.e_list[j], self.e_list[j + 1] = self.e_list[j + 1], self.e_list[j]

        for i in range(3):
            for j in range(2 - i):
                if self.e_list[j].get_DoJ() > self.e_list[j + 1].get_DoJ():
                    self.e_list[j], self.e_list[j + 1] = self.e_list[j + 1], self.e_list[j]

        return '\n'.join(list(map(str, self.e_list[:3])))



temp = [('1', 'm', 10, 5, dt.date(2000, 10, 30)), ('2', 'f', 5, 3, dt.date(2001, 10, 12)), ('3', 'm', 100, 10, dt.date(1998, 10, 1))]
lst = Information([JoiningDetail(*i) for i in temp])
print(JoiningDetail.get_DoJ())
print(lst.readData())