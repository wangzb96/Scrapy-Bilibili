from typing import List
import json


def str_list(s: str, sep: str=None) -> List[str]:
    """分割单个字符串成多个字符串并返回字符串列表

    Args:
        s: 输入的字符串
        sep: 分隔符，默认空格

    Returns:
        字符串列表，其中的每个字符串都去除头尾空字符
    """

    if sep is None or sep==' ': return s.split()
    return [i.strip() for i in s.split(sep)]


def json2obj(s: str, enc: str=None):
    """json字符串 -> Python对象

    Args:
        s: 输入的json字符串
        enc: 字符串编码格式，默认UTF-8

    Returns:
        Python对象
    """

    if enc is None: enc = 'UTF-8'
    return json.loads(s, encoding=enc)


def obj2json(x, show: bool=None) -> str:
    """Python对象 -> json字符串

    Args:
        x: 输入的Python对象
        show: 是否返回显示格式，默认否
              否：返回紧凑格式，其中没有空格和换行
              是：返回显示格式，其中有空格和换行

    Returns:
        json字符串，并且不替换ASCII字符
    """

    if not show:
        key_sep = ':'
        item_sep = ','
        indent = None
    else:
        key_sep = ': '
        item_sep = ','
        indent = 4
    return json.dumps(x, ensure_ascii=False,
        separators=(item_sep, key_sep), indent=indent)


if __name__=='__main__':
    x = {'a': 123, 'b': 3.14, 'c': 'hello', 'd': [789, 456, 123]}
    s = obj2json(x, True)
    print(s)
    print('a{}b{}c'.format(1, '{}'))

