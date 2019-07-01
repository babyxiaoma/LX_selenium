import xlrd
from xlutils.copy import copy


class Read_Excel(object):
    def __init__(self, file_path='E:\LX_selenium\config\case.xls', index=0):
        if file_path:
            self.file_path = file_path
            self.index = index
        self.data = self.get_data()

    def get_data(self):
        '''获取excel数据'''
        data = xlrd.open_workbook(filename=self.file_path)
        sheet = data.sheet_by_index(sheetx=self.index)
        return sheet

    def get_nrows(self):
        '''获取excel数据行数'''
        if self.data.nrows >= 1:
            return self.data.nrows
        return None

    def get_data_list(self):
        '''获取全部行数据的列表'''
        data_list = []
        if self.get_nrows() != None:
            for i in range(self.get_nrows()):
                row_data = self.get_data().row_values(i)
                data_list.append(row_data)
            return data_list
        return None

    def get_cell_value(self, row, col):
        '''获取单元格数据'''
        if self.get_nrows() >= row:
            return self.data.cell_value(rowx=row, colx=col)
        return None

    def write_value(self, row, col, value):
        '''写入单元格数据'''
        book1 = xlrd.open_workbook(self.file_path)
        book2 = copy(book1)
        sheet_data = book2.get_sheet(0)
        sheet_data.write(row, col, value)
        book2.save(self.file_path)

    def get_except_value(self, data):
        '''获取预期结果值'''
        return data.split('=')


if __name__ == '__main__':
    ex = Read_Excel('E:\LX_selenium\config\key_case.xls')
    print(ex.get_nrows())
    print(ex.get_cell_value(10, 2))
    # ex.write_value(4, 0, 'pass')
