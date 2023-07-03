import pandas as pd


class SkuChart(object):
    def __init__(self):
        data = pd.read_excel('F:\\python\\python_office\\file\\extra1.xlsx')
        self.sku_data = data.values

    def get_ean_list(self):
        ean_list = list()
        for index, value in enumerate(self.sku_data):
            ean = value[1]
            ean_list.append(ean)
        return ean_list

    def handle_asin_chart(self, asin_map, title_map):
        data_map = {'SKU': [], 'EAN': [], 'ASIN': [], 'TITLE': []}
        for index, value in enumerate(self.sku_data):
            data_map.get('SKU').append(value[0])
            data_map.get('EAN').append(value[1])
            data_map.get('ASIN').append(asin_map.get(value[1], ''))
            data_map.get('TITLE').append(title_map.get(value[1], ''))
        df = pd.DataFrame(data_map)
        df.to_excel("F:\\python\\python_office\\file\\extra1.xlsx", sheet_name='处理后', index=False)


if __name__ == '__main__':
    s = SkuChart()
    print(s.get_ean_list())