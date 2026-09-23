<template>
  <div class="grafico graficos">
    <header><h2>{{ title }}</h2></header>
      <table class="table" id="datatableV">
        <thead>
            <tr>
                <th>Estado</th>
                <th>Dsei</th>
                <th>População de 05 a 11 anos</th>
                <th>1ª dose de 05 a 11 anos</th>
                <th>Cobertura da 1ª dose de 05 a 11 anos</th>
                <th>2ª dose de 05 a 11 anos</th>
                <th>Cobertura da 2ª dose de 05 a 11 anos</th>
                <th>População de 12 a 17 anos</th>
                <th>1ª dose de 12 a 17 anos</th>
                <th>Cobertura da 1ª dose de 12 a 17 anos</th>
                <th>2ª dose de 12 a 17 anos</th>
                <th>Cobertura da 2ª dose de 12 a 17 anos</th>
                <th>População de 18 anos ou mais</th>
                <th>1ª dose de 18 anos ou mais</th>
                <th>Cobertura da 1ª dose de 18 anos ou mais</th>
                <th>2ª dose de 18 anos ou mais</th>
                <th>Cobertura da 2ª dose de 18 anos ou mais</th>
                <th>Reforço e/ou Adicional 18 anos ou mais</th>
                <th>Cobertura do Reforço e/ou Adicional de 18 anos ou mais</th>
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
    jsonIndigenasVac: Array,
    title: String,
  },
  mounted(){
    var dataV = [];
    for (var i=0; i<this.jsonIndigenasVac.length; i++){
      dataV.push([ this.jsonIndigenasVac[i]["Unidade_Federada"], this.jsonIndigenasVac[i]["Dsei"],
        this.jsonIndigenasVac[i]["Populacao_05_a_11_anos"], this.jsonIndigenasVac[i]["05_a_11_1dose"], this.jsonIndigenasVac[i]["Cobertura_05_a_11_1dose"],
        this.jsonIndigenasVac[i]["05_a_11_2dose"], this.jsonIndigenasVac[i]["Cobertura_05_a_11_2dose"], this.jsonIndigenasVac[i]["Populacao_12_a_17_anos"],
        this.jsonIndigenasVac[i]["12_a_17_1dose"], this.jsonIndigenasVac[i]["Cobertura_12_a_17_1dose"], this.jsonIndigenasVac[i]["12_a_17_2dose"],
        this.jsonIndigenasVac[i]["Cobertura_12_a_17_2dose"], this.jsonIndigenasVac[i]["Populacao_18_anos_ou_mais"], this.jsonIndigenasVac[i]["18_anos_ou_mais_1dose"],
        this.jsonIndigenasVac[i]["Cobertura_18_anos_ou_mais_1dose"], this.jsonIndigenasVac[i]["18_anos_ou_mais_2dose"], this.jsonIndigenasVac[i]["Cobertura_18_anos_ou_mais_2dose"],
        this.jsonIndigenasVac[i]["18_anos_ou_mais_Reforco_mais_Adicional"], this.jsonIndigenasVac[i]["Cobertura_18_anos_ou_mais_Reforco_mais_dicional"] ]);
    }
    $('#datatableV').DataTable({
      destroy: true,
      data: dataV,
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
