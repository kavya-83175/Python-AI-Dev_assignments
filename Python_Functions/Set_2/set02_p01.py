
def place_order(customer,*items,**charges):
    print("Customer : ",customer)
    for i,item in enumerate(items,start=1):
        print(i,".",item)
    for key,value in charges.items():
        print(f"{key:10}"," : ",value)

place_order("Kavya","Biryani","Pizza",delivery=40, gst=25, discount=50)
