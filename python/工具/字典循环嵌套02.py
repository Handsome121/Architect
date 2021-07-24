def get_dict_value(in_dict, target_key, results=[], current_key=None):
    """
    :param in_dict: 嵌套字典
    :param target_key:需要获取的字段
    :param results:结果存放的列表
    :param not_d:判断是否筛选
    :return:列表
    """
    if isinstance(in_dict, dict):
        for key, value in in_dict.items():
            get_dict_value(value, target_key, results, key)
    # 如果当前键与目标键相等, 并且判断是否要筛选
    if current_key in target_key:
        results.append(in_dict)
    return results


if __name__ == '__main__':
    advanced_config = {'Statistical_methods': 'A',
                       'report_fileds':
                           {"speclial_filed":
                                {"left":
                                     {"left":
                                          {"left":
                                               {"left":
                                                    {"left":
                                                         {"left":
                                                              {"left": "mail_receivers", "op": "!=", "right": "sssss"},
                                                          "right": {"left": "mail_sender", "op": "=", "right": "dsdsd"},
                                                          "op": "AND"
                                                          },
                                                     "right":
                                                         {"left": "tgt_ip", "op": "in", "right": ["1.1.1.1"]}
                                                        , "op": "OR"
                                                     },
                                                "right": {"left": "dev_ip", "op": "!=", "right": "2.1.3.4"},
                                                "op": "OR"
                                                },
                                           "right":
                                               {"left": "info2", "op": "=", "right": "adad"},
                                           "op": "AND"
                                           },
                                      "right":
                                          {"left": "info1", "op": "in", "right": [11111]},
                                      "op": "AND"
                                      },
                                 "right": {"left": "info4", "op": "=", "right": "aaaaa"},
                                 "op": "OR"
                                 }
                            }
                       }
    speclial_filed = advanced_config["report_fileds"]["speclial_filed"]
    target_key = ["left"]
    result_left = get_dict_value(speclial_filed, target_key)
    print(result_left)
