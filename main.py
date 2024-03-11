
def saver(parameters_: dict = None, results: dict = None, description: str = None) -> None:
    import datetime
    import time
    import json
    import os

    ARTIFACT_PATH = 'd:/Documents/march_kaggle/artifacts/'

    dict_list = [parameters_, results]

    try:
        os.mkdir('../../artifacts')
    except:
        pass

    for dictionary in dict_list:
        total_score = 0
        if dictionary == None:
            continue
        date_time_stamp = datetime.datetime.now().strftime("%d_%b_%H_%M_%S")
        with open(f'{ARTIFACT_PATH}{date_time_stamp}.json', 'w') as file:
            json.dump(dictionary, file)

        for key, value in dictionary.items():
            if type(value) != float:
                break
            total_score += value
        total_score = total_score/7
        with open(f'{ARTIFACT_PATH}description.txt', 'a') as file:
            file.write(
                f'{date_time_stamp}:- score: {total_score}, {description}\n')
        time.sleep(4)
