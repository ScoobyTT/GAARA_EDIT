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
    background: String,
    covid: Object,
    uti: Object,
    nuti: Object,
    ufs: String,
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
          title: "Hospitalizações",
        },
        yaxis2: {
          title: "Casos de Covid-19",
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
    let myufs = new Set(Object.values(this.uti.SG_UF));
    let data = [{
          x: Object.values(this.uti.SEM_NOT),
          y: Object.values(this.uti.CASOS_SRAG),
          type: "bar",
          name: "Hospitalizações em UTI",
          opacity: 0.8,
          marker: {
            color: "#7fcdbb",
          },
        },
        {
          x: Object.values(this.uti.SEM_NOT),
          y: Object.values(this.nuti.CASOS_SRAG),
          type: "bar",
          name: "Hospitalizações em NÃO UTI",
          opacity: 0.8,
          marker: {
            color: "#c7e9b4",
          },
        },
        {
          x: Object.values(this.uti.SEM_NOT),
          y: Object.values(this.covid.CASOS_COVID),
          type: "scatter",
          name: "Casos COVID-19 reportados",
          marker: {
            color: "#253494",
          },
          yaxis: "y2",
        }];
    myufs.forEach((uf) => {
      if (typeof this.ufs !== "undefined") {
        if (this.ufs !== uf) {
          return false;
        }
      }
      // todas as chaves da ufs
      let keysU = Object.keys(this.uti.SG_UF).filter(
        (chave) => this.uti.SG_UF[chave] === uf
      );
      
      let keysN = Object.keys(this.nuti.SG_UF).filter(
        (chave) => this.nuti.SG_UF[chave] === uf
      );
      
      let keysC = Object.keys(this.covid.SG_UF).filter(
        (chave) => this.covid.SG_UF[chave] === uf
      );

      let utiX = keysU.map((key) => {
        return this.uti.SEM_NOT[key];
      });

      let utiY = keysU.map((key) => {
        return this.uti.CASOS_SRAG[key];
      });
      
      let nutiX = keysN.map((key) => {
        return this.nuti.SEM_NOT[key];
      });

      let nutiY = keysN.map((key) => {
        return this.nuti.CASOS_SRAG[key];
      });
      
      let covidX = keysC.map((key) => {
        return this.covid.SEM_NOT[key];
      });

      let covidY = keysC.map((key) => {
        return this.covid.CASOS_COVID[key];
      });
      
      data = [];
      
      data.push({
        x: utiX,
        y: utiY,
        type: "bar",
        name: "Hospitalizações em UTI",
        opacity: 0.8,
        marker: {
          color: "#7fcdbb",
        },
      },
      {
        x: nutiX,
        y: nutiY,
        type: "bar",
        name: "Hospitalizações em NÃO UTI",
        opacity: 0.8,
        marker: {
          color: "#c7e9b4",
        },
      },
      {
        x: covidX,
        y: covidY,
        type: "scatter",
        name: "Casos COVID-19 reportados",
        opacity: 0.6,
        marker: {
          color: "#253494",
        },
        yaxis: "y2",
      });
    });
    this.data = data;
  },
  methods: {},
};
</script>

