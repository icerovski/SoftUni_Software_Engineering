'''
Judge statistics on the last Programing Fundamentals exam were not working correctly, so you have the task of taking all the submissions and analyzing them properly. You should collect all the submissions and print the final results and statistics about each language in which the participants submitted their solutions.
You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". You should store each username and their submissions and points. If a student has two or more submissions for the same language, save only his maximum points.
You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you should remove the user from the contest but preserve his submissions in the total count of submissions for each language.
After receiving "exam finished", print each of the participants in the following format:
"Results:
{username1} | {points}
{username2} | {points}
…
{usernameN} | {points}"
After that, print each language used in the exam in the following format:
"Submissions:
{language1} - {submissions_count}
{language2} - {submissions_count}
…
{language3} - {submissions_count}"
Input / Constraints
Until you receive "exam finished" you will be receiving participant submissions in the following format: "{username}-{language}-{points}"
You can receive a ban command -> "{username}-banned"
The points of the participant will always be a valid integer in the range [0-100];
Output
•	Print the exam results for each participant
•	After that, print each language in the format shown above
•	Allowed working time / memory: 100ms / 16MB
'''


from audioop import reverse


def update_points(user, lang, points):
    if students[user][lang]:
        result = max(students[user][lang], points)
    else:
        result = points
    return result

def update_students(user, lang, points):
    if user not in students:
        students[user] = {}
    if lang not in students[user]:
        students[user] = {lang : []}
    students[user][lang].append(points)
    
def update_submissions(lang):
    if lang not in submissions.keys():
        submissions[lang] = 0
    submissions[lang] += 1

def sort_values(dictionary):
    for language in dictionary.values():
        for scores in language.values():
            scores.sort(reverse=True)
    

students = {}
submissions = {}
while True:
    line = input()
    if line == 'exam finished':
        break
    commands = line.split('-')
    username = commands[0]

    if commands[1] == 'banned':
        del students[username]
    else:
        language = commands[1]
        points = int(commands[2])

        update_students(username, language, points)
        update_submissions(language)

# sort_values(students)

print('Results:')
for name, score in students.items():
    for score_list in score.values():
        max_score = sorted(score_list, reverse=True)[0]
        print(f'{name} | {max_score}')

print('Submissions:')
for k, v in submissions.items():
    print(f'{k} - {v}')
    