def reverse_decorator(function):
    print('Inside reverse_decorator function')
  
    def reverse_wrapper():
        print('Inside reverse_wrapper function')
        return 'Return reverse_wrapper function'
  
    return reverse_wrapper
  
  
@reverse_decorator
def say_hi():
    return 'Inside say_hi'
