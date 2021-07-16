"""Data Warehouse == Server + Dashboard + Indexing."""

# Server

install PostgeSQL

pip install sqlalchemy

from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import streamlit as st

### create new table

p_engine = create_engine("postgresql://<username>:<password>@localhost:5432//records_db")
p_engine_dataset = create_engine("postgresql://<username>:<password>@localhost:5432/datasets_db")
p_engine.execute("CREATE TABLE IF NOT EXISTS records (name text PRIMARY KEY, details text[])")

# If you want to store your database credentials in a secure way then save
# them in a configuration_file and then invoke them as parameters in your code
# as per your requirement.

### make functions for CRUD

def write_record(name, details, p_engine):
    p_engine.execute("INSERT INTO record (name, details) VALUES ('%s', '%s')" % (name, details))

def read_record(field, name, p_engine):
    result = p_engine.execute("SELECT %s FROM records WHERE name = '%s'" % (field, name))
    return result.first()[0]

def update_record(field, name, new_value, p_engine):
    p_engine.execute("UPDATE records SET %s = '%s' WHERE name = '%s'" % (field, new_value, name))

def write_dataset(name, dataset, p_engine):
    dataset.to_sql('%s' % (name), p_engine, index=False, if_exixs='replace', chuksize=1000)

def read_dataset(name, p_engine):
    try:
        dataset = pd.read_sql_table(name, p_engine)
    except:
        dataset = pd.DataFrame([])
    return dataset

def list_datasets(p_engine):
    datasets = p_engine.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;")
    return datasets.fetchall()

###### Dashboard
# streamlit

st.title('Dashboard')
column_1, column_2 = st.beta_columns(2)

with column_1:
    st.header('Save records')
    name = st.text_input('Please enter name')
    details = st.text_input('Please enter your details (separated by comma ",")')
    details = ('{%s}' % (details))
    if st.button('Save record to database'):
        write_record(name, details, p_engine)
        st.info('Name: **%s** and details: **%s** saved to database' % (name, details[1:-1]))
    st.header('Update records')
    field = st.selectbox('Please select field to update', ('name','details'))
    name_key = st.text_input('Please enter name of record that to be updated')
    if field == 'name':
        updated_name = st.text_input('Please enter your updated name')
        if st.button('Update records'):
            update_record(filed, name_key, updated_name, p_engine)
            st.info('Updated name to **%s** in record **%**' % (updated_name, name_key))
    elif field == 'details':
        updated_details = st.text_input('Please enter updated details (separated by comma)')
        updated_details = ('{%s}' % (updated_details))
        if st.button('Update records'):
            update_record(field, name_key, updated_details, p_engine)
            st.info('Updated details to **%s** in records **%s**' % (updated_details[1:-1], name_key))
    st.header('Read records')
    record_to_read = st.text_input('Please enter name of record to read')
    if st.button('Search'):
        read_name = read_record('name', record_to_read, p_engine)
        read_details = read_record('details', record_to_read, p_engine)
        st.info('Record name is **%s**, record details is **%s**' % (read_name, str(read_details)[1:-1]))
        
with column_2:
    st.header('Save datasets')
    dataset = st.file_uploader('Please upload dataset')
    if dataset is not None:
        dataset = pd.read_csv(dataset)
        dataset_name = st.text_input('Please enter name for dataset')
        if st.button('Save dataset to database'):
            write_dataset('%s' % (dataset_name), dataset, p_engine_dataset)
            st.info('**%s** saved to database' % (dataset_name))

    try:
        read_title = st.empty()
        dataset_to_read = st.selectbox('Please select dataset to read', ([x[0] for x in list_datasets(p_engine_dataset)]))
        read_title.header('Read datasets')
        if st.button('Read dataset'):
            df = read_dataset(dataset_to_read, p_engine_dataset)
            st.subheader('Chart')
            st.line_chart(df['value'])
            st.subheader('Dataframe')
            st.write(df)
    except:
        pass

###### next
streamlit run file_name.py
