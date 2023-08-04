import random

# Sample PLU data (for demonstration purposes)
sample_plu_data = [random.choice(['4011', '4225', '3035', '84011', '93000']) for _ in range(100)]

def generate_analytics(plu_data):
    # Basic statistics on popular produce
    popular_produce = max(set(plu_data), key=plu_data.count)
    popular_produce_count = plu_data.count(popular_produce)

    # Sales trends (frequency of each PLU)
    sales_trends = {plu: plu_data.count(plu) for plu in set(plu_data)}

    # Customer preferences (percentage of each PLU)
    total_sales = len(plu_data)
    customer_preferences = {plu: (plu_data.count(plu) / total_sales) * 100 for plu in set(plu_data)}

    return popular_produce, popular_produce_count, sales_trends, customer_preferences

if __name__ == "__main__":
    # Assuming the script runs periodically to process PLU data
    popular_produce, popular_produce_count, sales_trends, customer_preferences = generate_analytics(sample_plu_data)

    print(f"Most Popular Produce: PLU {popular_produce}, Sold {popular_produce_count} times.")
    print("Sales Trends:")
    for plu, count in sales_trends.items():
        print(f"PLU {plu}: Sold {count} times.")
    print("Customer Preferences:")
    for plu, percentage in customer_preferences.items():
        print(f"PLU {plu}: {percentage:.2f}%")

