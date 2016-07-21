import xlsx_utils

data1 = xlsx_utils.get_all_data_by_filename('test_workbook.xlsx', \
                                            data_only=False)
data2 = xlsx_utils.get_all_data_by_filename('test_workbook.xlsx', \
                                            data_only=True)

