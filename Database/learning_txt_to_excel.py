import xlsxwriter as xw

if __name__ == '__main__':
    datas = []
    f = open("两岸学术用词.txt", "r", encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        data = line.split("      ")
        datas.append(data)

    print("开始写入excel...")
    workbook = xw.Workbook("两岸学术用词.xlsx")  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ["领域", "台湾用语", "大陆用语", "外文", "来源", "是否於華語文大辭典有相關條目"]  # 设置表头

    first_bold = workbook.add_format({
        'bold': True,  # 字体加粗
        'border': 1,  # 单元格边框宽度
        'align': 'center',  # 水平对齐方式
        'valign': 'vcenter',  # 垂直对齐方式
        'fg_color': '#F4B084',  # 单元格背景颜色
        'text_wrap': False,  # 是否自动换行
        'font_size': 14,
    })
    bold = workbook.add_format({
        # 'bold': True,  # 字体加粗
        'border': 1,  # 单元格边框宽度
        'align': 'center',  # 水平对齐方式
        'valign': 'vcenter',  # 垂直对齐方式
        # 'fg_color': '#F4B084',  # 单元格背景颜色
        'text_wrap': False,  # 是否自动换行
        # 'font_size': 14,
    })
    worksheet1.set_column('A:F', 25)
    # worksheet1.set_column('B:B', 20)
    # worksheet1.set_column('C:C', 30)
    # worksheet1.set_column('D:D', 30)
    worksheet1.write_row('A1', title, first_bold)  # 从A1单元格开始写入表头
    i = 2
    for data in datas:
        row = 'A' + str(i)
        worksheet1.write_row(row, data, bold)
        i += 1
    workbook.close()
    print("写入完成~")
