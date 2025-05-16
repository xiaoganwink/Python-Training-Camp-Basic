"""
练习: HTTP请求

描述：
本练习帮助您学习如何使用requests库发送HTTP请求并处理响应。
注意：运行此练习前，请确保已安装requests库（pip install requests）。

请补全下面的函数，实现发送HTTP请求并处理响应的功能。
"""
def get_website_content(url):
    """
    发送GET请求获取网页内容
    
    参数:
    - url: 目标网站URL
    
    返回:
    - 包含响应信息的字典: 
      {
        'status_code': HTTP状态码,
        'content': 响应内容文本,
        'headers': 响应头部信息
      }
    """
    # 请在下方编写代码
    # 使用requests.get()发送GET请求
    # 返回包含状态码、内容和头部信息的字典
    pass
    # 发送GET请求
    import requests
    # 处理网络异常
    from requests.exceptions import RequestException
    try:
        request = requests.get(url)
        # 获取响应状态码
        status_code = request.status_code
        # 获取响应内容
        content = request.text
        # 获取响应头部信息
        headers = request.headers
        # 返回结果
        return {
            'status_code': status_code,
            'content': content,
            'headers': headers
        }
    except RequestException as e:
        # 处理网络异常（如超时、连接错误）
        return {
            'status_code': None,
            'content': None,
            'headers': None,
            'error': str(e)  # 可选：返回错误信息
        }


def post_data(url, data):
    """
    发送POST请求提交数据
    
    参数:
    - url: 目标网站URL
    - data: 要提交的数据字典
    
    返回:
    - 包含响应信息的字典:
      {
        'status_code': HTTP状态码,
        'response_json': 响应的JSON数据(如果有),
        'success': 请求是否成功(状态码为2xx)
      }
    """
    # 请在下方编写代码
    # 使用requests.post()发送POST请求
    # 返回包含状态码、响应JSON和成功标志的字典
    pass
    # 发送POST请求
    import requests
    # 处理网络异常
    from requests.exceptions import RequestException
    try:
        request = requests.post(url, json=data)
        # 获取响应状态码
        status_code = request.status_code
        # 获取响应JSON数据
        # 注意：如果响应不是JSON格式，json()方法会抛出异常
        # 因此需要使用try-except来处理
        try:
            response_json = request.json()
        except ValueError:
            response_json = None  # 如果不是JSON格式，返回None
       # response_json = request.json() if request.status_code == 200 else None
        # 返回结果
        return {
            'status_code': status_code,
            'response_json': response_json,
            'success': request.ok # 判断是否为2xx状态码
        }
    except RequestException as e:
        # 处理网络异常（如超时、连接错误）
        return {
            'status_code': None,
            'response_json': None,
            'success': False,
            'error': str(e)  # 可选：返回错误信息
        }