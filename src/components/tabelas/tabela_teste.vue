<template>
  <div class="grafico">
    <h2>{{ title }}</h2>
      <table class="table" id="datatable">
        <thead>
            <tr>
                <th>Região</th>
                <th>Estado</th>
                <th>Código Municipio</th>
                <th>Município</th>
                <th>Faixa Etária</th>
                <th>População</th>
                <th>1ª Dose</th>
                <th>2ª Dose</th>
                <th>Reforço</th>
                <th>%Cobertura 1º Dose</th>
                <th>Não Vacinados 1ª Dose</th>
                <th>%Cobertura 2ª Dose</th>
                <th>Não Vacinados 2ª Dose</th>
                <th>%Cobertura Reforço</th>
                <th>Não Vacinados Reforço</th>
            </tr>
        </thead>
        <tfoot>
            <tr>
                <th>Região</th>
                <th>Estado</th>
                <th>Código Municipio</th>
                <th>Município</th>
                <th>Faixa Etária</th>
                <th>População</th>
                <th>1ª Dose</th>
                <th>2ª Dose</th>
                <th>Reforço</th>
                <th>%Cobertura 1º Dose</th>
                <th>Não Vacinados 1ª Dose</th>
                <th>%Cobertura 2ª Dose</th>
                <th>Não Vacinados 2ª Dose</th>
                <th>%Cobertura Reforço</th>
                <th>Não Vacinados Reforço</th>
            </tr>
        </tfoot>
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
import json from "../../data/tabela_vacina.json"
//import axios from 'axios';
import $ from 'jquery'; 
window.JSZip = jsZip;

export default {
props: {
    title: String,
  },
  mounted(){
      var data = json;
      $('#datatable').DataTable( {
        data: data,
        "columns": [
            { "data": "regiao" },
            { "data": "estado" },
            { "data": "codigo_municipio" },
            { "data": "municipio" },
            { "data": "faixa_etaria" },
            { "data": "populacao" },
            { "data": "1dose" },
            { "data": "2dose" },
            { "data": "reforco" },
            { "data": "cobertura1dose" },
            { "data": "naovacinados1dose" },
            { "data": "cobertura2dose" },
            { "data": "naovacinados2dose" },
            { "data": "coberturareforco" },
            { "data": "naovacinadosreforco" }
        ],
        dom: 'Bfrtip',
        buttons: [
            { extend: 'csv', className: 'button' },
            { extend: 'excel', className: 'button' }
        ],
        order: [[ 1, "asc" ]]
    });
  },
}
</script>