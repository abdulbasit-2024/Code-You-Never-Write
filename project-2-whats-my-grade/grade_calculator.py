# 1. Input Data
quiz_scores = [85, 60, 90]
midterm_score = 88
target_overall_grade = 90

# 2. Apply Teacher's Rules
# Drop the lowest quiz score
sorted_quizzes = sorted(quiz_scores)
dropped_quiz = sorted_quizzes[0]
valid_quizzes = sorted_quizzes[1:]

# Calculate the average of the remaining quizzes
quiz_average = sum(valid_quizzes) / len(valid_quizzes)

# 3. Calculate Current Weighted Standing (Out of the 70% of the class completed so far)
current_quiz_contribution = quiz_average * 0.40
current_midterm_contribution = midterm_score * 0.30
total_earned_weight = current_quiz_contribution + current_midterm_contribution
completed_class_weight = 0.40 + 0.30

current_percentage = (total_earned_weight / completed_class_weight)

# 4. Calculate Required Final Exam Score
# Formula: Target (90) = Quiz_Weight + Midterm_Weight + (Final_Weight * Final_Score)
required_final_contribution = target_overall_grade - total_earned_weight
required_final_score = required_final_contribution / 0.30

# 5. Print Results clearly
print("--- Grading Analysis ---")
print(f"Dropped Lowest Quiz Score: {dropped_quiz}")
print(f"Quiz Average (After Drop): {quiz_average:.2f}")
print(f"Current Class Grade: {current_percentage:.2f}%")
print("\n--- Target Goal ---")
print(f"To get a final grade of {target_overall_grade}%, you need a score of: {required_final_score:.2f} on the Final Exam.")
