<template>
  <div class="grafico">
    <header>
      <h2>
        {{ title }}
      </h2>
    </header>
    <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
  </div>
</template>

<script>
import { Plotly } from "vue-plotly";

export default {
  props: {
    title: String,
    obitosCovid: Object,
    obitosNCovid: Object,
    dose1: Object,
    dose2: Object,
    dose3: Object,
    dose4: Object,
    uf: String,
  },
  components: {
    Plotly,
  },
  data() {
    return {
     data: [],
      layout: {
        bargap: 0.06,
        margin: {
          t: 20,
          l: 50,
          r: 50,
        },
        paper_bgcolor: this.background,
        plot_bgcolor: this.background,
        barmode: "stack",
        legend: {
          orientation: "h",
          y: -0.20,
        },
        xaxis: {
          zeroline: true,
          showline: false,
        },
        yaxis: {
          zeroline: false, //ssd
          showline: false,
          showgrid: true,
          linewidth: 0,
          title: "Óbitos",
        },
        yaxis2: {
          title: "Vacinação",
          zeroline: false,
          showline: false,
          showgrid: false,
          // position: 0.15,
          linewidth: 0,
          overlaying: "y",
          side: "right",
          tickfont: {
            color: "#000000",
          },
        },
      },
    };
  },
  mounted() {
    let myufs = new Set(Object.values(this.obitosCovid.SG_UF));
    let data = [{
          x: Object.values(this.obitosCovid.SEM_NOT),
          y: Object.values(this.obitosCovid.OBITOS_ESPECIFICADOS),
          type: "bar",
          name: "Óbito por SRAG confirmado para Covid-19",
          opacity: 0.8,
          marker: {
            color: "#7fcdbb",
          },
        },
        {
          x: Object.values(this.obitosNCovid.SEM_NOT),
          y: Object.values(this.obitosNCovid.OBITOS_ESPECIFICADOS),
          type: "bar",
          name: "Óbito por SRAG não especificado",
          opacity: 0.8,
          marker: {
            color: "#c7e9b4",
          },
        },
        {
          x: Object.values(this.dose1.SEM_NOT),
          y: Object.values(this.dose1.VACINA_1DOSE),
          type: "scatter",
          name: "Vacinação 1ª dose",
          marker: {
            color: "#41b6c4",
          },
          yaxis: "y2",
        },
        {
          x: Object.values(this.dose2.SEM_NOT),
          y: Object.values(this.dose2.VACINA_COMPLETA),
          type: "scatter",
          name: "Vacinação 2ª dose",
          marker: {
            color: "#2c7fb8",
          },
          yaxis: "y2",
        },
        {
          x: Object.values(this.dose3.SEM_NOT),
          y: Object.values(this.dose3.VACINA_REFORCO),
          type: "scatter",
          name: "Vacinação dose de reforço",
          marker: {
            color: "#253494",
          },
          yaxis: "y2",
        },
        {
          x: Object.values(this.dose4.SEM_NOT),
          y: Object.values(this.dose4.VACINA_2REFORCO),
          type: "scatter",
          name: "Vacinação 2ª dose de reforço",
          marker: {
            color: "#080b20",
          },
          yaxis: "y2",
        }];
    myufs.forEach((uf) => {
      if (typeof this.uf !== "undefined") {
        if (this.uf !== uf) {
          return false;
        }
      }
      
      // todas as chaves da ufs
      let keysOC = Object.keys(this.obitosCovid.SG_UF).filter(
        (chave) => this.obitosCovid.SG_UF[chave] === uf
      );
      let ocX = keysOC.map((key) => {
        return this.obitosCovid.SEM_NOT[key];
      });
      let ocY = keysOC.map((key) => {
        return this.obitosCovid.OBITOS_ESPECIFICADOS[key];
      });
      let keysONC = Object.keys(this.obitosNCovid.SG_UF).filter(
        (chave) => this.obitosNCovid.SG_UF[chave] === uf
      );
      let oncX = keysONC.map((key) => {
        return this.obitosNCovid.SEM_NOT[key];
      });
      let oncY = keysONC.map((key) => {
        return this.obitosNCovid.OBITOS_ESPECIFICADOS[key];
      });
      let keysD1 = Object.keys(this.dose1.SG_UF).filter(
        (chave) => this.dose1.SG_UF[chave] === uf
      );
      let d1X = keysD1.map((key) => {
        return this.dose1.SEM_NOT[key];
      });
      let d1Y = keysD1.map((key) => {
        return this.dose1.VACINA_1DOSE[key];
      });
      let keysD2 = Object.keys(this.dose2.SG_UF).filter(
        (chave) => this.dose2.SG_UF[chave] === uf
      );
      let d2X = keysD2.map((key) => {
        return this.dose2.SEM_NOT[key];
      });
      let d2Y = keysD2.map((key) => {
        return this.dose2.VACINA_COMPLETA[key];
      });
      let keysD3 = Object.keys(this.dose3.SG_UF).filter(
        (chave) => this.dose3.SG_UF[chave] === uf
      );
      let d3X = keysD3.map((key) => {
        return this.dose3.SEM_NOT[key];
      });
      let d3Y = keysD3.map((key) => {
        return this.dose3.VACINA_REFORCO[key];
      });
      let keysD4 = Object.keys(this.dose4.SG_UF).filter(
        (chave) => this.dose4.SG_UF[chave] === uf
      );
      let d4X = keysD4.map((key) => {
        return this.dose4.SEM_NOT[key];
      });
      let d4Y = keysD4.map((key) => {
        return this.dose4.VACINA_2REFORCO[key];
      });
      
      data = [];
      
      data.push({
        x: ocX,
        y: ocY,
        type: "bar",
        name: "Óbito por SRAG confirmado para Covid-19 por data de início de sintomas",
        opacity: 0.8,
        marker: {
          color: "#7fcdbb",
        },
      },
      {
        x: oncX,
        y: oncY,
        type: "bar",
        name: "Óbito por SRAG não especificado por data de início de sintomas",
        opacity: 0.8,
        marker: {
          color: "#c7e9b4",
        },
      },
      {
        x: d1X,
        y: d1Y,
        type: "scatter",
        name: "Vacinação 1ª dose",
        marker: {
          color: "#41b6c4",
        },
        yaxis: "y2",
      },
      {
        x: d2X,
        y: d2Y,
        type: "scatter",
        name: "Vacinação 2ª dose",
        marker: {
          color: "#2c7fb8",
        },
        yaxis: "y2",
      },
      {
        x: d3X,
        y: d3Y,
        type: "scatter",
        name: "Vacinação dose de reforço",
        marker: {
          color: "#253494",
        },
        yaxis: "y2",
      },
      {
        x: d4X,
        y: d4Y,
        type: "scatter",
        name: "Vacinação 2ª dose de reforço",
        marker: {
          color: "#080b20",
        },
        yaxis: "y2",
      });
    });
    this.data = data;
  },
  methods: {},
};
</script>
