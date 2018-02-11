<template>
<v-app light>
  <router-view></router-view>
</v-app>
</template>

<script>
require('vuetify/dist/vuetify.css')
require('font-awesome/css/font-awesome.css')
export default {
  name: 'app',
  data () {
    return {
      drawer: true
    }
  }
}
</script>

<style>

</style>
