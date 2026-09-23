<template>
  <div>
    <l-map
      class="componente-mapa"
      v-if="tipo === 'Dose1'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="Dose1Options"
    >
      <l-choropleth-layer
        :data="dadosPorDsei"
        titleKey="Dsei"
        idKey="id_int_dsei"
        :value="Dose1.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="DseiGeojson"
        :colorScale="Dose1.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="Dose1.tituloInfo"
            placeholder="Passe o mouse sobre a DSEI para visualizar os dados"
          />
          <l-reference-chart
            :title="Dose1.tituloReferencia"
            :colorScale="Dose1.colorScale"
            :min="0"
            :max="props.max"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>
    
    <l-map
      class="componente-mapa"
      v-if="tipo === 'Dose2'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="Dose2Options"
    >
      <l-choropleth-layer
        :data="dadosPorDsei"
        titleKey="Dsei"
        idKey="id_int_dsei"
        :value="Dose2.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="DseiGeojson"
        :colorScale="Dose2.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="Dose2.tituloInfo"
            placeholder="Passe o mouse sobre a DSEI para visualizar os dados"
          />
          <l-reference-chart
            :title="Dose2.tituloReferencia"
            :colorScale="Dose2.colorScale"
            :min="0"
            :max="props.max"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>
    
    <l-map
      class="componente-mapa"
      v-if="tipo === 'Reforco'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="ReforcoOptions"
    >
      <l-choropleth-layer
        :data="dadosPorDsei"
        titleKey="Dsei"
        idKey="id_int_dsei"
        :value="Reforco.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="DseiGeojson"
        :colorScale="Reforco.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="Reforco.tituloInfo"
            placeholder="Passe o mouse sobre a DSEI para visualizar os dados"
          />
          <l-reference-chart
            :title="Reforco.tituloReferencia"
            :colorScale="Reforco.colorScale"
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
import { ReferenceChart, InfoControl, ChoroplethLayer } from "vue-choropleth";
import DseiGeojson from "../../data/indigena/limite_dsei.json";
import { dadosPorDsei } from "../../data/indigena/dados-vacina-por-dsei.js";
import { LMap } from "vue2-leaflet";

export default {
  name: "mapa",
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
      dadosPorDsei,
      DseiGeojson,
      Dose1: {
        tituloInfo: "1º dose",
        tituloReferencia: "1º DOSE POR DSEI",
        colorScale: ["8dd3db", "66c4cf", "41b6c4", "34919c", "276d75"],
        value: {
          key: "Cobertura_1dose",
          metric: "%",
        },
      },
      Dose2: {
        tituloInfo: "2º dose",
        tituloReferencia: "2º DOSE POR DSEI",
        colorScale: ["80b2d4", "5698c6", "2c7fb8", "236593", "1a4c6e"],
        value: {
          key: "Cobertura_2dose",
          metric: "%",
        },
      },
      Reforco: {
        tituloInfo: "Dose de Reforço/Adicional",
        tituloReferencia: "DOSE DE REFORÇO/ADICIONAL POR DSEI",
        colorScale: ["7c85be", "505ca9", "253494", "1d2976", "161f58"],
        value: {
          key: "Cobertura_Ref_Adc",
          metric: "%",
        },
      },
      Dose1Options: {
        name: "Dose1Map",
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
      Dose2Options: {
        name: "Dose2Map",
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
      ReforcoOptions: {
        name: "ReforcoMap",
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
