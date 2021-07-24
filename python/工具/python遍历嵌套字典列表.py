def traverse_take_field(data, fields, values=[], currentKey=None):
    """
    遍历嵌套字典列表，取出某些字段的值
    :param data: 嵌套字典列表
    :param fields: 列表，某些字段
    :param values: 返回的值
    :param currentKey: 当前的键值
    :return: 列表
    """
    if isinstance(data, list):
        for i in data:
            traverse_take_field(i, fields, values, currentKey)
    elif isinstance(data, dict):
        for key, value in data.items():
            traverse_take_field(value, fields, values, key)
    else:
        if currentKey in fields:
            values.append(data)
    return values


if __name__ == '__main__':
    data = {"info": "2班成绩单",
            "grades": {
                "小明":
                    [{"chinese": 60}, {"math": 80}, {"english": 100}],
                "小红":
                    [{"chinese": 90}, {"math": 70}, {"english": 50}],
                "小蓝":
                    [{"chinese": 80}, {"math": 80}, {"english": 80}],
            },
            "newGrades": {
                "info": "新增数据",
                "newChinese": 77
            }}
    fields = ["chinese", "newChinese"]
    scores = traverse_take_field(data, fields)
    print("语文平均成绩为", sum(scores) / len(scores))
