import os
class Products:
	def __init__(self, id, name, group, subgroup):
		self.id=id
		self.name=name
		self.group=group
		self.subgroup=subgroup
		
	def storeProducts(self):
		out=open('product_list.out','a')
		print>>out, "Product ID=%d :: Product Name=%s :: Product Group=%s :: Product Subgroup=%s" % (self.id, self.name, self.group, self.subgroup)
		out.close()

class Admin():
	def __init__(self, id, name):
		self.id = id
		self.name = name

	def ViewProducts(self):
		# print("entered")
		try:
			data = open('product_list.out')
			for each_line in data:
				try:
					each_line=each_line.strip()
					(id, name, group, subgroup) = each_line.split('::')
					print("%s | %s | %s | %s" % (id, name, group, subgroup))
				except ValueError:
					pass
			data.close()
		except IOError:
			print('The product_list file is missing!')


	def AddProducts(self, id, name, group, subgroup):
		product=Products(id, name, group, subgroup)
		product.storeProducts()

	def DeleteProducts(self, id):
		idgiven="Product ID="+str(id)
		temp={}
		temp.clear()
		try:
			data = open('product_list.out')
			for each_line in data:
				try:
					each_line=each_line.strip()
					(id1, name, group, subgroup) = each_line.split(' :: ')
					value = name+' :: '+group+' :: '+subgroup+' '
					temp[id1]=value
				except ValueError:
					pass
			
			if idgiven in temp:
				del temp[idgiven]
			data.close()
			
			out=open('product_list.out','wb')
			for each_line in temp:
				try:
					print>>out, "%s :: %s" % (each_line, temp[each_line])
				except ValueError:
					pass
			out.close()
		except IOError:
			print('The product_list file is missing!')

	def ModifyProduct(self, id, name='',group='',subgroup=''):
		idgiven="Product ID="+str(id)
		temp={}
		temp.clear()
		try:
			data = open('product_list.out')
			for each_line in data:
				try:
					each_line=each_line.strip()
					(id1, name1, group1, subgroup1) = each_line.split(' :: ')
					value = name1+' :: '+group1+' :: '+subgroup1+' '
					temp[id1]=value
				except ValueError:
					pass
			
			if idgiven in temp:
				(name2, group2, subgroup2) = temp[idgiven].split(' :: ')
				if name!='':
					name2="Product Name="+name
				if group!='':
					group2="Product Group="+group
				if subgroup!='':
					subgroup2="Product Subgroup="+subgroup
				temp[idgiven]=name2+' :: '+group2+' :: '+subgroup2+' '
			data.close()
			
			out=open('product_list.out','wb')
			for each_line in temp:
				try:
					print>>out, "%s :: %s" % (each_line, temp[each_line])
				except ValueError:
					pass
			out.close()
		except IOError:
			print('The product_list file is missing!')
		

	#def MakeShipment(self):


	# def ConfirmDelivery(self):

class Customer():
	def __init__(self, id, name, address, phone):
		self.id=id
		self.name=name
		self.address=address
		self.phone=phone

	def BuyProducts():
		pass
	def ViewProducts():
		pass
	def MakeProducts():
		pass
	def AddToCart():
		pass
	def DeleteFromCart():
		pass

class Payment():
	def __init__(self, CustId, name, CardType, CardNo):
		self.CustId=CustId
		self.name=name
		self.CardType=CardType
		self.CardNo=CardNo

class Cart():
	def __init__(self, id, NoOfProducts, *products, price, total):
		self.id=id
		self.NoOfProducts=NoOfProducts
		self.products=products
		self.price=price
		self.total=total

class Guest():
	def __init__(self, GuestId):
		self.GuestId=GuestId
	def ViewProducts():
		pass
	def GetRegistered():
		pass

if __name__=='__main__':
	
	product1=Products(1,'apple','fruits','seasonal')
	product2=Products(2,'coke','beverages','soft-drink')
	product3=Products(3,'bottle','stationary','plastic')
	# print>>out,"hi there"
	product1.storeProducts()
	# print("\n")
	product2.storeProducts()
	# print("\n")
	product3.storeProducts()
	
	admin=Admin(1,'Prabha Pandey')
	# print(admin.id)
	# print(admin.name)
	
	admin.AddProducts(5,'Ponds','cosmetics','cream')
	admin.DeleteProducts(3)
	# admin.ViewProducts()
	admin.ModifyProduct(2,name="Colour Pencil", group="stationary", subgroup="writing")
