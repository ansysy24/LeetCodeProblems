def getLowestCommonManager(topManager, reportOne, reportTwo):
    list1 = get_list(topManager, reportOne, [topManager])
    if list1 is not None:
        print([l.name for l in list1])
    list2 = get_list(topManager, reportTwo, [topManager])
    if list2 is not None:
        print([l.name for l in list2])
    if list1 is None or list2 is None:
        return topManager

    if len(list2) < len(list1):
        list2, list1 = list1, list2

    for i, element in enumerate(list1):
        if element != list2[i]:
            return list2[i - 1]
    print(list1[i].name)
    return list1[i]


def get_list(head, node, lst):
    for report in head.directReports:
        if report.name == node.name:
            return lst + [report]

        result = get_list(report, node, lst + [report])
        if result is not None:
            return result


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []