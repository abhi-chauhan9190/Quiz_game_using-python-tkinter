import requests
params={
    'amount':20 ,
    'type' : 'boolean'
}
data=requests.get('https://opentdb.com/api.php',params=params)
data=data.json()




question_data=data['results']
