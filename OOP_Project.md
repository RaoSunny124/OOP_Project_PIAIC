# Student Performance Tracker

This program tracks student performance by calculating their average scores, determining if they are passing, and computing the class average.

---

## **Step 1: Define the `Student` Class**
In this class we defined two attribute `name` and `scores` and defined two actions one is `calculate_average` and other is `is_passing`.

```python
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self):
        passing_score = 40
        return all(score >= passing_score for score in self.scores)
```

## **Step 2: Define the `PerformanceTracker` Class**
We create a other class to find the all class average and in this class we make one attribute is `students` for add student and their scores and we defined three actions `add_student` , `calculate_class_average` and `display_student_performance`.

```python
class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        print("\nStudent Performance Report:")
        for student in self.students.values():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"Student: {student.name}, Average: {average:.2f}, Status: {status}")

        class_average = self.calculate_class_average()
        print(f"\nClass Average: {class_average:.2f}")
```

## **Step 3: Define the `Student_Performance_Tracker()` function**
This function is the body of the `project`.In this function we add `input` for ask the code run or not and use `try` and `except` for `error handling`.

```python
def Student_Performance_Tracker():
    tracker = PerformanceTracker()
    print("Welcome to the Student Performance Tracker!")

    while True:
        try:
            name = input("\nEnter student's name (or type 'done' to finish): ")
            if name.lower().strip() == "done":
                break
            scores = []
            for subject in ["Math", "Science", "English"]:
                while True:
                    try:
                        score = int(input(f"Enter score for {subject}: "))
                        if 0 <= score <= 100:
                            scores.append(score)
                            break
                        else:
                            print("Score must be between 0 and 100. Try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")

            tracker.add_student(name, scores)
            print(f"Added {name}'s scores: {scores}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    tracker.display_student_performance()
```

## **Step 4: Function Calling**
Call the function and calculate the class average.
```python
Student_Performance_Tracker()
```