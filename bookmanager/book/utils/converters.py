class MobileConverter:
    """
    自定义路由转换器，匹配手机号
    """
    # 自定义匹配手机号的正则表达式
    regex = '1[3589]\d{9}'

    def to_python(self, value):
        """
        这个方法用于将URL中的字符串形式的手机号转换为Python中的整数类型。
        例如,当URL中有/users/13812345678/时,这个方法会将'13812345678'转换为整数13812345678
        """
        return int(value)

    def to_url(self, value):
        """
        这个方法用于将Python中的整数类型的手机号转换为URL中的字符串形式。
        例如,当在Python代码中使用reverse('user_detail', args=[13812345678])时,
        这个方法会将整数13812345678转换为字符串'13812345678'
        """
        return str(value)

