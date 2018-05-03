import os, time, Funciones;
f = Funciones;
	
productos = ['zapallo','limon','cebolla','pera','pina'];
precios = [200,500,300,450,1000];
carro = [];
opc=0;
opc2=0;

while True:
	
	f.menu1();															#menu principal
	opc= input("Ingrese una Opcion: ");
	
	while (opc not in ('1','2','3','4')):	
		f.menu1();							
		print ("\n"+"-"*5," ERROR:Ha ingresado una opcion invalida"+"-"*5,"\n")
		opc= input("Ingrese Opcion Valida: ");
	
	if (opc == '1'):                                                    #ingresando producto
		
		f.ingresarProductos(productos,precios);			
			
	elif (opc == '2'):													#opcion compra
		carro = [];
		f.comprarp(carro, productos, precios);
		
	elif (opc == '3'): 													#opcion de modificacion y borrar
		f.menu2();
		opc2 = input("Ingrese una opcion: ");
		while (opc2 not in ('1','2','3')):	
			f.menu2()							
			print ("\n"+"-"*5," ERROR:Ha ingresado una opcion invalida"+"-"*5,"\n")
			opc2= input("Ingrese Opcion Valida: ");
		
		if(opc2 == '1'):	
															#modificar
			f.modprod(productos,precios);
		
		elif (opc2 == '2'):
			f.borrarprod (productos,precios);
		else:
			print("\n"+"...Volviendo al menu principal...");
			time.sleep(2);
		
	elif (opc == '4'):													#opcion salir
	
		print("\n"+"...Saliendo...");
		break
		
	else:
		
		print("...Opcion Incorrecta Reingrese...");
