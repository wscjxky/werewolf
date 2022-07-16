import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import Desktop from  './desktop.vue'

const routes = {
  '/': App,
  '/desktop': Desktop
}
Vue.use(ElementUI)

new Vue({
  el: '#app',
  // render: h => h(App),
  data: {
    currentRoute: window.location.pathname
  },
  computed: {
    ViewComponent () {
      return routes[this.currentRoute] || NotFound
    }
  },
  render (h) { return h(this.ViewComponent) }
})
