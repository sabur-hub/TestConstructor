from testResult import testResult

def checkingResult(root):
    result = []
    user_result = []
    user_mark = 0
    user_percent = 0
    wrong_answer = 0
    with open('result.txt', 'r') as file:
        for elem in file:
            elem = elem.replace('\n', '').strip()
            result.append(elem)
    with open('userResult.txt', 'r') as file:
        for elem in file:
            elem = elem.replace('\n', '').strip()
            user_result.append(elem)

    for elem in range(len(user_result)):
        if result[elem] == user_result[elem]: user_mark += 1

    if user_mark == 0:
        user_percent = 0
        wrong_answer = len(result)
    else:
        user_percent = (user_mark * 100) / len(result)
        wrong_answer = len(result) - user_mark

    testResult(root, [user_mark, wrong_answer, user_percent], result, user_result)
