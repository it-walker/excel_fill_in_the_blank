class Sex:
    TEMPLATE_MALE = '　　①．男　　　　　　5．男（基金）\n　　2．女　　　　　　6．女（基金）\n　　3．坑内員　　　7．坑内員\n　　　　　　　　　　　　　　　（基金）'
    TEMPLATE_FEMALE = '　　1．男　　　　　　5．男（基金）\n　　2．女　　　　　　⑥．女（基金）\n　　3．坑内員　　　7．坑内員\n　　　　　　　　　　　　　　　（基金）'
    KEY_TO_TEMPLATE = {'男': TEMPLATE_MALE, '女': TEMPLATE_FEMALE}

    def text(self, keyword):
        return_value = ''

        if keyword in Sex.KEY_TO_TEMPLATE:
            return_value = Sex.KEY_TO_TEMPLATE[keyword]
        else:
            raise ValueError("sex_textメソッドでエラー!")

        return return_value
