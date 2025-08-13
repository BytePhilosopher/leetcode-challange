from collections import deque

class Solution(object):
    def countStudents(self, students, sandwiches):
        students = deque(students)  # queue
        sandwiches = deque(sandwiches)  # stack (leftmost is top)
        
        fail_count = 0  # track consecutive failures

        while students and fail_count < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                fail_count = 0  # reset because a student ate
            else:
                students.append(students.popleft())  # move front to back
                fail_count += 1  # one more fail in a row

        return len(students)  # number of students who can't eat
