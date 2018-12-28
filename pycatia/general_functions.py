#! /user/bin/python3.6

from win32com.client import Dispatch

def create_measurable(spa_workbench, com_reference):
    """

    :param spa_workbench:
    :param com_reference:
    :return:
    """

    return spa_workbench.GetMeasurable(com_reference)


def run_system_service(vba_code, function_name, measurable_items, cat_script_language=0):
    """

    :param vba_code:
    :param function_name:
    :param measurable_items:
    :param cat_script_language:
    :return:
    """
    try:
        run = Dispatch('CATIA.Application').SystemService.Evaluate(
            vba_code,
            cat_script_language,
            function_name,
            measurable_items,
        )

        return run

    except ValueError:
        # noinspection SpellCheckingInspection
        print(f'There was a problem running SystemService.Evalue(*args) on the VBA code. The inputs were:')
        print(f'vba_code: {vba_code}, function_name: {function_name}')
