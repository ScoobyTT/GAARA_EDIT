<template>
  <div>
    <l-map
      class="componente-mapa"
      v-if="tipo === 'covid'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="covidOptions"
    >
      <l-choropleth-layer
        :data="dadosPorEstado"
        titleKey="nome_var_estado"
        idKey="id_int_estado"
        :value="covid.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="brasilGeojson"
        :colorScale="covid.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="covid.tituloInfo"
            placeholder="Passe o mouse sobre a UF para visualizar os dados"
          />
          <l-reference-chart
            :title="covid.tituloReferencia"
            :colorScale="covid.colorScale"
            :min="0"
            :max="props.max"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>

    <l-map
      class="componente-mapa"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="sragOptions"
    >
      <l-choropleth-layer
        :data="dadosPorEstado"
        titleKey="nome_var_estado"
        idKey="id_int_estado"
        :value="srag.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="brasilGeojson"
        :colorScale="srag.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="srag.tituloInfo"
            placeholder="Passe o mouse sobre a UF para visualizar os dados"
          />
          <l-reference-chart
            :title="srag.tituloReferencia"
            :colorScale="srag.colorScale"
            :min="0"
            :max="props.max"
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
import { dadosPorEstado } from "../../data/home/dados-por-estado";
import { LMap } from "vue2-leaflet";
export default {
  name: "mapa-brasil",
  props: {
    tipo: String,
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
      covid: {
        tituloInfo: "Casos COVID-19",
        tituloReferencia: "CASOS DE COVID-19 POR ESTADO",
        colorScale: ["00ace3", "008ebc", "007092"],
        value: {
          key: "quantidade_int_covid",
          metric: " casos",
        },
      },
      srag: {
        tituloInfo: "Casos SRAG",
        tituloReferencia: "CASOS DE SRAG POR ESTADO",
        colorScale: ["ff9058", "fb7f41", "ff671b"],
        value: {
          key: "quantidade_int_srag",
          metric: " casos",
        },
      },
      covidOptions: {
        name: "covidMap",
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
      sragOptions: {
        name: "sragMap",
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
      zoom: screen.width <= 760 ? 3.5 : 4.5,
    };
  },
  methods: {},
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
  width: 500px;
  right: 0;
  text-align: left;
  max-width: 300px;
  min-height: 80px;
}
.leaflet-bottom .info h4 {
  margin: 0 0 16px;
  color: #777;
  font-size: 1.8rem;
  text-transform: uppercase;
}
.leaflet-bottom .info b {
  font-size: 1.01rem;
}
.leaflet-top .info .gradient .domain-min,
.leaflet-top .info .gradient .domain-med,
.leaflet-top .info .gradient .domain-max {
  font-size: 16px;
  bottom: -4px;
  font-weight: bold;
}
</style>