<template>
  <div class="grafico graficos">
    <header><h2>{{ title }}</h2></header>
      <table class="table datatable">
        <thead>
            <tr>
                <th>Região</th>
                <th>Estado</th>
                <th>Data</th>
                <th>Ocupação</th>
            </tr>
        </thead>
        <tfoot>
            <tr>
                <th>Região</th>
                <th>Estado</th>
                <th>Data</th>
                <th>Ocupação</th>
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
    jsonOcupacao: Array,
    title: String,
  },
  mounted(){
    var data = [];
    for (var i=0; i<this.jsonOcupacao.length; i++){
      data.push([ this.jsonOcupacao[i]["region"], this.jsonOcupacao[i]["state"], this.jsonOcupacao[i]["date"], this.jsonOcupacao[i]["beds"] ]);
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
      ],
      order: [[2, "desc"]]
    });
  },
}
</script>
