# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

def load_data():
    df = pd.read_csv('files/input/shipping-data.csv')
    return df

def create_visual_shipping_per_warehouse(df):
    df = df.copy()
    plt.figure()
    counts = df['Warehouse_block'].value_counts()
    df['Warehouse_block'].value_counts().plot(kind='bar', color='skyblue')
    counts.plot.bar(
        title='Shipping per Warehouse',
        xlabel='Warehouse Block',
        ylabel='Record Count',
        color='tab:blue',
        fontsize=10,
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('docs/shipping_per_warehouse.png')
    plt.close()

def create_visual_mode_of_shipment(df):
    df = df.copy()
    plt.figure()
    counts = df['Mode_of_Shipment'].value_counts()
    counts.plot.pie(
        title='Mode of Shipment',
        wedgeprops=dict(width=0.3),
        ylabel='',
        colors=['tab:blue', 'tab:orange', 'tab:green'],
    )
    plt.savefig('docs/mode_of_shipment.png')
    plt.close()

def create_visual_customer_rating(df):
    df = df.copy()
    plt.figure()
    df = (
        df[['Mode_of_Shipment', 'Customer_rating']]
        .groupby('Mode_of_Shipment')
        .describe()
    )
    df.columns = df.columns.droplevel()
    df = df[['min', 'max', 'mean']]
    plt.barh(
        df.index.values,
        width=df['max'].values - 1,
        left=df['min'].values,
        height=0.9,
        color='lightgray',
        alpha=0.8
    )
    colors = ['tab:green' if value >= 3 else 'tab:orange' for value in df['mean'].values]
    plt.barh(
        df.index.values,
        width=df['mean'].values - 1,
        left=df['min'].values,
        height=0.5,
        color=colors,
        alpha=1.0
    )
    plt.title('Average Customer Rating')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_color('gray')
    plt.gca().spines['bottom'].set_color('gray')
    plt.savefig('docs/average_customer_rating.png')
    plt.close()

def create_visual_weight_distribution(df):
    df = df.copy()
    plt.figure()
    df['Weight_in_gms'].plot.hist(
        color='tab:orange',
        edgecolor='white',
        alpha=0.7
    )
    plt.title('Shipped Weight Distribution')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('docs/weight_distribution.png')
    plt.close()

def pregunta_01():
    """
    El archivo `files/input/shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    os.makedirs('docs', exist_ok=True)
    df = load_data()
    create_visual_shipping_per_warehouse(df)
    create_visual_mode_of_shipment(df)
    create_visual_customer_rating(df)
    create_visual_weight_distribution(df)
