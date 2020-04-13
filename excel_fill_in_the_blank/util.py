import jaconv

class Util:

    @staticmethod
    def to_zenkaku(str):
        """引数の文字列を全角に変換します
        
        Arguments:
            str {string} -- 文字列
        
        Returns:
            string -- 変換後の文字列
        """        
        return jaconv.h2z(str, digit=True, ascii=True)
