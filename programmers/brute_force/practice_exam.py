def solution(answers):
    
    problems_count = len(answers)
    
    mg1 = (1, 2, 3, 4, 5)
    mg2 = (2, 1, 2, 3, 2, 4, 2, 5)
    mg3 = (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    
    points = {}

    for idx, mg in enumerate([mg1, mg2, mg3]):
        q = problems_count // len(mg)  
        m = problems_count % len(mg)
        mg_submit = (mg * q) + mg[:m] 

        mg_point = 0
        cpr = zip(mg_submit, answers)
        for s, a in cpr:
            if s == a:
                mg_point += 1
        points[idx+1] = mg_point

    result = []
    max_score = max(points.values())
    for key, value in points.items():
        if value == max_score:
            result.append(key)

    return result

if __name__ == "__main__":
    answer = solution([1,3,2,4,2])	
    print(answer)
    assert answer == [1,2,3]