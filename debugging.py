import fourop as fo

print(fo.addtion(10, 19))

t=10
def test(t):
    print(x)
    t = 20
    print("in fuction : ", t)

x=20
test(x)
print(t)

def strTest():
    global s
    s = "I love lll"
    print(s)

s = "Ilove s"
strTest()
print(s)

print("{s}, {x}")
'''
연습 문제 7.1: 가변 인자의 간단한 예
다음 함수를 정의해 보자.

>>> def avg(x,*more):
        return float(x+sum(more))/(1+len(more))

>>> avg(10,11)
10.5
>>> avg(3,4,5)
4.0
>>> avg(1,2,3,4,5,6)
3.5
>>>
*more 매개변수(parameter)가 추가적인 인자를 어떻게 수집하는지 살펴보라.

'''
def avg(x,*more):
        return float(x+sum(more))/(1+len(more))
print(avg(1,4,5,6,7))


'''
연습 문제 7.2: 튜플과 딕셔너리를 인자로 전달
데이터 파일을 읽어 다음과 같은 튜플을 얻었다고 하자.

>>> data = ('GOOG', 100, 490.1)
>>>
이 데이터로부터 Stock 객체를 생성하고자 한다. 그런데 data를 직접 전달하면 작동하지 않는다.

>>> from stock import Stock
>>> s = Stock(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 4 arguments (2 given)
>>>
그 대신 *data를 사용하면 간단히 해결할 수 있다. 다음과 같이 해 보라.

>>> s = Stock(*data)
>>> s
Stock('GOOG', 100, 490.1)
>>>
딕셔너리를 사용할 때는 **을 붙인다. 예:

>>> data = { 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
>>> s = Stock(**data)
Stock('GOOG', 100, 490.1)
>>>
연습 문제 7.3: 인스턴스의 리스트를 생성
report.py 프로그램에서 다음과 같은 코드를 사용해 인스턴스의 리스트를 생성했다.

def read_portfolio(filename):
    주식 포트폴리오 파일을 읽어 딕셔너리의 리스트를 생성.
    name, shares, price를 키로 사용.
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                               select=['name','shares','price'],
                               types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price'])
                  for d in portdicts ]
    return Portfolio(portfolio)
Stock(**d)를 사용해 코드를 단순화할 수 있다. 그렇게 바꿔보라.

연습 문제 7.4: 인자 통과
fileparse.parse_csv() 함수에는 파일 구분자를 바꾸거나 오류를 보고하는 옵션이 있다. 위의 read_portfolio() 함수에 그런 기능이 있으면 좋을 것이다. 다음과 같이 바꿔보자.

def read_portfolio(filename, **opts):
    '''
    주식 포트폴리오 파일을 읽어 딕셔너리의 리스트를 생성.
    name, shares, price를 키로 사용.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
변경을 했으면, 오류가 있는 파일을 읽어보자.

>>> import report
>>> port = report.read_portfolio('Data/missing.csv')
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
오류 메시지가 나오지 않게 해 보자.

>>> import report
>>> port = report.read_portfolio('Data/missing.csv', silence_errors=True)
>>>
'''