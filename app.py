import streamlit as st
import pandas as pd


def analyze(df: pd.DataFrame) -> None:
    """Render only the requested summaries (sums by city and by name) in Arabic.

    This function performs a minimal, local numeric coercion just when computing
    the sums so we don't rely on a separate cleaning step.
    """

    # مجموعات حسب المدينة
    if "City" in df.columns:
        st.write("### مجموع التفعيلات ومجموع التسجيلات حسب المدينة")
        city_df = df.copy()
        if "Activation" in city_df.columns and "Registration" in city_df.columns:
            # coerce to numeric locally for correct summation
            city_df["Activation"] = pd.to_numeric(city_df["Activation"], errors="coerce").fillna(0)
            city_df["Registration"] = pd.to_numeric(city_df["Registration"], errors="coerce").fillna(0)
            city_sums = city_df.groupby("City")[ ["Activation", "Registration"] ].sum()
            city_sums.columns = ["مجموع التفعيل", "مجموع التسجيل"]
            st.dataframe(city_sums)
            # Visualization: bar chart of activation and registration by city
            city_sums_sorted = city_sums.sort_values(by="مجموع التفعيل", ascending=False)
            st.write("#### رسم بياني: التفعيل والتسجيل حسب المدينة")
            st.bar_chart(city_sums_sorted)
        else:
            st.write("الملف لا يحتوي على أعمدة 'Activation' و/أو 'Registration'.")

    # مجموعات حسب الاسم
    if "Name" in df.columns:
        st.write("### مجموع التفعيلات ومجموع التسجيلات حسب الاسم")
        name_df = df.copy()
        if "Activation" in name_df.columns and "Registration" in name_df.columns:
            name_df["Activation"] = pd.to_numeric(name_df["Activation"], errors="coerce").fillna(0)
            name_df["Registration"] = pd.to_numeric(name_df["Registration"], errors="coerce").fillna(0)
            name_sums = name_df.groupby("Name")[ ["Activation", "Registration"] ].sum()
            name_sums.columns = ["مجموع التفعيل", "مجموع التسجيل"]
            # allow user to pick top-N names to visualize (to avoid huge charts)
            max_n = min(200, len(name_sums))
            top_n = st.slider("اختر عدد الأسماء الأعلى للعرض", min_value=5, max_value=max_n if max_n>=5 else 5, value=min(20, max_n))
            # show table for top_n by activation
            name_sums_by_activation = name_sums.sort_values(by="مجموع التفعيل", ascending=False).head(top_n)
            st.write(f"#### أعلى {top_n} أسماء حسب مجموع التفعيل")
            st.dataframe(name_sums_by_activation)
            st.write("#### رسم بياني: أعلى الأسماء حسب التفعيل والتسجيل")
            st.bar_chart(name_sums_by_activation)
        else:
            st.write("الملف لا يحتوي على أعمدة 'Activation' و/أو 'Registration'.")


if __name__ == "__main__":
    st.set_page_config(page_title="محلل الإكسل", layout="wide")
    st.title("📊 أداة تحليل الإكسل - التفعيلات والتسجيلات")

    uploaded_file = st.file_uploader("اختر ملف إكسل", type=["xls", "xlsx"])
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            analyze(df)
        except Exception as e:
            st.error(f"حدث خطأ عند قراءة الملف: {e}")
