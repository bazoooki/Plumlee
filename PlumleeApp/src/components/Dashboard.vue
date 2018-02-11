<template>
  <v-layout id="dashboard" row wrap fill-height >
    <v-flex xs4>wooho </v-flex>
    <v-flex xs8>      
      <players-table></players-table>
    </v-flex>
    <v-flex></v-flex>
  </v-layout>
</template>

<script>
import PlayersTable from '@/components/dashboard/PlayersTable.vue'
export default {
  name: 'Dashboard',
  props: ['userId'],
  components: {
    PlayersTable
  },
  methods: {
  },
  created () {
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>

</style>
