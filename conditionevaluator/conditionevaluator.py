# -*- coding: utf-8 -*-
import functools


def conditionevaluator(func):
    # create a dictionary to hold the functions for each value
    registry = {}

    # use functools to wrap the function
    @functools.wraps(func)
    def wrapper(arg0, *args, **kwargs):
        # check if there is already a function registered for arg0
        try:
            delegate = registry[arg0]
        except KeyError:
            pass
        else:
            # if there is, call it with the given arguments
            return delegate(arg0, *args, **kwargs)
        # if not, call the original function with the given arguments
        return func(arg0, *args, **kwargs)

    # function to register a function for a specific value
    def register(value):
        def wrap(func):
            # check if a function is already registered for this value
            if value in registry:
                raise ValueError(
                    f'@value_dispatch: there is already a handler '
                    f'registered for {value!r}'
                )
            # if not, add the function to the registry for the value
            registry[value] = func
            return func

        return wrap

    # function to register a function for multiple values
    def register_for_all(values):
        def wrap(func):
            # iterate through the values and register the function for each one
            for value in values:
                # check if a function is already registered for this value
                if value in registry:
                    raise ValueError(
                        f'@value_dispatch: there is already a handler '
                        f'registered for {value!r}'
                    )
                # if not, add the function to the registry for the value
                registry[value] = func
            return func

        return wrap

    # add the register functions to the wrapper so they can be accessed
    wrapper.register = register
    wrapper.register_for_all = register_for_all
    return wrapper
