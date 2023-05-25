# -*- coding: utf-8 -*-
import conditionevaluator

@conditionevaluator
def doorType(door):
    """
    条件1
    :param door: 门类型  2  --> 双开门
    :return: bool
    """
    return "门类型错误"


@doorType.register(1)
def params_door_type_1(door):
    """
    条件2
    :param door:
    :return: False
    """
    count = 1
    return count


@doorType.register(2)
def params_door_type_2(door):
    """
    双开门返回True
    :param door:
    :return: True
    """
    count = 2
    return count



if __name__ == '__main__':
    print(params_door_type_2(1))
