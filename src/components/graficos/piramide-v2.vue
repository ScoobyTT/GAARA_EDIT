<template>
  <div class="grafico">
    <header>
      <h2>{{ title }}</h2>
    </header>
    <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
  </div>
</template>

<script>
import { Plotly } from "vue-plotly";
export default {
  props: {
    title: String,
    hospitalizados: Array,
  },
  components: {
    Plotly,
  },
  data() {
    return {
      masculino: [600, 623, 653, 650, 670, 578, 541, 360, 312, 170],
      data: [
        {
          x: this.hospitalizados.map((h) => {
            return -h.male.hospitalizations;
          }),
          y: this.hospitalizados.map((h) => {
            return h.labels;
          }),
          type: "bar",
          name: "Hospitalizados por SRAG - Masculino",
          hoverinfo: "none",
          orientation: "h",
          marker: {
            color: "#08BAFA",
          },
        },
        {
          x: this.hospitalizados.map((h) => {
            return h.female.hospitalizations;
          }),
          y: this.hospitalizados.map((h) => {
            return h.labels;
          }),
          type: "bar",
          name: "Hospitalizados por SRAG - Feminino",
          orientation: "h",
          hoverinfo: "none",
          marker: {
            color: "#FF7B34",
          },
        },
        {
          x: this.hospitalizados.map((h) => {
            return -h.male.deaths;
          }),
          y: this.hospitalizados.map((h) => {
            return h.labels;
          }),
          type: "bar",
          name: "Óbitos por SRAG (Masculino)",
          orientation: "h",
          text: this.hospitalizados.map((h) => {
            return Number(h.male.deaths).toLocaleString('pt-BR');
          }),
          textposition: "auto",
          hoverinfo: "none",
          marker: {
            color: "#1874CD",
          },
        },
        {
          x: this.hospitalizados.map((h) => {
            return h.female.deaths;
          }),
          y: this.hospitalizados.map((h) => {
            return h.labels;
          }),
          type: "bar",
          name: "Óbitos por SRAG (Feminino)",
          orientation: "h",
          text: this.hospitalizados.map((h) => {
            return Number(h.female.deaths).toLocaleString('pt-BR');
          }),
          textposition: "auto",
          hoverinfo: "none",
          marker: {
            color: "#CC661C",
          },
        },
      ],
      layout: {
        barmode: "overlay",
        bargap: 0.06,
        legend: {
          orientation: "h",
        },
        margin: {
          t: 0,
          l: 100,
          r: 0,
          b: 90,
        },
        yaxis: {
          // title: "Faixa Etária",
          zeroline: false,
        },
        xaxis: {
          range: [-360000, 360000],
          tickvals: [
            -340000,
            -255000,
            -170000,
            -85000,
            0,
            85000,
            170000,
            255000,
            340000,
          ],
          ticktext: [
            "340K",
            "255K",
            "170K",
            "85K",
            0,
            "85K",
            "170K",
            "255K",
            "340K",
          ],
          // tickvals: [-1000, -700, -300, 0, 300, 700, 1000],
          // ticktext: [1000, 700, 300, 0, 300, 700, 1000],
        },
      },
    };
  },
};
</script>

<style></style>
