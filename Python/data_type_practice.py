

#튜플 tuple 연습

my_tuple1 = ()
print(my_tuple1)

my_tuple2 = (1)
print(my_tuple2) # 1

#단일 요소 튜플을 만들때는 반드시 후행 쉼표 (1,) 식으로 만들어야함

my_tuple3 = (1,)
print(my_tuple3)

s = "apple"

result = s[1:4] # ppl
print(result)

x = 'Hello'
print(x[::-1])

my_dict = {"a": 1, "b": 2}
my_dict["a"] = 3
print(my_dict)

r = range(2, 10, 2)
print(list(r))

y = 0
print(y or 5)
# 5출력함
print( 3 or 7 )
#왼쪽부터 평가 진행 후 3이 0이 아니므로 참. or 조건을 이미 만족하므로 뒤는 평가 안하고 3반환 후 종료

print(7 <= 7)


#복잡한 자료구조
'''

data = [{'has_more': False,
  'next_cursor': None,
  'object': 'list',
  'page_or_database': {},
  'request_id': 'a5163fff-758f-45ea-b6fb',
  'results': [{'archived': False,
               'cover': None,
               'created_by': {'object': 'user'},
               'created_time': '2023-06-15T04:29:00.000Z',
               'icon': None,
               'last_edited_by': {'object': 'user'},
               'last_edited_time': '2023-12-12T09:19:00.000Z',
               'object': 'page',
               'parent': {'type': 'database_id'},
               'properties': {'setNum': {'id': '%7DK%40%5C',
                                         'number': 1,
                                         'type': 'number'},
                              '과목': {'id': 'YuIE',
                                     'multi_select': [{'color': 'default',
                                                       'name': 'Python'}],
                                     'type': 'multi_select'},
                              '구분': {'id': '%40%3EmR',
                                     'select': {'color': 'purple',
                                                'name': '실습'},
                                     'type': 'select'},
                              '단계': {'id': 'T%7B%7BP',
                                     'select': {'color': 'default',
                                                'name': '3'},
                                     'type': 'select'},
                              '문제번호': {'id': 'uEBt',
                                       'number': 1431,
                                       'type': 'number'},
                              '제목': {'id': 'title',
                                     'title': [{'annotations': {'bold': False,
                                                                'code': False,
                                                                'color': 'default',
                                                                'italic': False,
                                                                'strikethrough': False,
                                                                'underline': False},
                                                'href': None,
                                                'plain_text': '복잡한 자료구조',
                                                'text': {'content': '복잡한 자료구조',
                                                         'link': None},
                                                'type': 'text'}],
                                     'type': 'title'},
                              '일차': {'id': 'nWnH',
                                     'number': '2',
                                     'type': 'number'},
                              '커리큘럼': {'id': 'T%3AR_',
                                       'multi_select': [{'color': 'default',
                                                         'name': 'fundamentals-of-python'}],
                                       'type': 'multi_select'}},
               'public_url': None
            }],
  'type': 'page_or_database'}]


"""
주어진 data 변수에 할당된 값에서 적절한 값을 찾아 새로운 데이터를 생성한다. 
first_data 변수에 비어있는 dict를 할당한다. 
'제목' key에 문제의 제목에 해당하는 값을 찾아 할당한다. 
'일차' key에는 일차에 해당하는 값을 `정수`로 할당한다. 
'단계' key에는 단계에 해당하는 값을 찾아 '{value}단계'가 되도록 값을 변경하여 할당한다. 
'과목' key에는 과목에 해당하는 값을 찾아 할당한다. 
first_data를 출력한다.
"""

# 아래에 코드를 작성하시오.

first_data = {}

print(type(data))
print(data[0])
print('\n\n')
print(data[0]['results'])
print('\n\n')

#print(data[0]['results']['properties']) >> 에러남
print(data[0]['results'][0])
print('\n\n')
print(data[0]['results'][0]['properties'])
print('\n\n')
print(data[0]['results'][0]['properties']['제목'])
print('\n\n')
print(data[0]['results'][0]['properties']['제목']['title'])
print('\n\n')
print(data[0]['results'][0]['properties']['제목']['title'][0])
print('\n\n')
print(data[0]['results'][0]['properties']['제목']['title'][0])
print('\n\n')
print(data[0]['results'][0]['properties']['제목']['title'][0]['text'])
print('\n\n')
print(data[0]['results'][0]['properties']['제목']['title'][0]['text']['content'])
print('\n\n')


first_data['제목'] = data[0]['results'][0]['properties']['제목']['title'][0]['text']['content']
print(first_data)

first_data['일차'] = int(data[0]['results'][0]['properties']['일차']['number'])
print(first_data)

first_data['단계'] = data[0]['results'][0]['properties']['단계']['select']['name']
print(first_data)

first_data['과목'] = data[0]['results'][0]['properties']['과목']['multi_select'][0]['name']
print(first_data)

'''

