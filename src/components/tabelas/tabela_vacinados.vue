<template>
  <div class="grafico graficos">
    <header><h2>{{ title }}</h2></header>
      <table class="table datatable">
        <thead>
            <tr>
                <th>Região</th>
                <th>Estado</th>
                <th>Código Municipio</th>
                <th>Município</th>
                <th>Distrito</th>
                <th>Faixa Etária</th>
                <th>População</th>
                <th>1ª Dose</th>
                <th>2ª Dose</th>
                <th>2ª Dose Única</th>
                <th>Reforço</th>
                <th>Adicional</th>
                <th>2ª Dose Reforço</th>
                <th>%Cobertura 1º Dose</th>
                <th>Não Vacinados 1ª Dose</th>
                <th>%Cobertura 2ª Dose</th>
                <th>Não Vacinados 2ª Dose</th>
                <th>%Cobertura Reforço</th>
                <th>Não Vacinados Reforço</th>
                <th>%Cobertura Adicional</th>
                <th>Não Vacinados Adicional</th>
                <th>%Cobertura 2ª Dose Reforço</th>
                <th>Não Vacinados 2ª Dose Reforço</th>
            </tr>
        </thead>
    </table> 
  </div>
</template>
<script>

import 'jquery/dist/jquery.min.js';
// import 'bootstrap/dist/css/bootstrap.css';
 import 'bulma/css/bulma.css';
import "datatables.net-dt/js/dataTables.dataTables"
import "datatables.net-dt/css/jquery.dataTables.min.css"
import "datatables.net-bm/js/dataTables.bulma.min.js"
import "datatables.net-bm/css/dataTables.bulma.min.css"
import jsZip from 'jszip';
import "datatables.net-buttons-dt";
import 'datatables.net-buttons/js/dataTables.buttons.js'
import 'datatables.net-buttons/js/buttons.html5.js'
import 'datatables.net-buttons/js/buttons.print.js'
//import axios from 'axios';
import $ from 'jquery'; 
window.JSZip = jsZip;

export default {
props: {
    jsonVacinadosMun: Array,
    title: String,
  },
  mounted(){
    var data = [];
    for (var i=0; i<this.jsonVacinadosMun.length; i++){
      data.push([
        this.jsonVacinadosMun[i]["regiao"], this.jsonVacinadosMun[i]["estado"], this.jsonVacinadosMun[i]["codigo_municipio"],
        this.jsonVacinadosMun[i]["municipio"], this.jsonVacinadosMun[i]["distrito"], this.jsonVacinadosMun[i]["faixa_etaria"],
        this.jsonVacinadosMun[i]["populacao"], this.jsonVacinadosMun[i]["1dose"], this.jsonVacinadosMun[i]["2dose"],
        this.jsonVacinadosMun[i]["2Dose_Unica"], this.jsonVacinadosMun[i]["reforco"], this.jsonVacinadosMun[i]["adicional"], this.jsonVacinadosMun[i]["2reforco"],
        this.jsonVacinadosMun[i]["cobertura1dose"], this.jsonVacinadosMun[i]["naovacinados1dose"],
        this.jsonVacinadosMun[i]["cobertura2dose_unica"],this.jsonVacinadosMun[i]["naovacinados2dose_unica"], 
        this.jsonVacinadosMun[i]["coberturareforco"], this.jsonVacinadosMun[i]["naovacinadosreforco"], 
        this.jsonVacinadosMun[i]["coberturaadicional"], this.jsonVacinadosMun[i]["naovacinadosadicional"], 
        this.jsonVacinadosMun[i]["cobertura2reforco"], this.jsonVacinadosMun[i]["naovacinados2reforco"]
      ]);
    }
    $('.datatable').DataTable({
      destroy: true,
      data: data,
      deferRender: true,
      scrollCollapse: true,
      scroller: true,
      dom: 'Bfrtip',
      buttons:[
        {extend: 'csv', className: 'button' },
        {extend: 'excel', className: 'button'}
      ]
    });
  },
}
</script>
