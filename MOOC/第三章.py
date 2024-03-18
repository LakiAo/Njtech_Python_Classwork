score = int(input())
print('Excellent' if 90 <= score <= 100 else 'Good' if 80 <= score < 90 else 'Passed' if 60 <= score < 80 else 'Failed' if 0 <= score < 60 else 'Error')