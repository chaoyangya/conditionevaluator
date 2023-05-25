# ProjectName

ProjectName and Description

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-cywhat]][contributors-url]
[![Forks][forks-cywhat]][forks-url]
[![Stargazers][stars-cywhat]][stars-url]
[![Issues][issues-cywhat]][issues-url]
[![MIT License][license-cywhat]][license-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/chaoyangya/conditionevaluator/">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">"优雅的if-else替换"</h3>
  <p align="center">
    优化并美观你的if-else
    <br />
    <a href="https://github.com/chaoyangya/conditionevaluator"><strong>探索本项目的文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/chaoyangya/conditionevaluator">查看Demo</a>
    ·
    <a href="https://github.com/chaoyangya/conditionevaluator/issues">报告Bug</a>
    ·
    <a href="https://github.com/chaoyangya/conditionevaluator/issues">提出新特性</a>
  </p>

</p>

## 目录

- [文件目录说明](#文件目录说明)
- [上手指南](#上手指南)
    - [环境要求](#环境要求)
    - [安装依赖包](#安装依赖包)
    - [1.在需要做多条件判断的函数中引入装饰器](#1.在需要做多条件判断的函数中引入装饰器)
    - [2.其他函数调用](#2.其他函数调用)
    - [3.测试](#3.测试)
- [使用到的框架](#使用到的框架)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)

### 文件目录说明

```
conditionevaluatortool 
├── /conditionevaluator/
│  ├── __init__.py
│  ├── conditionevaluator.py
├── /test/
│  ├── __init__.py
│  ├── test.py
├── README.md
└── setup.py

```

### 上手指南

###### 环境要求

1. Python 3.7.0

###### 安装依赖包

1. pip install conditionevaluator

###### 使用步骤

###### 1.在需要做多条件判断的函数中引入装饰器

```python
import conditionevaluator


@conditionevaluator
def doorType(door):
    """
    条件1
    :param door: 门类型  2  --> 双开门
    :return: bool
    """
    return "门类型错误"
```

###### 2.其他函数调用

```python
@doorType.register(1)
def params_door_type_1(door):
    """
    条件1
    :param door:
    :return: False
    """
    count = 1
    return count


@doorType.register(2)
def params_door_type_2(door):
    """
    条件2
    :param door:
    :return: True
    """
    count = 2
    return count
```

###### 3.测试

```python
if __name__ == '__main__':
    print(params_door_type_2(1))

# 结果输出
>> > 2
```


### 使用到的框架

暂无


### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

cywhat


[![blog][contributors-cywhat]][blog-url]

- 🔗[个人博客](https://cywhat.cn)

### 鸣谢

- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)
- [edgedb](https://github.com/edgedb/edgedb)

<!-- links -->

[your-project-path]:chaoyangya/conditionevaluator

[contributors-cywhat]: https://img.shields.io/github/contributors/chaoyangya/conditionevaluator.svg?style=flat-square

[contributors-url]: https://github.com/chaoyangya/conditionevaluator/graphs/contributors

[forks-cywhat]: https://img.shields.io/github/forks/chaoyangya/conditionevaluator.svg?style=flat-square

[forks-url]: https://github.com/chaoyangya/conditionevaluator/network/members

[stars-cywhat]: https://img.shields.io/github/stars/chaoyangya/conditionevaluator.svg?style=flat-square

[stars-url]: https://github.com/chaoyangya/conditionevaluator/stargazers

[issues-cywhat]: https://img.shields.io/github/issues/chaoyangya/conditionevaluator.svg?style=flat-square

[issues-url]: https://img.shields.io/github/issues/chaoyangya/conditionevaluator.svg

[license-cywhat]: https://img.shields.io/github/license/chaoyangya/conditionevaluator.svg?style=flat-square

[license-url]: https://github.com/chaoyangya/conditionevaluator/blob/master/LICENSE.txt

[blog-url]:https://cywhat.cn




