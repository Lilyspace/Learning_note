import xlwings as xw
import pandas as pd
import time

start = time.time()

app1 = xw.App(visible=True, add_book=False)
# wb1_last_week = app1.books.open(r'C:/Users/pengyuxu/Desktop/文件/Data_analysis_task_Fancy/seller_candidate_list_20220403_NA_row data.xlsx', read_only=True)
wb2_result = app1.books.open(r'C:/Users/pengyuxu/Desktop/文件/Data_analysis_task_Fancy/seller_candidate_list_20220403_NA_demo_data.xlsx', read_only=False)

# step1: copy the result data of last week: cli-surfacing list, cli-tollgate list, pl-tollgate list

df1 = pd.read_excel(r'C:/Users/pengyuxu/Desktop/文件/Data_analysis_task_Fancy/seller_candidate_list_20220403_NA_row data.xlsx', sheet_name='Cli-surfacing list')
df2 = pd.read_excel(r'C:/Users/pengyuxu/Desktop/文件/Data_analysis_task_Fancy/seller_candidate_list_20220403_NA_row data.xlsx', sheet_name='cli-tollgate list')
df3 = pd.read_excel(r'C:/Users/pengyuxu/Desktop/文件/Data_analysis_task_Fancy/seller_candidate_list_20220403_NA_row data.xlsx', sheet_name='pl-tollgate list')

def copy_from_last_week():
    global sht1
    sht1 = wb2_result.sheets.add('Cli-surfacing list', after=wb2_result.sheets[0])
    sht2 = wb2_result.sheets.add('cli-tollgate list', after=wb2_result.sheets[1])
    sht3 = wb2_result.sheets.add('pl-tollgate list', after=wb2_result.sheets[2])
    sht1.cells(1, 1).value = 'merchant_customer_id'
    sht1.range('A2').value = df1.values
    sht2.cells(1, 1).value = 'merchant_customer_id'
    sht2.range('A2').value = df2.values
    sht3.cells(1, 1).value = 'merchant_customer_id'
    sht3.range('A2').value = df3.values

copy_from_last_week()


def logic_calculation_add_to_result():
    global sht0, rownum, i
    sht0 = wb2_result.sheets[0]
    sht0.cells(1, 12).value = 'is_cli_surfacing'
    sht0.cells(1, 13).value = 'is_cli_tollgate'
    sht0.cells(1, 14).value = 'is_pl_surfacing'
    sht0.cells(1, 15).value = 'is_pl_tollgate'
    rownum = sht0.range('A1').current_region.last_cell.row
    for i in range(2, rownum):
        original_customer_id = sht0.cells(i, 1).value  # (rows, column)
        if (original_customer_id in df1['merchant_customer_id'].values):
            sht0.cells(i, 12).value = 1
        else:
            sht0.cells(i, 12).value = 0

        if (original_customer_id in df2['merchant_customer_id'].values):
            sht0.cells(i, 13).value = 1
        else:
            sht0.cells(i, 13).value = 0

        if (original_customer_id in df3['merchant_customer_id'].values):
            sht0.cells(i, 15).value = 1
        else:
            sht0.cells(i, 15).value = 0


logic_calculation_add_to_result()


def generate_seller_modification_list():
    global newSellerToAddList, sellerToRemoveList, i
    sht1.cells(1, 2).value = 'merchant_customer_id'
    newSellerToAddList = []
    sellerToRemoveList = []
    for i in range(2, rownum):
        defect_category = sht0.cells(i, 2).value
        merchant_customer_id = sht0.cells(i, 1).value
        is_tollgate_eligible = sht0.cells(i, 11).value
        is_pl_tollgate = sht0.cells(i, 15).value
        is_cli_tollgate = sht0.cells(i, 13).value
        if defect_category == 'Label':
            if is_tollgate_eligible == 1 and is_pl_tollgate == 0:
                newSellerToAddList.append(merchant_customer_id)
            elif is_tollgate_eligible == 0 and is_pl_tollgate == 1:
                sellerToRemoveList.append(merchant_customer_id)
        elif defect_category == 'Quantity':
            if is_tollgate_eligible == 1 and is_cli_tollgate == 0:
                newSellerToAddList.append(merchant_customer_id)
            elif is_tollgate_eligible == 0 and is_cli_tollgate == 1:
                sellerToRemoveList.append(merchant_customer_id)
        else:
            print('unexpected defect category [%s] for customer [%d]' % defect_category % merchant_customer_id)
    print('new seller to add', newSellerToAddList)
    print('seller to remove', sellerToRemoveList)


generate_seller_modification_list()


def generate_new_seller_list():
    ids_last_week = df1['merchant_customer_id'].values.tolist()
    for id_to_remove in sellerToRemoveList:
        ids_last_week.remove(id_to_remove)
    for id_to_add in newSellerToAddList:
        ids_last_week.append(id_to_add)
    sht1.cells(1, 2).value = 'merchant_customer_id'
    sht1.range('B2').value = pd.DataFrame(ids_last_week, columns=['merchant_customer_id']).values


generate_new_seller_list()

# wb1_last_week.save()
# wb1_last_week.close()
wb2_result.save(r'C:/Users/pengyuxu/Desktop/文件/Data_analysis_task_Fancy/result.xlsx')
wb2_result.close()
app1.quit()

end = time.time()
print('Running time: %s Seconds' %(end-start))



