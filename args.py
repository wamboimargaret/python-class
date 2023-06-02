def my_country(country = "Rwanda"):
    print(f"Hello from {country}")

    # create a function that accepts ant number of intergers and returns the result of multiplying all of them.
def product(nums):
    answer = 1
    for num in nums:
        answer*=num
    return answer

def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")    

# A function named concatenate_args that takes any number of string arguments
#  in positional arguments format and concatenates them into a single string

def concatenate_args(*names):
    answer = ""
    for name in names:
        answer+=name
    return answer    
    

# A function named concatenate_kwargs that takes any number of string arguments in
#  keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**namess):
    result = ""
    for key,value in namess.items():
        result+= value
    return result