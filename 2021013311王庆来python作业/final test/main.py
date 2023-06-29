import importlib

def run_assignment(assignment_number):
    assignment_file = f"assignment{assignment_number}.py"
    try:
        module = importlib.import_module(assignment_file[:-3])
        module.run_example()
    except ModuleNotFoundError:
        print(f"Assignment {assignment_number} not found.")
    except AttributeError:
        print(f"Example function not found in Assignment {assignment_number}.")

while True:
    assignment_number = input("请输入要求展示的作业号（1、2或3），输入 q 退出：")
    if assignment_number == 'q':
        break
    if assignment_number in ['1', '2', '3']:
        run_assignment(assignment_number)
    else:
        print("无效的作业号，请重新输入。")
