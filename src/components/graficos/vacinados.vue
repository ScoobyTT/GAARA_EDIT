<template>
  <div class="grafico">
    <header>
      <h2>
        {{ title }}
      </h2>
    </header>
    <!-- <div class="tipo">
      <a href="#" @click.prevent="ordenar('primera')">1ª dose</a>
      <a href="#" @click.prevent="ordenar('imunizados')">2ª dose</a>
      <a href="#" @click.prevent="ordenar('reforco')">Reforço</a>
    </div> -->
    <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
  </div>
</template>

<script>
import { Plotly } from "vue-plotly";
export default {
  props: {
    title: String,
    json: Array,
  },
  components: {
    Plotly,
  },
  data() {
    return {
      data: [
        {
          x: this.json.map((v) => {
            return v.primeira;
          }),
          y: this.json.map((v) => {
            return v.state;
          }),
          type: "bar",
          name: "% da população vacinada na 1ª dose",
          text: this.json.map((v) => v.primeira + "% " + v.id),
          hoverinfo: "none",
          textposition: "auto",
          orientation: "h",
          opacity: 0.7,
          marker: {
            color: "#41b6c4",
          },
        },
        {
          x: this.json.map((v) => {
            return v.imunizados;
          }),
          y: this.json.map((v) => {
            return v.state;
          }),
          type: "bar",
          name: "% da população totalmente imunizada",
          text: this.json.map((v) => {
            return v.imunizados + "% " + v.id;
          }),
          orientation: "h",
          hoverinfo: "none",
          textposition: "auto",

          opacity: 0.7,
          marker: {
            color: "#2c7fb8",
          },
        },
        {
          x: this.json.map((v) => {
            return v.reforco;
          }),
          y: this.json.map((v) => {
            return v.state;
          }),
          type: "bar",
          name: "% da população vacinada com dose de reforço",
          text: this.json.map((v) => {
            return v.reforco + "% " + v.id;
          }),
          orientation: "h",
          textposition: "auto",
          hoverinfo: "none",
          opacity: 0.7,
          marker: {
            color: "#253494",
          },
        },
      ],
      layout: {
        margin: {
          t: 0,
          l: 140,
          r: 180,
          b: 180,
        },
        height: 800,
        barmode: "overlay",
        bargap: 0.04,
        legend: {
          orientation: "h",
        },
        yaxis: {
          overlaying: "x",
        },
        xaxis: {
          range: [0, 100],
          tickvals: [0, 25, 50, 75, 100],
          ticktext: [0, 25, 50, 75, 100],
          title: "% da População",
        },
      },
    };
  },

  created() {
    this.sort();
  },

  methods: {
    ordenar(ordem) {
      console.log(ordem);
      this.json = this.json.sort((a, b) => a[ordem] - b[ordem]);
    },
    sort() {
      this.json = this.json.sort((a, b) => a.id - b.id);
      
    },
  },
};
</script>

<style></style>
