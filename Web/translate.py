import pandas as pd


class Trans:
    def __init__(self):
        self.df_trans = None
        self.learning_df_trans = None

    def load_data(self, dict_path):
        self.df_trans = pd.read_excel(dict_path + "/cleaned_两岸用词差异.xlsx", engine='openpyxl')
        self.learning_df_trans = pd.read_excel(dict_path + "/cleaned_两岸学术用词.xlsx", engine='openpyxl')

    def translate(self, input_text, to_language):
        # 对台湾化进行处理
        if to_language == 'Taiwan':
            # Search in the "两岸用词差异" dataset
            df_results = self.df_trans[
                self.df_trans['大陆用语'] == input_text
                ][['异同类别', '子领域', '台湾用语']]
            df_results.loc[df_results['异同类别'] == '大陸特有', '台湾用语'] = input_text

            # Search in the "两岸学术用词" dataset
            learning_df_results = self.learning_df_trans[
                self.learning_df_trans['大陆用语'] == input_text
                ][['领域', '台湾用语', '外文']]

            # 查找结果格式化到result
            if not df_results.empty:
                result = [
                    f"【{row['异同类别']}，{row['子领域']}】{row['台湾用语']}"
                    for _, row in df_results.iterrows()
                ]
            if not learning_df_results.empty:
                result = [
                    f"【{row['领域']}】{row['台湾用语']}，({row['外文']})"
                    for _, row in learning_df_results.iterrows()
                ]

        # 对大陆化进行处理
        else:
            # Search in the "两岸用词差异" dataset
            df_results = self.df_trans[
                self.df_trans['台湾用语'] == input_text
                ][['异同类别', '子领域', '大陆用语']]

            # Search in the "两岸学术用词" dataset
            learning_df_results = self.learning_df_trans[
                self.learning_df_trans['台湾用语'] == input_text
                ][['领域', '大陆用语', '外文']]

            df_results.loc[df_results['异同类别'] == '臺灣特有', '大陆用语'] = input_text

            # 查找结果格式化到result
            if not df_results.empty:
                result = [
                    f"【{row['异同类别']}，{row['子领域']}】{row['大陆用语']}"
                    for _, row in df_results.iterrows()
                ]
            if not learning_df_results.empty:
                result = [
                    f"【{row['领域']}】{row['大陆用语']}，({row['外文']})"
                    for _, row in learning_df_results.iterrows()
                ]

        # 格式化结果到字符串output_text
        if df_results.empty and learning_df_results.empty:
            output_text = input_text
        else:
            output_text = "\n".join(result)
        return output_text


translate = Trans()
