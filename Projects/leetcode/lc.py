from leetcode_utility import get_leetcode_details_from_username
import pandas as pd
import threading
import pickle

df = pd.read_csv('data.csv')

df_start_limit = 15000
df_end_limit = 16000

df = df.iloc[df_start_limit:df_end_limit]

leetcode_data = list()

total = df.shape[0]
div_size = 200
div_n = total // div_size

divs = list()

for div in range(div_n):
    div_start = df_start_limit + div * div_size
    div_end = div_start + div_size
        
    divs.append(
        df.loc[div_start : div_end - 1 , :]
    )

def thread_function(div):
    for index, row in div.iterrows():

        username = row['username']
        
        response = str()
        try:
            leetcode_details_respnose = get_leetcode_details_from_username(username)

            if type(leetcode_details_respnose) == dict:
                if 'errors' not in leetcode_details_respnose:

                    leetcode_data.append({
                        'username': username,
                        'data': leetcode_details_respnose['data']['matchedUser']
                    })
                    # with open(f'data/lc_{username}.pkl', 'wb') as file:
                        # pickle.dump(leetcode_details_respnose['data']['matchedUser'], file)
        
            response = 'data' if type(leetcode_details_respnose) == dict else 'null'
            
        except Exception as exception:
            response = f'Exception: {exception}'
            
        finally:
            print(f"{index}. {username}: {response}")

threads = list()
for div in divs:
    threads.append(threading.Thread(target = thread_function, args = (div,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print('loaded all')

df_new = pd.DataFrame.from_dict(leetcode_data)
print(df_new.shape)

df_new.to_csv(f'd_{df_end_limit}.csv')