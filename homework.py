total_homework = 4
original_count = total_homework
print(f"you have {original_count} homework tasks to finish today\n")
completed_count = 0
task_num = 1
while task_num <= total_homework:
    if task_num == 1:
        next_task = "math worksheet"
    elif task_num == 2:
        next_task = "science reading"
    elif task_num == 3:
        next_task = "english writing"
    else:
        next_task = "coding practice"
    answer = input(f"have you finished: {next_task}? (yes/no): ")
    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("great job homework task completed.")
    else:
        print("okay finish it and check again")
 
    # PART 6: Print how many homework tasks remain
    print("homework tasks remaining:", total_homework - completed_count)
    print()
print("all homework completed")
print("great work finishing your homework today\n")
print("now lets safely peek at an infinite loop")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("this condition never changes so it would run forever")
    safety_counter += 1
    if safety_counter == 3:
        print("(stopping here on purpose - a real infinite loop never stops on its own)")
        break
print("\nhomework completion summary")
print("homework assigned today:", original_count)
print("homework completed:", completed_count)
print("homework remaining:", total_homework - completed_count)