import streamlit as st 
from PyPDF2 import PdfReader

from backend import get_details, recommend_courses, industry_trends, highlight_action_items, personal_branding, career_dev_ops


with open('main.css') as f:
	st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.title("Performance Review analyzer")

st.subheader("""Analyze ,Evaluate ,Acknowldge Your Employees""")

placeholder = st.empty()
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns([4,1])
col6, col7 = st.columns([4,1])

col8, col9 = st.columns([4,1])





with st.sidebar:

	st.header("Please add the performance review file")

	with st.form(key="form"):


		uploaded_file = st.file_uploader("Choose a file", type='pdf')


		submit_button = st.form_submit_button(label='Submit Data')




if submit_button:

	with open('style.css') as f:
		st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


	with open('uploaded.pdf', 'wb') as f:
		f.write(uploaded_file.getvalue())

	reader = PdfReader('uploaded.pdf')

	pages = reader.getNumPages()
	

	with col1:
		with st.spinner("Getting Details"):

			st.subheader("Details")
			out = get_details(reader.pages[0].extract_text())

			st.markdown(f"<p>{out}</p>", unsafe_allow_html=True)

		with st.spinner("Carrer Opportunities"):
			st.subheader("Career opportunities")

			performance_text = ''
			for i in range(pages-2, pages):
				performance_text += reader.pages[i].extract_text()

			out = career_dev_ops(performance_text)

			st.markdown(out)








	with col2:
		with st.spinner("Recommending Courses"):

			st.subheader("Recommended Courses")

			performance_text = ''
			for i in range(pages-2, pages):
				performance_text += reader.pages[i].extract_text()

			output = recommend_courses(performance_text)
			st.markdown(output)

	with col3:

		with st.spinner("Getting Trends"):

			st.subheader("Trends")

			input_text = reader.pages[i-2].extract_text() + reader.pages[i-1].extract_text()

			output = industry_trends(input_text)

			st.markdown(output)

	with col4:

		with st.spinner("Generating Actions"):

			st.subheader("Action Items for next Year")

			input_text = reader.pages[2].extract_text() + reader.pages[3].extract_text()
				
				

			out = highlight_action_items(input_text)

			st.markdown(out)

	with col6:
		with st.spinner("Facts for personal branding"):

			st.subheader("Personal Branding")

			output = personal_branding(performance_text)

			st.markdown(output)


	with col8:

		with st.spinner("Develop the personal skills"):

			st.subheader("Personal Skills")

			output = personal_branding(performance_text)

			st.markdown(output)






		







