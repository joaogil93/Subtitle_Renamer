def ChooseOption(TypeofPick):

    if TypeofPick == 'Subtitle':
        TypeOptions = ['.srt']
        input_message = "Whats the substitles file type?\n"

    elif TypeofPick == 'VideoFileType':
        TypeOptions = ['.mp4','mkv']
        input_message = "Whats the video file type?\n"
    
    elif TypeofPick == 'Language':
        TypeOptions = ['English']
        input_message = "Whats the subs language?\n"

    else:
        exit

    user_input = ''

    for index, item in enumerate(TypeOptions):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Your choice: '

    while user_input not in map(str, range(1, len(TypeOptions) + 1)):
        user_input = input(input_message)

    TypeOptions = TypeOptions[int(user_input) - 1]

    return(TypeOptions)