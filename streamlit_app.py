import streamlit as st
from datetime import datetime

# 页面配置
st.set_page_config(page_title="德国机电安全巡检", page_icon="🛡️")

# 标题
st.title("🛡️ 德标机电安装安全检查")
st.info("提示：请如实记录现场情况。根据德国HSE标准，所有不合格项必须拍照闭环。")

# 1. 基础信息
col1, col2 = st.columns(2)
with col1:
    project = st.text_input("项目名称", "示例：中德产业园机电项目")
    inspector = st.text_input("巡检人", "安全主管")
with col2:
    date_now = st.date_input("检查日期", datetime.now())
    area = st.text_input("作业区域", "如：B1机房、3F走廊")

st.divider()

# 2. 常规项快速核对
st.subheader("✅ 每日安全红线核对")
items = [
    "个人防护(PPE)：头盔、反光衣、安全鞋齐全",
    "临时用电：配电箱锁闭、电缆无破损挂地",
    "高处作业：梯子稳固、安全带高挂低用",
    "现场文明：工完场清、材料堆放有序"
]

check_results = {}
for item in items:
    check_results[item] = st.radio(item, ["合格(OK)", "不合格(NG)", "不适用(NA)"], index=0, horizontal=True, key=item)

# 3. 违规取证与说明
st.divider()
if any(v == "不合格(NG)" for v in check_results.values()):
    st.error("⚠️ 发现安全隐患，请立即取证")
    img_file = st.camera_input("点击拍摄现场违规照片")
    if img_file:
        st.image(img_file, caption="现场取证照片")
    desc = st.text_area("隐患描述及整改要求")
    if st.button("🚀 提交整改报告", type="primary"):
        st.success("报告已生成！")
else:
    st.success("✅ 现场状态良好。")
    if st.button("🚀 提交平安日报"):
        st.balloons()
        st.success("今日记录已归档。")
