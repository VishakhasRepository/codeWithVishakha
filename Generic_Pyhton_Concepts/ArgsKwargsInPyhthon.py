# why we  use args and kargs-->when we want to use ma arguments in the method parameters

def special_functions(normalWalaParameter, *argsWalaParameter, **kwargsWalaParameter):
    print(normalWalaParameter)
    for item in argsWalaParameter:
        print(item)
    for key, value in kwargsWalaParameter.items():
        print(f"{key} is a {value}")

normal = "Hello"
listAsTuple = ["Vishakha", "Vishi", "Vishu"]
kwargs = {"Heroine": "Vishakha", "Batch": "2014", "Surname": "Saini"}

special_functions(normal, *listAsTuple, **kwargs)

#normal parameter should always be first parameter then args and kwargs parameter
