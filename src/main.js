import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueMeta from 'vue-meta'
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';
import 'vue2-datepicker/locale/pt-br';
// import VueDragscroll from 'vue-dragscroll';

// Vue.use(VueDragscroll);
Vue.use(VueMeta);
Vue.use(DatePicker);
Vue.config.productionTip = false;



new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
