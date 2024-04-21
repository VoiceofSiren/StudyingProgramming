'''
https://school.programmers.co.kr/learn/courses/30/lessons/72410
'''

def solution(new_id):
    answer = ''

    step1 = ''
    for i in new_id:
        if 65 <= ord(i) <= 90:
            step1 += chr(ord(i) + 32)
        else:
            step1 += i
    # print(f'step1 = {step1}')

    step2 = ''
    for i in step1:
        if (48 <= ord(i) <= 57) or (97 <= ord(i) <= 122) or i in ('-', '_', '.'):
            step2 += i
        else:
            continue
    # print(f'step2 = {step2}')

    step3 = []
    for i in step2:
        step3.append(i)
        if step3[-2:] == ['.']*2:
            step3.pop()
    # print(f'step3 = {step3}')

    step4 = step3
    if len(step4) > 0:
        if step4[-1] == '.':
            step4[:] = step4[:-1]
    if len(step4) > 0:
        if step4[0] == '.':
            step4[:] = step4[1:]
    # print(f'step4 = {step4}')

    step5 = list_to_str(step4)
    if step5 == '':
        step5 += 'a'
    # print(f'step5 = {step5}')

    step6 = ''
    if len(step5) >= 16:
        step6 += step5[:15]
    else:
        step6 += step5
    step6 = list(step6)

    if len(step6) > 0:
        if step6[-1] == '.':
            step6[:] = step6[:-1]
    # print(f'step6 = {step6}')

    step7 = step6
    length = len(step7)
    if length <= 2:
        last_char = step7[-1]
        step7[:] = step7[:] + [last_char] * (3-length)
    # print(f'step7 = {step7}')

    answer = list_to_str(step7)

    return answer


def list_to_str(str_list):
    new_str = ''
    for string in str_list:
        new_str += string
    return new_str

new_id = input()
print(solution(new_id))

# ...!@BaT#*..y.abcdefghijklm
# z-+.^.
# =.=
# 123_.def
# abcdefghijklmn.p