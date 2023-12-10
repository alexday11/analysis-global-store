import streamlit as st
import pandas as pd
from Graph import Display_Sales_category, Display_Sales_cate_year,Display_Profit_cate_year,DisplayCountry_category,Display_sales_segment,Display_top_order_sales,Display_Sales_date_trend,Display_Sales_year,Display_Quantity_sales,Display_month_sales,Display_avg_each_year,Display_market_sale_profit,display_market_category,Display_Sales_shipMode,Display_Sales_shipMode,Display_discount_profit,Display_profit_shipMode,market_profit,Display_growth_ratio



st.set_page_config(
    page_title = 'Global superstore',
    page_icon='',

)

# Data
df = pd.read_csv('superstore.csv')
df['Order.Date'] = pd.to_datetime(df['Order.Date'])
category_sales =  df.groupby('Category').agg({'Sales':'sum','Profit':'sum'})
growth_cate_year = pd.pivot_table(data=df , index='Year', columns='Category', values=['Sales','Profit'],aggfunc=['sum'])
country_category = pd.pivot_table(data=df, index=['Country','Category'],values='Sales',aggfunc='sum')
customer_sales = df.groupby('Segment').agg({'Sales':['sum','mean']})
customer_order_sales  = pd.pivot_table(data=df, index=['Customer.ID','Segment'],values='Sales',aggfunc='sum').reset_index()
top_order_sales_sort = customer_order_sales.sort_values('Sales',ascending=False)
Date_trend = df.groupby('Order.Date').agg({'Sales':'sum'})
Date_trend_resampling = Date_trend.resample('7d').mean()
date_sale = df.groupby('Year').agg({'Sales':'sum'})
sales_qual = pd.pivot_table(df, index=['Year'], values=['Sales', 'Quantity'], aggfunc='sum').reset_index()
month_sale = df.groupby(df['Order.Date'].dt.month).agg({'Sales':'sum'})
customer_avg = pd.pivot_table(data=df, index=['Year'], values='Sales', aggfunc='median')
market_group = df.groupby('Market').agg({'Sales':'mean','Profit':'mean'})
market_category = pd.pivot_table(data=df, index=['Market','Category'],values=['Sales','Profit'], aggfunc='sum')
market_growth = pd.pivot_table(data=df , index='Year',columns='Market', values=['Sales','Profit'], aggfunc='sum')
top_5_country_grow = pd.read_csv('./top_5_country_grow.csv',index_col='Country')



st.title("Global Superstore")
st.image('./market.jpg')
st.header('Product Categories and Sales',divider='gray')

st.markdown("""
            Let's examine the overall sales performance to identify the products with the highest sales or purchases. Notably, Office Supplies products lead in the number of orders, representing 60 percent of all product categories. Following closely are Technology and Furniture products, respectively. The dominance of office supplies in orders is expected, given their affordability and frequent usage.

However, it's essential to look beyond order numbers. The subsequent graph reveals the total sales of product categories, where Technology products take the lead, followed by Furniture. While sales are crucial, profitability is equally important. The next graph illustrates that Technology products not only boast the highest sales but also contribute significantly to the store's profit. Office Supplies products follow closely, demonstrating their capacity to generate substantial profits.

These insights highlight a trend of potential growth in sales for each product category in the coming years.


  Moving on, let's explore which types of products perform well in different countries. For instance, in the United States, Technology products dominate sales, influenced by factors such as market size, diversity, and the country's role as a global center for innovation. With a population exceeding 330 million, the U.S. market accommodates various products and services, while a culture of innovation continuously introduces new and advanced products, driving consumer interest.

In contrast, Afghanistan experiences high sales in Furniture, likely influenced by cultural factors emphasizing the importance of home aesthetics and traditional home decoration practices. Understanding local preferences is crucial for manufacturers and retailers to cater to diverse markets.

For a personalized exploration of your country's trends, I've created an interactive graph to assist you in visualizing the data.
            """)
Display_Sales_category(category_sales)
Display_Sales_cate_year(growth_cate_year)
Display_Profit_cate_year(growth_cate_year)

names_country = country_category.index.get_level_values(0).tolist()
names_country[0] = 'United States'
names1  = st.selectbox('Select:',names_country,key='select1')
DisplayCountry_category(country_category, names1)


st.header("Customer Analysis",divider='gray')
st.markdown("""
            Now, let's delve into an overview of customer types. The data reveals three main categories: 1. Consumer, 2. Corporate, and 3. Home Office. Unsurprisingly, consumers contribute significantly to order numbers, given their large representation. However, our focus shifts to identifying the customers making the most purchases, with customer JG-158051 standing out with an impressive 40 orders. A closer look at the data shows that this customer consistently places orders, particularly in June, accounting for 17 orders or 42 percent of their total orders.

This pattern is not unique, as demonstrated by another example: customer number 3, who places a total of 37 orders, with 16 purchases concentrated in December, making up 43 percent of their order frequency. These insights into individual customer behavior become invaluable when the store plans promotions or campaigns, ensuring they are both effective and tailored to meet consumer needs.

However, it's essential to note that frequent customers, as identified from the graph, may not necessarily have the highest order count. There exists another customer type that responds to different promotions or initiatives. Our interest extends beyond frequent customers to those who make one-time purchases and those with repeat purchases.

Analyzing the data further, customers with a single purchase have an average sales amount of $142.69, while  those  making repeat purchases average $257.39. This information can be strategically employed; for instance, setting a target average order amount of $250 for one-time customers may incentivize them to become repeat customers.
            """)

Display_sales_segment(customer_sales)
Display_top_order_sales(top_order_sales_sort)


st.header("Order Placement and Trends",divider='gray')
st.markdown("""
            Let's now analyze the overall pattern of order placement over time. While the graph may initially seem intricate, I've simplified it by averaging the 7-day sales data, making it more accessible. From the beginning of 2011 to the end of 2014, the store's overall sales exhibited a consistent upward trend. This positive trajectory suggests a favorable aspect for each store, with the sales picture indicating continuous growth.

Taking a closer look at the graph depicting the number of orders, it's evident that the quantity has been steadily increasing each year. This growth is indicative of a rising influx of new customers placing orders. A deeper examination reveals monthly sales trends, with a noticeable surge in the middle of the year, particularly in November and December. These months coincide with peak holiday seasons, including Super Bowl, Labor Day, Thanksgiving, and Christmas. Weeks surrounding these holidays carry significantly more weight in evaluations, often marked by company bonuses, which likely contribute to the spike in product orders. Notably, Technology products, particularly phones, dominated orders at the end of the year.

Beyond sales, the analysis extends to store operations, showing a consistent upward trend in profits each year, a positive observation from the data. However, a caveat arises when considering the average sales volume. The next graph indicates a yearly decrease in the average order amount per person. While the growth in sales may be attributed to an increased number of people placing orders, it raises concerns if this trend continues. A decline in the quantity or value of product orders in the future could pose challenges and potential harm.
            """)

Display_Sales_date_trend(Date_trend,Date_trend_resampling)
Display_Sales_year(date_sale )
Display_Quantity_sales(sales_qual)
Display_month_sales(month_sale)
Display_avg_each_year(customer_avg)


st.header("Market Anlysis",divider='gray')
st.markdown("""
            Let's delve into market growth in each region, considering overall sales. To ensure fairness to regions and countries with varying sizes, we'll examine a graph displaying the average sales in each market. This approach avoids potential unfairness associated with using total sales, especially for regions and countries with smaller numbers, such as Canada. The graph highlights that the APAC region exhibits the highest average sales, closely followed by the EU.

Now, let's explore the countries that experienced sales growth from the beginning of 2011 to the end of 2014. However, our current focus remains on average sales. The subsequent graph reveals that Canada emerges as the market with the highest average profits, with the APAC and EU regions following suit. This prompts an exploration into the factors contributing to Canada's leading position in regional market profitability.

To understand this further, we turn to a correlation table showcasing relationships between various factors. Notably, the cost of shipping and sales demonstrate a positive correlation, suggesting that higher shipping costs may influence increased sales. Examining another relationship, we find that profitability and early delivery correlate with low wholesale prices. The graph indicates a grouping effect where lower wholesale prices tend to result in higher profits, especially when shipping costs are lower.

Another evident factor is the relationship between profitability and product price reduction. Lower prices offer advantages, especially during festivals or inventory clearance. However, the graph illustrates that price cuts may impact outcomes—higher prices lead to limited flexibility, potentially resulting in either high profits or significant losses.

Looking at the subsequent graph, we observe that markets in the EMEA region have the highest number of discounted products and are the least profitable. In contrast, the Canadian market shows no regional price declines, positioning it as a market capable of generating the highest profits. The data strongly suggests that price reductions significantly influence profitability.
            """)

Display_market_sale_profit(market_group)
name_counry2 = market_category.index.get_level_values(0).tolist()
name_counry2[0] = 'APAC'
names2 = st.selectbox('Selected:',name_counry2,key='select2')
display_market_category(market_category,names2)
#Display_Sales_shipMode(df)
#Display_profit_shipMode(df)
Display_discount_profit(df)

st.header('Market Growth and Regions',divider='gray')
st.markdown("""
            Expanding upon the previous analysis, let's delve into the countries that are likely to drive growth within their regional markets. Our initial graph highlights that regions experiencing higher overall sales and profitability often correlate with substantial growth. Examining the period from 2011 to 2014, certain countries have emerged as significant contributors to this growth.

In the APAC market, we initially observe the market share distribution in 2011, with China leading at 34.25 percent, followed by Australia at 21.25 percent, and India. By 2014, the landscape has shifted, with Australia claiming the top spot at an impressive 49.23 percent market share, followed by China at 34.25 percent, and India. However, the critical factor lies in the growth rate during this period.

Australia stands out with the highest growth rate, soaring from an initial proportion of 27.71 to an impressive 102.08 percent. This substantial growth is a testament to Australia's relatively stable and developed economy, fostering consumer confidence and increased spending across various sectors.

India, with a growth proportion of 17.71, saw significant expansion, growing from the original to 69.55 percent. The country's second-largest population globally and a growing pool of talented individuals have contributed to advancements across diverse sectors.

China, while initially holding the top market share, fell to the fourth position in terms of growth rate. Indonesia took the third spot, showcasing its emerging role in driving market growth within the APAC region.

To provide a more personalized exploration, interactive graphs have been developed for you. These graphs allow you to assess the influence of specific countries on markets in your region of interest.
            """)

market_profit(market_growth)
Display_growth_ratio(top_5_country_grow)



st.header("Summary",divider='gray')
st.markdown("""
            **1. Product Categories and Sales**

- Office Supplies products lead in the number of orders, representing 60 percent of all product categories.
- Technology and Furniture products follow in order, with Technology having the highest overall sales.
- Technology products stand out for both high sales and profitability, making them a significant contributor to store profits.

**2. Customer Analysis**

- Customers are categorized into Consumer, Corporate, and Home Office groups.
- Notable customers, like JG-158051, provide insights into order patterns and frequency.
- Analysis of one-time purchasers versus repeat customers reveals differences in average order amounts.

**3. Order Placement and Trends:**

- Examining the overall pattern of order placement shows a positive sales trend from 2011 to 2014.
- Peak sales months, especially November and December, indicate the influence of holiday seasons and events.
- While overall sales and profits are growing, the average order amount per person is decreasing, signaling a potential concern.

**4. Market Growth and Regions**

- regions with higher overall sales and profitability contribute significantly to market growth.
- The APAC region has the highest average sales, with Australia showing the highest average profits.
- Analysis of the APAC market from 2011 to 2014 reveals Australia as the leader in growth, followed by India.


**5. Factors Influencing Profitability**

- Correlation analysis highlights relationships between factors such as shipping costs, sales, and profitability.
- Lower wholesale prices and early delivery correlate with higher profitability, while higher shipping costs may lead to increased sales.
- Price reductions can impact profitability, with regions like EMEA having the highest number of discounted products and lower overall profitability.
Interactive Graphs:


In summary, the analysis provides a comprehensive understanding of product sales, customer behavior, order trends, market growth, and factors influencing profitability. The information suggests opportunities for strategic decisions, such as targeted promotions and understanding regional market dynamics.
            """)