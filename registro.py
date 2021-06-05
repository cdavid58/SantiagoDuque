import pymysql.cursors
from time import sleep
from sys import argv
from dbf import *

class Registro:

	def __init__(self,compania):
		self.MyDB = pymysql.connect(host="159.203.170.123",port=3306,user='root',passwd="medellin100",db="dbFacturacionElectronica1",charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)	
		self.cursor = self.MyDB.cursor()
		self.compania = compania[0]

	def idCompania(self):
		try:
			queryCompania = "SELECT ID FROM a_compania WHERE nit="+str(self.compania)
			cp = self.cursor.execute(queryCompania)
			compa = self.cursor.fetchone()
		except Exception as e:
			print('No existe compania',e)
			sys.exit()
		return compa['ID']

	def lectura_dbf(self,columna):
		table = Table(r'C:\BASURA2\tmpvenfe.dbf')
		table.open()
		dato = []
		for i in table:
			dato.append(str(i[columna]).strip())
		return dato

	def scannerClient(self,i):
		try:
			queryClienteNit = "SELECT ID FROM a_cliente WHERE cc='"+str(self.lectura_dbf('Cc_nit')[i])+"'"
			nc = self.cursor.execute(queryClienteNit)
			nitCliente = self.cursor.fetchone()
		except Exception as e:
			print(e)

		if nitCliente is not None:
			return nitCliente['ID']
		else:
			try:
				query = "INSERT INTO a_cliente(tcliente,tregimen,cc,nombre,domicilio,telefono,email,tipodoc,compania_id)VALUES('"+str(self.lectura_dbf('Tcliente')[i])+"', '"+str(self.lectura_dbf('Tregimen')[i])+"', '"+str(self.lectura_dbf('Cc_nit')[i])+"','"+str(self.lectura_dbf('Nombres')[i])+"', '"+str(self.lectura_dbf('Domicilio')[i])+"','"+str(self.lectura_dbf('Telefono')[i])+"','"+str(self.lectura_dbf('Email')[i])+"', '"+str(self.lectura_dbf('Tdocmto')[i])+"','"+str(self.idCompania())+"')"
				self.cursor.execute(query)
				self.MyDB.commit()
			except Exception as e:
				print('Error',e)
			

	def crearFactura(self):
		try:
			for i in range(len(self.lectura_dbf('codigo'))):
				fechaV = ""
				if self.lectura_dbf('Fpago')[0] == "CR":
					fechaV = str(self.lectura_dbf('VENCE')[0])
				else:
					fechaV = str(self.lectura_dbf('Fecha')[0])


				ipo = self.lectura_dbf('ipoc')[i] if self.lectura_dbf('ipoc')[i] != 'None' else 0

				query = """INSERT INTO a_facturafinal(numero,prefijo,codproducto,producto,cantidad,precio,iva,descuento,retefuente,ipo,formaPago,diasVen,decuentoFactura,tipoFactura,fechaGenerada,estado,cliente_id,compania_id,observacion)
				VALUES('"""+ str(self.lectura_dbf('Factura')[0]) +"""','FE','"""+ str(self.lectura_dbf('Codigo')[i]) +"""','"""+ str(self.lectura_dbf('Articulo')[i]) +"""','"""+str(self.lectura_dbf('Cant')[i])+"""',
						'"""+str(self.lectura_dbf('Valunit')[i])+"""','"""+str(self.lectura_dbf('iva')[i])+"""','"""+str(self.lectura_dbf('Dcto')[i])+"""','0','"""+str(ipo)+"""','"""+str(self.lectura_dbf('Fpago')[0])+"""',
						'"""+fechaV+"""','0','1','"""+str(self.lectura_dbf('Fecha')[0])+"""','Sin Enviar a la Dian','"""+str(self.scannerClient())+"""','"""+str(self.idCompania())+"""','"""+str(self.lectura_dbf('Observa')[0] if str(self.lectura_dbf('Observa')[0]) != "" else 'No hay observaciones.' )+"""'

				)"""
				self.cursor.execute(query)
			self.MyDB.commit()
			return 'Correcto'
		except Exception as e:
			print('Error',e)


			


if __name__ == '__main__':
	r = Registro(argv[1:])
	print(r.crearFactura())
	


