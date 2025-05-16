"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    pass
    if operation == "add":
        student = args[0]
        students.append(student)
    elif operation == "remove":
        student = args[0]
        if student in students:
            students.remove(student)
        else:
            print(f"学生 {student} 不在列表中，无法删除。")
    elif operation == "update":
        idx = args[0]
        new_student = args[1]
        if idx in students:
            students[students.index(idx)] = new_student
        else:
            print(f"索引 {idx} 超出范围，无法更新。") 
    else:

        print("无效的操作类型，请选择 'add', 'remove' 或 'update'。")
    return students 