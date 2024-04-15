import pandas as pd

if __name__ == '__main__':
    # Load the Excel file
    # file_path = '两岸用词差异-拆分.xlsx'
    file_path = '两岸学术用词-拆分.xlsx'
    data = pd.read_excel(file_path)

    # Strip whitespace and newlines from all string cells
    data_cleaned = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Remove duplicate rows
    data_cleaned = data_cleaned.drop_duplicates()

    # Save the cleaned data to a new Excel file
    # output_path = 'cleaned_两岸用词差异.xlsx'
    output_path = 'cleaned_两岸学术用词.xlsx'
    data_cleaned.to_excel(output_path, index=False)