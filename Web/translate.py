import pandas as pd


class Trans:
    def __init__(self):
        self.df_trans = None
        self.learning_df_trans = None

    def load_data(self, dict_path):
        self.df_trans = pd.read_excel(dict_path + "/两岸用词差异.xlsx", engine='openpyxl')
        self.learning_df_trans = pd.read_excel(dict_path + "/两岸学术用词.xlsx", engine='openpyxl')

    def query(self, input_text, to_language):
        if to_language == 'Taiwan':
            result = self.df_trans[self.df_trans['大陆用语'].str.strip() == input_text]['台湾用语']
            if not result.empty:
                return result.iloc[0]
            result = self.learning_df_trans[self.learning_df_trans['大陆用语'].str.strip() == input_text]['台湾用语']
        else:
            result = self.df_trans[self.df_trans['台湾用语'].str.strip() == input_text]['大陆用语']
            if not result.empty:
                return result.iloc[0]
            result = self.learning_df_trans[self.learning_df_trans['台湾用语'].str.strip() == input_text]['大陆用语']

        if not result.empty:
            return result.iloc[0]
        return "Translation not found."


translate = Trans()
