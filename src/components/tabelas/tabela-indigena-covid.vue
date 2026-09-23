<template>
  <div class="grafico graficos">
    <header><h2>{{ title }}</h2></header>
      <table class="table" id="datatableC">
        <thead>
            <tr>
                <th>Dsei</th>
                <th>Polo Base</th>
                <th>Faixa Etária</th>
                <th>Semana Epidemiológica</th>
                <th>Número de Casos</th>
                <th>Número de Óbitos</th>
            </tr>
        </thead>
        <tfoot>
            <tr>
                <th>Dsei</th>
                <th>Polo Base</th>
                <th>Faixa Etária</th>
                <th>Semana Epidemiológica</th>
                <th>Número de Casos</th>
                <th>Número de Óbitos</th>
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
//import axios from 'axios';
import $ from 'jquery'; 
window.JSZip = jsZip;

export default {
  props: {
    jsonIndigenasCasos: Array,
    title: String,
  },
  mounted(){
    var dataC = [];
    for (var i=0; i<this.jsonIndigenasCasos.length; i++){
      dataC.push([ this.jsonIndigenasCasos[i]["Dsei"], this.jsonIndigenasCasos[i]["Polo_Base"], this.jsonIndigenasCasos[i]["Faixa_Etaria"], 
        this.jsonIndigenasCasos[i]["Semana_Epi"], this.jsonIndigenasCasos[i]["confirmado"], this.jsonIndigenasCasos[i]["obitos"] ]);
    }
    $('#datatableC').DataTable({
      destroy: true,
      data: dataC,
      deferRender: true,
      scrollCollapse: true,
      scroller: true,
      dom: 'Bfrtip',
      buttons:[
        {extend: 'csv', className: 'button' },
        {extend: 'excel', className: 'button'}
      ],
      order: [[2, "desc"]]
    });
  },
}
</script>
