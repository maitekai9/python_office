import pandas as pd
from string_utils import find_str_index

data = pd.read_excel('F:\\python\\python_office\\file\\乖宝写~.xlsx')
key_set = set()
pro_data = data.values
for index, value in enumerate(pro_data):
    desc = value[4]
    print(desc)
    space_index = find_str_index(desc, 1, 0)
    key_set.add(desc[0:space_index])

key_map = {key: [] for key in key_set}
print(key_map)
data_map = {'虚拟SKU': [], '真实SKU': [], 'ASIN': [], '类目': [], '描述': [], '1关键字': [], '2关键字': [], '3关键字': [], '4关键字': []}
for index, value in enumerate(pro_data):
    desc = value[4]
    space_index = find_str_index(desc, 0, 0)
    space_index1 = find_str_index(desc, 1, 0)
    space_index2 = find_str_index(desc, 2, 0)
    space_index3 = find_str_index(desc, 3, 0)
    key = desc[0:space_index]
    key1 = desc[0:space_index1]
    key2 = desc[0:space_index2]
    key3 = desc[0:space_index3]
    # value[5] = key
    # value[6] = key1
    # value[7] = key2
    # value[8] = key3
    # key_map.get(key).append(index)
    data_map.get('虚拟SKU').append(value[0])
    data_map.get('真实SKU').append(value[1])
    data_map.get('ASIN').append(value[2])
    data_map.get('类目').append(value[3])
    data_map.get('描述').append(value[4])
    data_map.get('1关键字').append(key)
    data_map.get('2关键字').append(key1)
    data_map.get('3关键字').append(key2)
    data_map.get('4关键字').append(key3)
print(data_map)
# writer = pd.ExcelWriter("F:\\python\\python_office\\file\\乖宝写~.xlsx", mode="a", engine="openpyxl")
df = pd.DataFrame(data_map)
df.to_excel("F:\\python\\python_office\\file\\乖宝写~3.xlsx", sheet_name='处理后', index=False)