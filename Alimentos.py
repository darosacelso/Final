#Base de datos en Excel
import openpyxl
book= openpyxl.workbook()
book.create_sheet('Producto')
Producto_page=book['Producto']
Producto_page.append(['PRODUCTO','CANTIDAD',.PRECIO])
Producto_page.append(['arroz','5', '$120,00'])
book.save('Productos Alimenticios.xlsx')

