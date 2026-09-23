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
    json: Array,
  },
  components: {
    Plotly,
  },
  data() {
    return {
      data: [
        /**{
          x: this.json.map((pop) => {
            return -pop.male.population;
          }),
          y: this.json.map((l) => {
            return l.labels;
          }),
          type: "bar",
          name: "População - Masculino",
          orientation: "h",
          marker: {
            color: "#a8e3f5",
          },
        },
        {
          x: this.json.map((pop) => {
            return pop.female.population;
          }),
          y: this.json.map((l) => {
            return l.labels;
          }),
          type: "bar",
          name: "População - Feminino",
          orientation: "h",
          // text: [-600, -623, -653, -650, -670, -578, -541, -411, -322, -230],
          // textposition: "auto",
          // hoverinfo: "none",
          marker: {
            color: "#f7e8ad",
          },
        },/**/
        {
          x: this.json.map((dose) => {
            return -dose.male.first;
          }),
          y: this.json.map((l) => {
            return l.labels;
          }),
          type: "bar",
          name: "1ª dose (MASC)",
          orientation: "h",
          text: this.json.map((h) => { return h.male.first + "%"; }),
          textposition: "outside",
          hoverinfo: "none",
          marker: {
            color: "#08BAFA",
          },
        },
        {
          x: this.json.map((dose) => {
            return -dose.male.second;
          }),
          y: this.json.map((l) => {
            return l.labels;
          }),
          type: "bar",
          name: "2ª dose (MASC)",
          orientation: "h",
          text: this.json.map((h) => { return h.male.second + "%"; }),
          textposition: "auto",
          hoverinfo: "none",
          marker: {
            color: "#1874CD",
          },
        },
        {
          x: this.json.map((dose) => {
            return -dose.male.third;
          }),
          y: this.json.map((l) => {
            return l.labels;
          }),
          type: "bar",
          name: "Reforço (MASC)",
          orientation: "h",
          text: this.json.map((h) => { return h.male.third + "%"; }),
          textposition: "auto",
          hoverinfo: "none",
          marker: {
            color: "#03045e",
          },
        },
        {
          x: this.json.map((dose) => {
            return dose.female.first;
          }),
          y: this.json.map((l) => {
            return l.labels;
          }),
          type: "bar",
          name: "1ª dose (FEM)",
          orientation: "h",
          text: this.json.map((h) => { return h.female.first + "%"; }),
          textposition: "outside",
          hoverinfo: "none",
          marker: {
            color: "#FBAD29",
          },
        },
        {
          x: this.json.map((dose) => {
            return dose.female.second;
          }),
          y: this.json.map((l) => {
            return l.labels;
          }),
          type: "bar",
          name: "2ª dose (FEM)",
          orientation: "h",
          text: this.json.map((h) => { return h.female.second + "%"; }),
          textposition: "auto",
          hoverinfo: "none",
          marker: {
            color: "#FF7B34",
          },
        },
        {
          x: this.json.map((dose) => {
            return dose.female.third;
          }),
          y: this.json.map((l) => {
            return l.labels;
          }),
          type: "bar",
          name: "Reforço (FEM)",
          orientation: "h",
          text: this.json.map((h) => { return h.female.third + "%"; }),
          textposition: "auto",
          hoverinfo: "none",
          marker: {
            color: "#CC661C",
          },
        },
      ],
      layout: {
        // showlegend: false,
        // title: {
        //   text: this.title.toUpperCase(),
        //   font: {
        //     size: 16,
        //   },
        //   align: "left",
        // },
        margin: {
          t: 40,
          l: 100,
          r: 50,
          b: 0,
        },
        text: "*SE = Semana Epidemiológica",
        barmode: "overlay",
        bargap: 0.1,
        legend: {
          orientation: "h",
          // x: 0,
          // xanchor: "right",
          // y: 1.02,
          // yanchor: "bottom",
        },
        yaxis: {
          title: "",
          zeroline: false,
        },
        xaxis: {
          range: [-120, 120],
          tickvals: [
            -100,
            -75,
            -50,
            -25,
            0,
            25,
            50,
            75,
            100,
          ],
          ticktext: [
            "100%",
            "75%",
            "50%",
            "25%",
            0,
            "25%",
            "50%",
            "75%",
            "100%",
          ],
          // title: this.title,
          // tickangle: -45,
        },
        // annotations: [
        //   {
        //     x: 2,
        //     y: 5,
        //     xref: "x",
        //     yref: "y",
        //     text: "Annotation Text",
        //     showarrow: true,
        //     arrowhead: 7,
        //     ax: 20,
        //     ay: 40,
        //   },
        // ],
      },
    };
  },

  methods: {},
};
</script>

<style></style>
