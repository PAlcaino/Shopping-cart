import os, time;

def menu1 ():
	os.system('cls');
	print("-"*50);
	print("-"*14," Caja Resgistradora ","-"*14);
	print("-"*50,"\n");
	print("1)Ingresar Productos ");
	print("2)Realizar Venta ");
	print("3)Borrar/Modificar Productos ");
	print("4)Salir \n");
	print("-"*50);

def menu2 ():
	os.system('cls');
	print("-"*50);
	print("-"*14," Caja Resgistradora ","-"*14);
	print("-"*50,"\n");
	print("1)Modificar Productos ");
	print("2)Borrar Productos ");
	print("3)Volver ","\n");
	print("-"*50);
	
def imprimirproductos (lproducto,lprecio):	
	os.system('cls');
	print ("-"*24," Lista de productos ","-"*24,"\n");	
	i=1;
	print ("    Nombre".ljust(17," "),"  Precio Unitario\n".ljust(17," "));
	for e,f in zip(lproducto,lprecio):
		f=str(f);
		print (i,")",e.ljust(15," "),"$",f.ljust(15," "));
		i=i+1;
	print ("\n\n");
	
def ingresarProductos (lproducto,lprecio):
	os.system('cls');
	
	
	nproducto = '';
	while (nproducto != 's'):
		os.system('cls');	
		
		imprimirproductos(lproducto,lprecio);		
		print("-"*24,"Ingresando Productos","-"*25,"\n")
		
		nproducto = input ("Ingrese nombre del producto o escriba 's' para finalizar: ");
		
		while(nproducto in lproducto and nproducto != 's'):
			os.system('cls');	
			imprimirproductos(lproducto,lprecio);		
			print("-"*24,"Ingresando Productos","-"*25,"\n")
			print("\n"+"-"*13," ERROR: producto ya se encuentra ingresado ","-"*13,"\n");
			nproducto = input ("Ingrese un nombre que no se encuentre en la lista o 's' para finalizar: ");
		
		if (nproducto == 's'):
			break
				
		pproducto = input("Ingrese precio del producto: ");
		while(pproducto.isdigit()== False or int(pproducto)<=0):
			os.system('cls');	
			imprimirproductos(lproducto,lprecio);	
			print("-"*24,"Ingresando Productos","-"*25,"\n")	
			print("\n"+"-"*13," ERROR: Precio debe ser un numero mayor a 0 "+"-"*13,"\n");		
			pproducto = input("Ingrese precio del producto: ");
		pproducto = int(pproducto);
			
		lproducto.append (nproducto);
		lprecio.append (pproducto);
		print ("\n\n....Producto ingresado con exito!....")
		time.sleep(1)
	print("\n\n....Volviendo al menu principal...")
	time.sleep(2)
		

			
def	comprarp(lcarro,lproducto, lprecio):
	comprar = '';
	total=0;
	lcantidad = [];		
	precioaux = [];
	
	while True:
		if (len(lproducto) == 0):
			print("\n"+"-"*13," Error: No hay productos en la lista ","-"*13,"\n");
			time.sleep(2)
			break
		
		imprimirproductos (lproducto,lprecio);
		print("-"*25,"Realizando Compra","-"*25,"\n")
		
		comprar = input("\nIngrese producto a comprar o 'f' para finalizar compra: ");
		if (comprar == 'f'):
			break
		
		while (comprar not in lproducto):
			imprimirproductos (lproducto,lprecio);
			print("-"*25,"Realizando Compra","-"*25,"\n")
			print("\n"+"-"*13+" ERROR:Producto no se encuentra en la lista "+"-"*12+"\n");		
			comprar = input("Reingrese nombre de producto a comprar: ");
		
		cant = 	input("Ingrese cantidad a comprar: ");
		while (cant.isdigit() == False or int(cant)<=0):
			imprimirproductos (lproducto,lprecio);
			print("-"*25,"Realizando Compra","-"*25,"\n")
			print("\n"+"-"*12+" ERROR:cantidad debe ser un numero mayor a 0 "+"-"*12+"\n");	
			cant = 	input("Reingrese cantidad: ");
			
		cant = int(cant);			
		
		
			
		lcantidad.append (cant);
		lcarro.append(comprar);
		print("\nProducto ingresado al carro de compras...");
		time.sleep(1)
#Boleta		
	if (len(lcarro) > 0):	
					
		for e in lcarro:
			for i in lproducto:
				if(e == i):
					precioaux.append(lprecio[lproducto.index(i)])					
									
		os.system('cls');
		print("-"*68);
		print("-"*30,"BOLETA","-"*30);
		print("-"*68);
		print("Fecha:"+time.strftime("%d/%m/%y").ljust(15," "),"Hora:"+time.strftime("%H:%M:%S").ljust(15," "));
		print("\n\nProducto".ljust(22," "),"Cantidad".ljust(17," "),"Precio".ljust(20," "),"Total".ljust(20," "),"\n");
		i=1;
		for e,f,g in zip(lcarro,lcantidad,precioaux):
			p = str(g);
			q = str(f*g);
			r = str(f);
			print (i,".-",e.ljust(15," "),r.ljust(17," "),"$",p.ljust(18," "),"$",q.ljust(20," ") );
			i = i+1;
			total = total + (f*g);
		print ("\nTOTAL COMPRA:".ljust(60," "),"$",total,"\n\n");
		print("-"*68);
		print("-"*30,"BOLETA","-"*30);
		print("-"*68);
		
		salir= input('\n'+'....Ingrese cualquier caracter para continuar....');

def borrarprod (lproducto,lprecio):
	while True:
		if (len(lproducto) == 0):
			print("\n","-"*13," ERROR: No hay productos en la lista ","-"*13,"\n");
			print ("Volviendo al menu principal...")
			time.sleep(2)
			break
		productob = '';
		
		
		imprimirproductos(lproducto,lprecio);
		print("-"*25,"Borrando Productos","-"*25,"\n")
	
		productob = input ("Ingrese nombre del producto a eliminar o escriba 's' para finalizar: ");
		if (productob == 's'):
			break
		
	
		while (productob not in lproducto):
			imprimirproductos(lproducto,lprecio);
			print("-"*25," Borrando Productos ","-"*25,"\n")
			print ("-"*13," ERROR: Producto no se encuentra en la lista ","-"*13,"\n\n");
			productob = input ("Ingrese producto nuevamente: ")
			
			
		indicep = lproducto.index(productob);
		del lproducto[indicep];
		del lprecio[indicep];
		print ("...Producto eliminado con exito...")
		time.sleep(1)

def modprod (lproducto,lprecio):
	while True:
		if (len(lproducto) == 0):
			print ("-"*13+" ERROR: No hay productos ingresados "+"-"*13,"\n\n");
			print ("...Volviendo al menu principal...")
			time.sleep(2)
			break
		productom = '';
	
		imprimirproductos(lproducto,lprecio);
		print("-"*23," Modificando Productos ","-"*22,"\n")
		
		productom = input ("Ingrese nombre del producto a modificar o escriba 's' para finalizar: ");
		if (productom == 's'):
			break
		
	
		while (productom not in lproducto and productom != 's'):
			imprimirproductos(lproducto,lprecio);
			print("-"*23," Modificando Productos ","-"*22,"\n")
			
			print ("\n"+"-"*12," ERROR: Producto no se encuentra en la lista "+"-"*12+"\n\n");
			productom = input ("Ingrese producto nuevamente o 's' para salir: ")
		if (productom == 's'):
			break
		
		for e in range(len(lproducto)):
			
			if (productom == lproducto[e]):
				lproducto[e] = input ("Ingrese nuevo nombre: ");
				lprecio [e] = input ("Ingrese nuevo precio: ");
				while (lprecio[e].isdigit() == False or int(lprecio[e])<=0):
					imprimirproductos(lproducto,lprecio);
					print("-"*23," Modificando Productos ","-"*22,"\n")
					print("\n"+"-"*13," ERROR: Precio debe ser un numero mayor a 0 ","-"*13,"\n");	
					lprecio [e] = input("Reingrese Precio: ");
			
				
				
			
			



