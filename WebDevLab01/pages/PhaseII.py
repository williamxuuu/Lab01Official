import streamlit as st
import pandas as pd
import json
import plotly.express as px
from datetime import date 


with open("data.json") as file:
    data = json.load(file)

patients = data["patients"]
#initializing

st.title("Feline Medical Care of Atlanta")
st.subheader("Tracking the Health of Cats All Over Atlanta")
st.image("/Users/williamxu/Documents/CS1301/Lab/WebDevLab01/images/happycatdoc.jpg", width = 200)


df = pd.DataFrame(patients)# making dataframe

tab1, tab2, tab3 = st.tabs(["Cat Search", "Cat Compare", "Graph Compare"], width = "stretch")
#organizing my application by tabs

with tab1:

    st.image("/Users/williamxu/Documents/CS1301/Lab/WebDevLab01/images/doctorcat.jpg", width = 200)

    
    st.header("Cat Search Engine")

    search = st.text_input("Enter Cat ID")

    if search:
        found = False
        for cat in patients:
            
            if cat["ID"] == search:
                st.subheader(f"Results found for: {cat['Name']}")
                st.text(f"Age: {cat['Age']}")
                st.text(f"Weight: {cat['Weight']}")
                st.text(f"Weight: {cat['Diagnosis']}")
                found = True
                break

        if not found:
            st.warning("No cat found with that ID!")
    
    

    

with tab2:

    
        
    
    st.image("/Users/williamxu/Documents/CS1301/Lab/WebDevLab01/images/clipboard.png", width = 200)
    st.header("Cat Comparison Tool")

    cat_names = []
    for cat in patients:
        cat_names.append(cat["Name"])

    with st.form("multi_select_form"):
        choosecat = st.multiselect("Which Cats Would You Like to Compare", cat_names, max_selections = 5 )
        
        
        st.session_state["choosecat"] = choosecat

        choosestat = st.selectbox("Which Stat Would You Like to Compare (Select 1)", ["Age", "Weight"] )
        
        st.session_state["choosestat"] = choosestat


        #NEW 
        submit = st.form_submit_button("Submit")
        if submit:
            
            graph_dict = {}
    
            for d in patients:
                if d["Name"] in st.session_state["choosecat"]:
                    graph_dict[d["Name"]] = d[st.session_state['choosestat']]
            st.bar_chart(graph_dict)
            
    

    



    
with tab3:
    st.image("/Users/williamxu/Documents/CS1301/Lab/WebDevLab01/images/graphpic.png", width = 200)
    st.header("Graphical Comparison Tool")
    
    
    
    graph_names = []
    for cat in patients:
        graph_names.append(cat["Name"])

    with st.form("multi_graph_form"):
        selectcat = st.multiselect("Which Cats Would You Like to Compare", graph_names, max_selections = 5 )
        
        
        st.session_state["selectcat"] = selectcat

        selectstat = st.selectbox("Which Stat Would You Like to Compare (Select 1)", ["Age", "Weight"] )
        
        st.session_state["selectstat"] = selectstat


        #NEW 
        submit = st.form_submit_button("Submit")
        if submit:
            
            graph_dict = {}
    
            for d in patients:
                if d["Name"] in st.session_state["selectcat"]:
                    graph_dict[d["Name"]] = d[st.session_state['selectstat']]
            st.bar_chart(graph_dict)
            
    

    





























