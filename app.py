from flask import Flask,jsonify,request



app = Flask(__name__)

from empresas import empresas


@app.route('/empresas',methods=['GET'])
def GETempresas():
   return jsonify(empresas)

@app.route('/empresas/<string:empresas_Denominacion>',methods=['GET'])
def GETempresasd(empresas_Denominacion):
   print(empresas_Denominacion)
   empresasFound=[empresas for empresas in empresas if empresas ['Denominacion']==empresas_Denominacion]
   if (len(empresasFound) > 0):
      return jsonify({"empresas": empresasFound[0]})
   return jsonify({"message":"empresa no encontrada"})

@app.route('/empresas',methods=['POST'])
def POSTempresas():

   new_empresas={
      "Denominacion": resquest.json['Denominacion'],
      "Filtrar departamento": resquest.json['Filtrar departamento'],
   }
   empresas.append(new_empresas)
   return jsonify({"message":"empresa agregado correctamente ","empresas": empresas})

@app.route('/empresas/<string:empresas_Denominacion>',methods=['PUT'])
def PUTempresasd(empresas_Denominacion):
   empresasFound = [empresas for empresas in empresas if empresas['Denominacion'] == empresas_Denominacion]
   if (len(empresasFound) > 0):
      empresasFound[0]['Denominacion']=request.json['Denominacion']
      empresasFound[0]['Filtrar departamento'] = request.json['Filtrar departamento']
      return jsonify({
         "message":"empresa actualizada  correctamente ",
         "empresas": empresasFound[0]
                      })
      return jsonify({"message":"empresa no existe"})

@app.route('/empresas/<string:empresas_Denominacion>',methods=['DELETE'])
def DELETEempresasd(empresas_Denominacion):
   empresasFound = [empresas for empresas in empresas if empresas['Denominacion'] == empresas_Denominacion]
   if (len(empresasFound) > 0):
      empresas.remove(empresasFound)
      return jsonify({"message": "empresa eliminada con exito"})
   return jsonify({"message": "empresa no existe"})

@app.route('/RPA',methods=['POST'])
def POSTRPAempresas():

   return jsonify({"message": "ejecutado robot"})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)
