import dateutil.parser

class Wareki:

    # 西暦と和暦の対応テーブル
    _wareki_table = [
        {"name": "明治", "start": 1868, "end": 1912},
        {"name": "大正", "start": 1912, "end": 1926},
        {"name": "昭和", "start": 1926, "end": 1989},
        {"name": "平成", "start": 1989, "end": 2019},
        {"name": "令和", "start": 2019, "end": 9999}
    ]

    _key_name = 'name'
    _key_start = 'start'
    _key_end = 'end'

    def check_wareki(self, wareki_keyword):
        """引数から与えられた和暦キーワードから、セルに入力する文字列を取得します
        
        Arguments:
            wareki_keyword {string} -- キーワード（昭和、平成、令和）
        
        Raises:
            ValueError: 存在しないキーワードが渡されたときは例外となります
        
        Returns:
            [string] -- 該当するキーワードに適した文字列
        """
        _key_to_template = { '昭和': '⑤.昭和\n\n7.平成\n\n9.令和', 
                             '平成': '5.昭和\n\n⑦.平成\n\n9.令和', 
                             '令和': '5.昭和\n\n7.平成\n\n⑨.令和' }
        if wareki_keyword in _key_to_template:
            return _key_to_template[wareki_keyword]
        else:
            raise ValueError("check_warekiメソッドでエラー!")

    def seireki_wareki(self, year):
        """西暦から和暦を取得します
        
        Arguments:
            year {int} -- 西暦年
        
        Returns:
            string -- 和暦＋年数
        """
        if not year: 
            raise ValueError('引数の値が不正です')
        elif year < 1868:
            raise ValueError('引数の値が不正です')

        for w in self._wareki_table:
            if w[self._key_start] <= year < w[self._key_end]:
                y = str(year - w[self._key_start] + 1)
                return w[self._key_name] + y

        raise ValueError('seireki_wareki でエラー。不正なキーが入力されました')

    def wa_yymmdd(self, date_string):
        """西暦から和暦を取得します
        
        Arguments:
            year {string} -- 西暦年
        
        Returns:
            list -- 和暦リスト（Y、Y、M、M、D、D）

        Note:
            和暦リストは、年月日が1文字ずつ分割されています
            1桁の月は、十の位には空文字が入っています
        """        
        target_date = dateutil.parser.parse(date_string)
        target_month = str(target_date.month)
        target_day = str(target_date.day)
        wareki = self.seireki_wareki(target_date.year)
        wa_yymmdd_list = []
        # 元号
        wa_yymmdd_list.append(wareki[0:2])
        # 年
        wa_yymmdd_list.append('' if len(wareki[2:]) == 1 else wareki[2])
        wa_yymmdd_list.append(wareki[2] if len(wareki[2:]) else wareki[3])
        # 月
        wa_yymmdd_list.append('' if len(target_month) == 1 else target_month[0])
        wa_yymmdd_list.append(target_month[0] if len(target_month) == 1 else target_month[1])
        # 日
        wa_yymmdd_list.append('' if len(target_day) == 1 else target_day[0])
        wa_yymmdd_list.append(target_day[0] if len(target_day) == 1 else target_day[1])

        return wa_yymmdd_list
