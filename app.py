import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Akam AI",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
body {
    direction: rtl;
}
.main {
    direction: rtl;
}
h1, h2, h3, p, div {
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Akam AI")
st.caption("دستیار هوشمند آکام تجارت آتیه پارسیان")

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:
   
    page = st.selectbox(
        "بخش",
        [
            "🏠 داشبورد",
            "💬 دستیار هوشمند",
            "📋 پروژه‌ها",
            "💰 مالی",
            "📦 محصولات"
        ]
    )

# -------------------------
# Dashboard
# -------------------------
if page == "🏠 داشبورد":

    st.header("داشبورد مدیریت")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("پروژه‌های فعال", "3")
    c2.metric("پروژه‌های تحویل‌شده", "2")
    c3.metric("فروش ماهانه هدف", "200M")
    c4.metric("وضعیت سیستم", "فعال")

    st.divider()

    st.subheader("📌 وضعیت پروژه‌ها")

    projects = [
        ("عامری", "مرحله تحویل"),
        ("کمالی فرد", "تحویل شده - کارهای جزئی باقی مانده"),
        ("فرج‌زاده", "اجرای سقف"),
    ]

    for name, status in projects:
        st.write(f"**{name}**")
        st.info(status)

# -------------------------
# AI Assistant
# -------------------------
elif page == "💬 دستیار هوشمند":

    st.header("💬 دستیار هوشمند Akam AI")

    st.write(
        "سؤال خود را درباره مدیریت، پروژه، فروش، محصولات یا امور شرکت بنویسید."
    )

    question = st.text_area(
        "پیام شما",
        placeholder="مثلاً: وضعیت پروژه‌های من چیست؟"
    )

    if st.button("ارسال 🚀"):

        if not question.strip():
            st.warning("لطفاً ابتدا سؤال خود را وارد کنید.")
        else:

            q = question.lower()

            if "پروژه" in q:
                answer = """
                پروژه‌های ثبت‌شده فعلی:

                • عامری: مرحله تحویل
                • کمالی فرد: تحویل شده و کارهای جزئی باقی مانده
                • فرج‌زاده: مرحله اجرای سقف
                """

            elif "فروش" in q:
                answer = """
                هدف فعلی پوشش هزینه‌های جاری شرکت حدود ۲۰۰ میلیون تومان در ماه است.
                """

            elif "محصول" in q or "فست" in q:
                answer = """
                محصولات اصلی شامل Fast Protection / Liquid Glove
                در حجم‌های مختلف هستند.
                """

            else:
                answer = """
                پیام شما دریافت شد.

                برای پاسخ هوشمندتر، این بخش در نسخه بعدی
                به موتور هوش مصنوعی متصل خواهد شد.
                """

            st.success(answer)

# -------------------------
# Projects
# -------------------------
elif page == "📋 پروژه‌ها":

    st.header("📋 مدیریت پروژه‌ها")

    data = {
        "پروژه": [
            "عامری",
            "کمالی فرد",
            "فرج‌زاده"
        ],
        "وضعیت": [
            "تحویل",
            "تحویل شده / جزئی",
            "اجرای سقف"
        ]
    }

    st.table(data)

    st.divider()

    st.subheader("➕ ثبت پروژه جدید")

    name = st.text_input("نام پروژه")
    status = st.selectbox(
        "وضعیت",
        ["شروع نشده", "در حال اجرا", "تأسیسات", "سقف", "تحویل", "تکمیل"]
    )

    if st.button("ثبت پروژه"):
        if name:
            st.success(f"پروژه «{name}» با وضعیت «{status}» ثبت شد.")
        else:
            st.warning("نام پروژه را وارد کنید.")

# -------------------------
# Financial
# -------------------------
elif page == "💰 مالی":

    st.header("💰 مدیریت مالی")

    monthly_cost = st.number_input(
        "هزینه جاری ماهانه (تومان)",
        min_value=0,
        value=200_000_000,
        step=10_000_000
    )

    sales = st.number_input(
        "فروش ماه جاری (تومان)",
        min_value=0,
        value=0,
        step=10_000_000
    )

    balance = sales - monthly_cost

    st.metric(
        "مانده نسبت به هزینه جاری",
        f"{balance:,.0f} تومان"
    )

# -------------------------
# Products
# -------------------------
elif page == "📦 محصولات":

    st.header("📦 محصولات")

    products = [
        ("Fast Protection 30cc", "محصول اصلی"),
        ("Fast Protection 60cc", "محصول اصلی"),
        ("Fast Protection 100cc", "محصول"),
        ("Fast Protection 120cc", "محصول")
    ]

    for product, description in products:
        st.write(f"### {product}")
        st.caption(description)

st.divider()

st.caption(
    f"Akam AI | آخرین بروزرسانی: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
)