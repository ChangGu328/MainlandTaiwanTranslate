import pandas as pd


# 加载 Excel 文件
def load_data(file_path):
    return pd.read_excel(file_path)


# 清理和拆分数据
def clean_and_split_data(data):
    # 移除多余的空格和换行符
    data['台湾用语'] = data['台湾用语'].astype(str).str.strip()
    data['大陆用语'] = data['大陆用语'].astype(str).str.strip()

    # 拆分包含 '/' 的条目
    def expand_rows_with_slash(row, column_name):
        entries = row[column_name].split('/')
        new_rows = []
        for entry in entries:
            new_row = row.copy()
            new_row[column_name] = entry.strip()
            new_rows.append(new_row)
        return new_rows

    expanded_rows = []
    for _, row in data.iterrows():
        if '/' in row['台湾用语'] or '/' in row['大陆用语']:
            expanded_taiwan = expand_rows_with_slash(row, '台湾用语')
            for row_taiwan in expanded_taiwan:
                expanded_mainland = expand_rows_with_slash(row_taiwan, '大陆用语')
                expanded_rows.extend(expanded_mainland)
        else:
            expanded_rows.append(row)

    return pd.DataFrame(expanded_rows)


# 主执行函数
def process_file(input_path, output_path):
    data = load_data(input_path)
    processed_data = clean_and_split_data(data)
    processed_data.to_excel(output_path, index=False)


# 运行处理
if __name__ == '__main__':
    # input_path = '两岸用词差异.xlsx'
    # output_path = '两岸用词差异-拆分.xlsx'
    input_path = '两岸学术用词.xlsx'
    output_path = '两岸学术用词-拆分.xlsx'
    process_file(input_path, output_path)
