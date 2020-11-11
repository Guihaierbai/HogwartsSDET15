# 黑名单加强函数
import allure


def handle_black(func):
    # 接受传入的函数的所有参数
    def wrapper(*args, **kwargs):
        # 类中的函数传入时，第一个参数是self，如果想调用BasePage中封装的其他方法，可使用instance来调用，如：instance.find
        from frame.xueqiu_blacklist.page.base_page import BasePage
        instance: BasePage = args[0]
        try:
            return func(*args, **kwargs)
        # 如果有异常弹窗导致无法找到元素，进入黑名单逻辑
        except Exception as e:
            # python自带截图
            # print("instance.driver=%s" % instance.driver)
            instance.driver.save_screenshot("tmp.png")
            with open("tmp.png", "rb") as f:
                content = f.read()
            # allure自带上传图片
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            # 将黑名单中的元素存放到black_ele中
            for black_ele in instance.black_list:
                # 查找页面中是否存在黑名单中的元素并存放到list ele中
                ele = instance.driver.find_elements(*black_ele)
                # 如果ele的长度大于0，说明找到了黑名单中的元素
                if len(ele) > 0:
                    # 点击黑名单中的第一个元素
                    ele[0].click()
                    # 处理完黑名单后再次查找原来的元素
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
