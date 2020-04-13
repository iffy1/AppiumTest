class XianyuDataCenter:
    def get_bottom_button(button_name):
        return "//android.widget.TextView[@text=\"%s\"]" % button_name

    def get_filter_button(button_name):
        return "//android.view.View[@text =\'%s\']" % button_name
