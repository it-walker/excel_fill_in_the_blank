import os
import shutil

import dateutil.parser
import numpy as np
import pandas as pd
import xlwings as xw

from sex import Sex
from wareki import Wareki
from util import Util


class ReportInsured:
    OFFSET_ROW = 35  # 行のオフセット
    COLUMN_EMPLOYEE_FULL_NAME = '社員氏名 (4)'
    # 社労夢データインデックス：厚生年金基礎年金番号
    COLUMN_PENSION_NUMBER = '厚生年金基礎年金番号 (46)'
    COLUMN_AWARD = '資格取得時報酬月額_金銭 (56)'
    COLUMN_POST_CODE = '郵便番号 (8)'
    COLUMN_SEX = '性別 (6)'
    COLUMN_BIRTH_DATE = '生年月日 (7)'
    COLUMN_HEALTH_INSURANCE = '健康保険_資格取得年月日 (49)'
    COLUMN_ADDRESS1 = '住所1 (9)'
    COLUMN_ADDRESS2 = '住所2 (10)'
    COLUMN_ADDRESS_KANA = '住所カナ (11)'
    COLUMN_FULL_NAME_KANA = '社員氏名カナ (5)'
    COLUMN_HEALTH_INSURANCE_NUMBER = '健康保険被保険者番号 (45)'

    def cell(self, reference_key, row_index):
        return self.sheet.range(reference_key).offset(ReportInsured.OFFSET_ROW * row_index, 0)

    def cells(self, relative_index, keys, data_list):
        for key, data in zip(keys, data_list):
            self.cell(key, relative_index).value = data

    def set_address(self, row_index, relative_index):
        keys = ['N86', 'AF84']
        address1 = Util.to_zenkaku(self.df.at[row_index, ReportInsured.COLUMN_ADDRESS1])
        address2 = Util.to_zenkaku(self.df.at[row_index, ReportInsured.COLUMN_ADDRESS2])
        kana = Util.to_zenkaku(self.df.at[row_index, ReportInsured.COLUMN_ADDRESS_KANA])
        address_list = [address1 + address2, kana]

        self.cells(relative_index, keys, address_list)

    def set_name(self, row_index, relative_index):
        """名前を設定します
        
        Arguments:
            row_index {int} -- 社労夢データの行インデックス
            relative_index {int} -- 出力ファイルの相対インデックス
        """        
        keys = ['AB58', 'AZ58']
        name_list = self.df.at[row_index, ReportInsured.COLUMN_EMPLOYEE_FULL_NAME].split('　', 1)
        self.cells(relative_index, keys, name_list)

    def set_name_kana(self, row_index, relative_index):
        """氏名カナを設定します

        Arguments:
            row_index {int} -- 社労夢データの行インデックス
            relative_index {int} -- 出力ファイルの相対インデックス
        """
        keys = ['AB55', 'AZ55']
        kana_list = Util.to_zenkaku(
            str(self.df.at[row_index, ReportInsured.COLUMN_FULL_NAME_KANA])).split('　', 1)

        self.cells(relative_index, keys, kana_list)

    def set_sex(self, row_index, relative_index):
        """性別を設定します

        Arguments:
            row_index {int} -- 社労夢データの行インデックス
            relative_index {int} -- 出力ファイルの相対インデックス
        """
        put_index = 'DH55'
        self.cell(put_index, relative_index).value = Sex().text(
            self.df.at[row_index, ReportInsured.COLUMN_SEX])

    def set_post_code(self, row_index, relative_index):
        """郵便番号を設定します

        Arguments:
            row_index {[type]} -- [description]
            relative_index {[type]} -- [description]
        """
        postcode_list = str(self.df.at[row_index, ReportInsured.COLUMN_POST_CODE]).split('-')
        keys  = ['P84', 'V84']

        self.cells(relative_index, keys, postcode_list)

    def set_reward(self, row_index, relative_index):
        """報酬月額を設定します

        Arguments:
            row_index {int} -- 社労夢データの行インデックス
            relative_index {int} -- 出力ファイルの相対インデックス
        """
        keys = ['S74', 'AR77']
        data_list = [ self.df.at[row_index, ReportInsured.COLUMN_AWARD], self.df.at[row_index, ReportInsured.COLUMN_AWARD]]
        self.cells(relative_index, keys, data_list)

    def set_my_number(self, row_index, relative_index):
        """個人番号を設定します

        Arguments:
            row_index {int} -- 社労夢データの行インデックス
            relative_index {int} -- 出力ファイルの相対インデックス
        """
        # 10桁で0埋め
        mynumber = str(
            self.df.at[row_index, ReportInsured.COLUMN_PENSION_NUMBER]).zfill(10)
        keys = ['AB65', 'AF65', 'AJ65', 'AN65',
                       'AR65', 'AV65', 'AZ65', 'BD65', 'BH65', 'BL65']
        self.cells(relative_index, keys, mynumber)

    def set_born_date(self, row_index, relative_index):
        keys = ['CF55', 'CJ55', 'CM55', 'CP55', 'CS55', 'CV55', 'CY55']
        w = Wareki()
        tmplist = w.wa_yymmdd(str(self.df.at[row_index, ReportInsured.COLUMN_BIRTH_DATE]))
        data_list = tmplist[1::1]
        gengou = tmplist[0]
        data_list.insert(0, w.check_wareki(gengou))

        self.cells(relative_index, keys, data_list)

    def set_health_insurance(self, row_index, relative_index):
        keys = ['CJ65', 'CM65', 'CP65','CS65', 'CV65', 'CY65']
        data_list = Wareki().wa_yymmdd(str(self.df.at[row_index, ReportInsured.COLUMN_HEALTH_INSURANCE]))[1::1]

        self.cells(relative_index, keys, data_list)

    def report(self, index, relative_index):
        """被保険者資格取得届を作成します

        Arguments:
            index {int} -- 社労夢データの行インデックス
            relative_index {int} -- 被保険者の相対インデックス
        Note:
            相対インデックスとは、1ファイルに最大4人まで入力できるので、その相対位置のことです
        """

        # 住所
        self.set_address(index, relative_index)
        # 社員氏名
        self.set_name(index, relative_index)
        # 社員氏名カナ
        self.set_name_kana(index, relative_index)
        # 生年月日
        self.set_born_date(index, relative_index)
        # 性別
        self.set_sex(index, relative_index)
        # 郵便番号
        self.set_post_code(index, relative_index)
        # 資格取得時報酬月額
        self.set_reward(index, relative_index)
        self.cell('N55', index).value = self.df.at[index, ReportInsured.COLUMN_HEALTH_INSURANCE_NUMBER]
        # 厚生年金基礎年金番号
        self.set_my_number(index, relative_index)
        # 健康保険資格取得日
        self.set_health_insurance(index, relative_index)

    def generate(self, input_file_path, template_file_path, save_directory):
        """被保険者資格取得届を出力する（.xlsx）

        Arguments:
            input_file_path {string} -- [社労夢データ（.xlsx）]
            template_file_path {[string]} -- [テンプレートファイルパス]
            save_directory {[string]} -- [保存ディレクトリパス]
        """

        self.df = pd.read_excel(input_file_path)
        li = list(range(len(self.df)))
        group_by = 4
        aaa = [li[i:i + group_by] for i in range(0, len(li), group_by)]
        for index, current_list in enumerate(aaa):
            save_file = os.path.join(
                save_directory, 'out_' + str(index).zfill(2) + '.xlsx')
            shutil.copy(template_file_path, save_file)
            wb = xw.Book(save_file)
            self.sheet = wb.sheets[0]

            for j in current_list:
                relative_index = j % 4
                self.report(j, relative_index)

            wb.save(path=None)
            wb.close()
