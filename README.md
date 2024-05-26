# impact_analytics
Probability calculation 


# Question
In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

 

  Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773

# Solution:

inference from the questions:
1. You are not allowed to miss classes for four or more consecutive days.
2. The graduation ceremony is on the last day, which is the N-th day.

we need to:
1. Calculate the total number of valid attendance sequences over N days.
2. Calculate the number of valid attendance sequences where you miss the graduation ceremony on the N-th day.

suppose:
A(n): The number of valid attendance sequences of length n.
B(n): The number of valid attendance sequences of length n that end with a missed class on the n-th day.


Calculating A(n):
To find A(n), we note that the valid sequences of length n can end in different ways:
- Attend on the n-th day: The previous n−1 days must form a valid sequence of *length n−1*
- Miss the n-th day (we can miss up to three consecutive days, but not four):
    - Miss one day: The first n−1 days must be a valid sequence.
    - Miss two days: The first n−2 days must be a valid sequence.
    - Miss three days: The first n−3 days must be a valid sequence.

This gives us the recurrence relation:
A(n) = A(n-1) + A(n-2) + A(n-3) + A(n-4)


Calculating B(n):
A valid sequence ending in a missed day could end in 1 to 3 missed days:
- End in one missed day: The firs n-1 days form a valid sequence.
- End in one missed day: The firs n-2 days form a valid sequence.
- End in one missed day: The firs n-3 days form a valid sequence.

This gives us the recurrence relation:
B(n) = A(n-1) + A(n-2) + A(n-3)


Initialization:

For n less than 4, we can directly enumerate the valid sequences:
For A:
A(0)=1 (an empty sequence is trivially valid)
A(1)=2 (A or M)
A(2)=4 (AA, AM, MA, MM)
A(3)=8 (AAA, AAM, AMA, AMM, MAA, MAM, MMA, MMM)

For 𝐵:
B(0)=1 (M)
B(1)=2 (MM, AM)
B(2)=4 (MMA, MAM, AMM, MMM)

=> Refer Code prob.py