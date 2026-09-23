<template>
  <div>
    <l-map
      class="componente-mapa"
      v-if="tipo === 'uti'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 450px;"
      :options="utiOptions"
    >
      <l-choropleth-layer
        :data="dadosPorEstado"
        titleKey="nome_var_estado"
        idKey="id_int_estado"
        :value="uti.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="brasilGeojson"
        :colorScale="uti.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="uti.tituloInfo"
            placeholder=""
          />
          <l-reference-chart
            :title="some_var"
            :colorScale="uti.colorScale"
            :min="0"
            :max="100"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>

    <l-map
      class="componente-mapa"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 450px;"
      :options="clinicoOptions"
    >
      <l-choropleth-layer
        :data="dadosPorEstado"
        titleKey="nome_var_estado"
        idKey="id_int_estado"
        :value="clinico.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="brasilGeojson"
        :colorScale="clinico.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="clinico.tituloInfo"
            placeholder=""
          />
          <l-reference-chart
            :title="some_var"
            :colorScale="clinico.colorScale"
            :min="0"
            :max="100"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>
  </div>
</template>

<script>
import { InfoControl, ReferenceChart, ChoroplethLayer } from "vue-choropleth";
import brasilGeojson from "../../data/brasil_estados.json";
import { dadosPorEstado } from "../../data/ocupacao/dados-por-estado-ocupacao";
import { LMap } from "vue2-leaflet";

export default {
  name: "mapa-brasil",
  props: {
    tipo: String,
    indice: String,
  },
  components: {
    LMap,
    "l-info-control": InfoControl,
    "l-reference-chart": ReferenceChart,
    "l-choropleth-layer": ChoroplethLayer,
  },
  data() {
    return {
      dadosPorEstado,
      brasilGeojson,
      some_var: "",
      uti: {
        tituloInfo: "Uti",
        tituloReferencia: "Semana: ",
        colorScale: ["7bad56", "ffa500", "FF0000"],
        value: {
          key: "quantidade_int_uti",
          metric: "%",
        },
      },
      clinico: {
        tituloInfo: "Clinico",
        tituloReferencia: "Semana: ",
        colorScale: ["7bad56", "ffa500", "FF0000"],
        colorValuePath: 'quantidade_int_clinico',
        colorMapping: [
            {
                from: 0, to: 25, color: 'rgb(153,174,214)'
            },
            {
                from: 25, to: 50, color: 'rgb(115,143,199)'
            },
            {
                from: 50, to: 75, color: 'rgb(77,112,184)'
            },
            {
                from: 75, to: 100, color: 'rgb(38,82,168)'
            }
        ],
        value: {
          key: "quantidade_int_clinico",
          metric: " %",
        },
      },
      utiOptions: {
        name: "utiMap",
        attributionControl: false,
        inertia: true,
        doubleClickZoom: false,
        closePopupOnClick: false,
        dragging: false,
        zoomSnap: false,
        zoomDelta: false,
        trackResize: false,
        touchZoom: false,
        scrollWheelZoom: false,
        zoomControl: false,
      },
      clinicoOptions: {
        name: "clinicoMap",
        attributionControl: false,
        inertia: true,
        doubleClickZoom: false,
        closePopupOnClick: false,
        dragging: false,
        zoomSnap: false,
        zoomDelta: false,
        trackResize: false,
        touchZoom: false,
        scrollWheelZoom: false,
        zoomControl: false,
      },
      currentStrokeColor: "ddd",
      zoom: screen.width <= 460 ? 2.5 : 2.8,
    };
  },
  mounted() {
    let mySemanas = String(this.dadosPorEstado[0]["semana"]);
    this.some_var = "Semana: " + mySemanas;
  },
  beforeMount () {
    this.dadosPorEstado = this.dadosPorEstado[0][parseInt(this.indice)];
  },
  methods: {
  },
};
</script>

<style>
@import "../../../node_modules/leaflet/dist/leaflet.css";
.leaflet-container {
  background: #fff;
}
.leaflet-bottom {
  bottom: 30%;
  left: 10%;
}
.leaflet-top.leaflet-right {
  right: 32px;
}
.leaflet-top .info .gradient {
  width: 100%;
}
.leaflet-top .info {
  box-shadow: none;
}
.leaflet-bottom .info {
  box-shadow: none;
  background: transparent;
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100px;
  right: 0;
  text-align: left;
  max-width: 300px;
  min-height: 80px;
}

.leaflet-bottom .info h4 {
  margin: 0 0 16px;
  color: #777;
  font-size: 1rem;
  text-transform: uppercase;
}
.leaflet-bottom .info b {
  font-size: 1.01rem;
}

.leaflet-top .info .gradient .domain-min,
.leaflet-top .info .gradient .domain-med,
.leaflet-top .info .gradient .domain-max {
  font-size: 12px;
  bottom: -4px;
  font-weight: bold;
}
.info .leaflet-control{
  padding:2px 4px;
  font:14px/16px sans-serif;
  background:#fff;
  background:hsla(0,0%,100%,.8);
  box-shadow:0 0 15px rgba(0,0,0,.2);
  border-radius:5px
}
.info h4{
  margin:0 0 5px;
  color:#777
}
</style>
