def calculate_discount(cart_total, total_products, products, cart):
    discount = 0
    applied_discount = ""

    
    if cart_total > 200:
        discount = max(discount, 10)
        applied_discount = "flat_10_discount"


    if any(quantity > 10 for quantity in cart.values()):
        discount = max(discount, 0.05 * cart_total)
        applied_discount = "bulk_5_discount"



    if total_products > 20:
        discount = max(discount, 0.10 * cart_total)
        applied_discount = "bulk_10_discount"


    
    if total_products > 30 and any(quantity > 15 for quantity in cart.values()):
        discounted_quantity = sum(max(0, quantity - 15) for quantity in cart.values())
        discount = max(max_discount, 0.50 * sum(products[product] * quantity for product, quantity in cart.items() if quantity > 15))
        applied_discount = "tiered_50_discount"

    return discount, applied_discount

def main():
    products = {"A": 20, "B": 40, "C": 50}  
    cart = {}
    gift_fee =0
    while True:
        print("Available Products:")
        for product, price in products.items():
            print(f"{product}: ${price}")

        product_name = input("\nSelect a product (A/B/C): ")  
        if product_name.upper() not in products:
            print(" select a valid product.")
            continue

        quantity = int(input(f"Enter quantity of  a  Product {product_name.upper()}: "))  
        
        
        is_gift = input(f" Product {product_name.upper()} wrapped as a gift (yes/no): ").lower() == "yes"

        if is_gift :
            gift_fee += quantity 
        
        product_price = products[product_name.upper()] + (1 if is_gift else 0)

        total_amount = quantity * product_price
        cart[product_name.upper()] = cart.get(product_name.upper(), 0) + quantity  

        continue_purchase = input("\nContinue purchasing (yes/no): ").lower()
        if continue_purchase != "yes":
            break

    
    total_products = sum(cart.values())
    
    print(f"\nTotal products in  cart: {total_products}")

    
    
    cart_total = sum(cart[product] * products[product] for product in cart)

    
    discount_amount, applied_discount = calculate_discount(cart_total, total_products, products, cart)
    
    subtotal = cart_total - discount_amount
    
    shipping_fee = shipping_fee = max(5, (total_products + 9) // 10 * 5)
    
    gift_wrap_fee = gift_fee  
    
    total_cost = subtotal + shipping_fee + gift_wrap_fee - discount_amount  

    
    print(f"\nCost of Products: ${subtotal}")
    print(f"Discount : {applied_discount}, Discount Amount : ${discount_amount}")
    
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print(f"Shipping Fee: ${shipping_fee}")
    print("\n")
    print(f"Payable Amount: ${total_cost}")

if __name__ == "__main__":
    main()
